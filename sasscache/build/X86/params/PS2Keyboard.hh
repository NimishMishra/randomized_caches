#ifndef __PARAMS__PS2Keyboard__
#define __PARAMS__PS2Keyboard__

class PS2Keyboard;

#include <cstddef>
#include "params/VncInput.hh"

#include "params/PS2Device.hh"

struct PS2KeyboardParams
    : public PS2DeviceParams
{
    PS2Keyboard * create();
    VncInput * vnc;
};

#endif // __PARAMS__PS2Keyboard__
