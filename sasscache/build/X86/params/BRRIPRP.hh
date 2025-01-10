#ifndef __PARAMS__BRRIPRP__
#define __PARAMS__BRRIPRP__

class BRRIPRP;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include <cstddef>
#include "base/types.hh"

#include "params/BaseReplacementPolicy.hh"

struct BRRIPRPParams
    : public BaseReplacementPolicyParams
{
    BRRIPRP * create();
    int btp;
    bool hit_priority;
    int max_RRPV;
};

#endif // __PARAMS__BRRIPRP__
