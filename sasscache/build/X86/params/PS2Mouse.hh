#ifndef __PARAMS__PS2Mouse__
#define __PARAMS__PS2Mouse__

class PS2Mouse;


#include "params/PS2Device.hh"

struct PS2MouseParams
    : public PS2DeviceParams
{
    PS2Mouse * create();
};

#endif // __PARAMS__PS2Mouse__
