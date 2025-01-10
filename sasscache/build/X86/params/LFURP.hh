#ifndef __PARAMS__LFURP__
#define __PARAMS__LFURP__

class LFURP;


#include "params/BaseReplacementPolicy.hh"

struct LFURPParams
    : public BaseReplacementPolicyParams
{
    LFURP * create();
};

#endif // __PARAMS__LFURP__
