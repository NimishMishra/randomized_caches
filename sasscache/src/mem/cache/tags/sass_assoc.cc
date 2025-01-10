#include "mem/cache/tags/sass_assoc.hh"

#include <vector>

#include "base/bitfield.hh"
#include "base/logging.hh"
#include "crypto/qarma64.h"

SassAssoc::SassAssoc(const Params *p)
    : BaseSetAssoc(p)
{
    // We must have more than two sets
    fatal_if(numSets < 2, "The number of sets must be greater than 2");
    fatal_if(assoc > 16, "The number of ways must be less or equal than 16");

    index_bits = floorLog2(numSets);

    coverage_t = -1;

    // We also store the set bits with the tag to enable the use of a
    // (noninvertible) hash function for set index calculation.
    tagShift = setShift;

    initializeKeys();
}

void SassAssoc::initializeKeys() {
    int i;
    unsigned char k1_M[16];

    for (i = 0; i < 16; i++) {
        k0[i] = i;
        w0[i] = ~(16-i) & 0xf;
    }

    qarma64KeySpecialisation(k0, w0, k1, k1_M, w1);
}

uint64_t
SassAssoc::hash(const Addr addr, const unsigned way) const
{
    int i;
    int R = 6;
    unsigned char p[16], t[16];

    Addr original_tag_and_set = addr >> setShift;

    // The following qarma implementation computes on nibbles. Split the
    // address accordingly.
    for (i = 0; i < 16; i++) {
        p[i] = (original_tag_and_set >> 4*i) & 0xf;
        t[i] = 0;
    }
    t[0] = way & 0xf;

    qarma64Encrypt(p, w0, w1, k0, k1, t, R);

    // Reconstruct the result which is computed in nibbles.
    uint64_t h = 0;
    for (i = 0; i < 16; i++) {
        h = h | (((uint64_t)p[i]) << 4*i);
    }

    return h;
}

uint64_t
SassAssoc::hash_second_layer(const uint64_t scatterindex, const unsigned way) const
{
    int i;
    int R = 6;
    unsigned char p[16], t[16];

    // TODO: we assume the number of ways can always be represented with 8 bit, maybe use a different function i the future
    Addr original_tag_and_set = ((Addr) (way & 0xFF) << ((sizeof(Addr)-1)*8)) | (scatterindex & setMask);

    // The following qarma implementation computes on nibbles. Split the
    // address accordingly.
    for (i = 0; i < 16; i++) {
        p[i] = (original_tag_and_set >> 4*i) & 0xf;
        // DPRINTF(Cache, "hash p[%d] = %x\n", i, p[i]);
        t[i] = 0;
    }
    // TODO Tweak is set to zero atm and not used. Way i part of the block
    // t[0] = way & 0xf;

    qarma64Encrypt(p, w0, w1, k0, k1, t, R);

    // Reconstruct the result which is computed in nibbles.
    uint64_t h = 0;
    for (i = 0; i < 16; i++) {
        h = h | (((uint64_t)p[i]) << 4*i);
    }
    return h;
}

Addr
SassAssoc::regenerateBlkAddr(const CacheBlk* blk) const
{
    // note that the tag includes the set bits here
    return (blk->tag << tagShift);
}

const std::vector<CacheBlk*>
SassAssoc::getPossibleLocations(Addr addr, uint64_t securityDomain) const
{
    std::vector<unsigned> scatterlocations;
    int ways_per_hash = 64/(index_bits + coverage_t); //parameter t
    // DPRINTF(Sasscache, "getPossibleLocations() for \n");

    int coverage_set_mask = (1 << (index_bits + coverage_t)) - 1;


    // Hash the address and extract as many bits as possible from a single
    // primitive invocation.
    int way = 0;
    while ( way < assoc ) {
        uint64_t digest = hash(addr, way);
        for (int ctr = 0; ctr < ways_per_hash
            && way < assoc; ++ctr, ++way, digest >>= (index_bits + coverage_t)) {
            // Extract the set index from the digest
            unsigned idx = digest & coverage_set_mask;
            scatterlocations.push_back(idx);
        }
    }

    // DPRINTF(Cache, "setMask = %x\n", setMask);
    std::vector<CacheBlk*> locations;
    for(way = 0; way < assoc; way++) {
        
        uint64_t digest = hash_second_layer(scatterlocations.at(way), way);

        // Extract the set index from the digest
        unsigned idx = digest & setMask;
    
        locations.push_back(sets[idx].blks[way]);
    }


    

    return locations;
}

CacheBlk*
SassAssoc::findBlock(Addr addr, bool is_secure) const
{
    // Extract block tag
    Addr tag = extractTag(addr);

    // Find possible locations for the given address
    std::vector<CacheBlk*> locations = getPossibleLocations(addr, 0);

    // Search for block
    for (const auto& blk : locations) {
        if ((blk->tag == tag) && blk->isValid() &&
            (blk->isSecure() == is_secure)) {
            return blk;
        }
    }

    // Did not find block
    return nullptr;
}

SassAssoc *SassAssocParams::create()
{
    return new SassAssoc(this);
}
