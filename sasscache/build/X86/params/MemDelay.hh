#ifndef __PARAMS__MemDelay__
#define __PARAMS__MemDelay__

class MemDelay;


#include "params/MemObject.hh"

struct MemDelayParams
    : public MemObjectParams
{
    unsigned int port_master_connection_count;
    unsigned int port_slave_connection_count;
};

#endif // __PARAMS__MemDelay__
