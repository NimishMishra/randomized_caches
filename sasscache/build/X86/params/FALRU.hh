#ifndef __PARAMS__FALRU__
#define __PARAMS__FALRU__

class FALRU;

#include <cstddef>
#include "base/types.hh"

#include "params/BaseTags.hh"

struct FALRUParams
    : public BaseTagsParams
{
    FALRU * create();
    uint64_t min_tracked_cache_size;
};

#endif // __PARAMS__FALRU__
