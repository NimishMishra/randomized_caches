#ifndef __MEM_CACHE_TAGS_SASS_ASSOC_HH__
#define __MEM_CACHE_TAGS_SASS_ASSOC_HH__

#include "mem/cache/blk.hh"
#include "mem/cache/tags/base_set_assoc.hh"
#include "params/SassAssoc.hh"

class SassAssoc : public BaseSetAssoc
{
  private:
    unsigned char k0[16];
    unsigned char k1[16];
    unsigned char w0[16];
    unsigned char w1[16];

    int index_bits;
    int coverage_t;

    void initializeKeys();

    uint64_t hash(const Addr addr, const unsigned way) const;
    uint64_t hash_second_layer(const uint64_t scatterindex, const unsigned way) const;

  public:
    /** Convenience typedef. */
     typedef SassAssocParams Params;

    SassAssoc(const Params *p);

    ~SassAssoc() {};

    /**
     * Find all possible block locations for insertion and replacement of
     * an address. Should be called immediately before ReplacementPolicy's
     * findVictim() not to break cache resizing.
     * Returns blocks in all ways belonging to the set of the address.
     *
     * @param addr The addr to a find possible locations for.
     * @return The possible locations.
     */
    const std::vector<CacheBlk*> getPossibleLocations(Addr addr, uint64_t securityDomain) const
                                                             override;

    /**
     * Finds the given address in the cache, do not update replacement data.
     * i.e. This is a no-side-effect find of a block.
     *
     * @param addr The address to find.
     * @param is_secure True if the target memory space is secure.
     * @return Pointer to the cache block if found.
     */
    CacheBlk* findBlock(Addr addr, bool is_secure) const override;

    /**
     * Regenerate the block address from the tag, set and way.
     *
     * @param block The block.
     * @return the block address.
     */
    Addr regenerateBlkAddr(const CacheBlk* blk) const override;
};

#endif //__MEM_CACHE_TAGS_SASS_ASSOC_HH__
