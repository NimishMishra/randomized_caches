#ifndef __PARAMS__NoncoherentCache__
#define __PARAMS__NoncoherentCache__

class NoncoherentCache;


#include "params/BaseCache.hh"

struct NoncoherentCacheParams
    : public BaseCacheParams
{
    NoncoherentCache * create();
};

#endif // __PARAMS__NoncoherentCache__
