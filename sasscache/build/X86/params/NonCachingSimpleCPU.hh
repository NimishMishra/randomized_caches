#ifndef __PARAMS__NonCachingSimpleCPU__
#define __PARAMS__NonCachingSimpleCPU__

class NonCachingSimpleCPU;


#include "params/AtomicSimpleCPU.hh"

struct NonCachingSimpleCPUParams
    : public AtomicSimpleCPUParams
{
    NonCachingSimpleCPU * create();
};

#endif // __PARAMS__NonCachingSimpleCPU__
