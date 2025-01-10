#ifndef __PARAMS__QoSMemSinkCtrl__
#define __PARAMS__QoSMemSinkCtrl__

namespace QoS {
class MemSinkCtrl;
} // namespace QoS

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/QoSMemCtrl.hh"

struct QoSMemSinkCtrlParams
    : public QoSMemCtrlParams
{
    QoS::MemSinkCtrl * create();
    uint64_t memory_packet_size;
    unsigned read_buffer_size;
    Tick request_latency;
    Tick response_latency;
    unsigned write_buffer_size;
    unsigned int port_port_connection_count;
};

#endif // __PARAMS__QoSMemSinkCtrl__
