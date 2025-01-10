#ifndef __PARAMS__SimpleMemDelay__
#define __PARAMS__SimpleMemDelay__

class SimpleMemDelay;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/MemDelay.hh"

struct SimpleMemDelayParams
    : public MemDelayParams
{
    SimpleMemDelay * create();
    Tick read_req;
    Tick read_resp;
    Tick write_req;
    Tick write_resp;
};

#endif // __PARAMS__SimpleMemDelay__
