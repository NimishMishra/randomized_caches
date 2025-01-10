#ifndef __PARAMS__SectorTags__
#define __PARAMS__SectorTags__

class SectorTags;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/BaseReplacementPolicy.hh"

#include "params/BaseTags.hh"

struct SectorTagsParams
    : public BaseTagsParams
{
    SectorTags * create();
    int assoc;
    int num_blocks_per_sector;
    BaseReplacementPolicy * replacement_policy;
};

#endif // __PARAMS__SectorTags__
