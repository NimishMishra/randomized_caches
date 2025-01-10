#ifndef __PARAMS__Cache__
#define __PARAMS__Cache__

class Cache;


#include "params/BaseCache.hh"

struct CacheParams
    : public BaseCacheParams
{
    Cache * create();
};

#endif // __PARAMS__Cache__
