#ifndef __PARAMS__PyTrafficGen__
#define __PARAMS__PyTrafficGen__

class PyTrafficGen;


#include "params/BaseTrafficGen.hh"

struct PyTrafficGenParams
    : public BaseTrafficGenParams
{
    PyTrafficGen * create();
};

#endif // __PARAMS__PyTrafficGen__
