#ifndef __PARAMS__QoSMemCtrl__
#define __PARAMS__QoSMemCtrl__

namespace QoS {
class MemCtrl;
} // namespace QoS

#include <vector>
#include <string>
#include <cstddef>
#include "params/QoSPolicy.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include <cstddef>
#include "enums/QoSQPolicy.hh"
#include <cstddef>
#include <cstddef>
#include "params/QoSTurnaroundPolicy.hh"

#include "params/AbstractMemory.hh"

#include "enums/QoSQPolicy.hh"

struct QoSMemCtrlParams
    : public AbstractMemoryParams
{
    std::vector< std::string > qos_masters;
    QoS::Policy * qos_policy;
    unsigned qos_priorities;
    bool qos_priority_escalation;
    Enums::QoSQPolicy qos_q_policy;
    bool qos_syncro_scheduler;
    QoS::TurnaroundPolicy * qos_turnaround_policy;
};

#endif // __PARAMS__QoSMemCtrl__
