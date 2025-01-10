#ifndef __PARAMS__QoSFixedPriorityPolicy__
#define __PARAMS__QoSFixedPriorityPolicy__

namespace QoS {
class FixedPriorityPolicy;
} // namespace QoS

#include <cstddef>
#include "base/types.hh"

#include "params/QoSPolicy.hh"

struct QoSFixedPriorityPolicyParams
    : public QoSPolicyParams
{
    QoS::FixedPriorityPolicy * create();
    uint8_t qos_fixed_prio_default_prio;
};

#endif // __PARAMS__QoSFixedPriorityPolicy__
