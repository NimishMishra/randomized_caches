#ifndef __PARAMS__SimpleUart__
#define __PARAMS__SimpleUart__

class SimpleUart;

#include <cstddef>
#include <cstddef>
#include <cstddef>
#include "base/types.hh"

#include "params/Uart.hh"

struct SimpleUartParams
    : public UartParams
{
    SimpleUart * create();
    bool big_endian;
    bool end_on_eot;
    Addr pio_size;
};

#endif // __PARAMS__SimpleUart__
