#ifndef __PARAMS__QoSTurnaroundPolicyIdeal__
#define __PARAMS__QoSTurnaroundPolicyIdeal__

namespace QoS {
class TurnaroundPolicyIdeal;
} // namespace QoS


#include "params/QoSTurnaroundPolicy.hh"

struct QoSTurnaroundPolicyIdealParams
    : public QoSTurnaroundPolicyParams
{
    QoS::TurnaroundPolicyIdeal * create();
};

#endif // __PARAMS__QoSTurnaroundPolicyIdeal__
