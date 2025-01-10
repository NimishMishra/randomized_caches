#ifndef __PARAMS__BIPRP__
#define __PARAMS__BIPRP__

class BIPRP;

#include <cstddef>
#include "base/types.hh"

#include "params/LRURP.hh"

struct BIPRPParams
    : public LRURPParams
{
    BIPRP * create();
    int btp;
};

#endif // __PARAMS__BIPRP__
