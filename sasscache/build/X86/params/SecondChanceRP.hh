#ifndef __PARAMS__SecondChanceRP__
#define __PARAMS__SecondChanceRP__

class SecondChanceRP;


#include "params/FIFORP.hh"

struct SecondChanceRPParams
    : public FIFORPParams
{
    SecondChanceRP * create();
};

#endif // __PARAMS__SecondChanceRP__
