#ifndef __PARAMS__SassAssoc__
#define __PARAMS__SassAssoc__

class SassAssoc;


#include "params/BaseSetAssoc.hh"

struct SassAssocParams
    : public BaseSetAssocParams
{
    SassAssoc * create();
};

#endif // __PARAMS__SassAssoc__
