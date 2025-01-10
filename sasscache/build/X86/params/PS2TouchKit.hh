#ifndef __PARAMS__PS2TouchKit__
#define __PARAMS__PS2TouchKit__

class PS2TouchKit;

#include <cstddef>
#include "params/VncInput.hh"

#include "params/PS2Device.hh"

struct PS2TouchKitParams
    : public PS2DeviceParams
{
    PS2TouchKit * create();
    VncInput * vnc;
};

#endif // __PARAMS__PS2TouchKit__
