#ifndef __PARAMS__QoSPropFairPolicy__
#define __PARAMS__QoSPropFairPolicy__

namespace QoS {
class PropFairPolicy;
} // namespace QoS

#include <cstddef>

#include "params/QoSPolicy.hh"

struct QoSPropFairPolicyParams
    : public QoSPolicyParams
{
    QoS::PropFairPolicy * create();
    double weight;
};

#endif // __PARAMS__QoSPropFairPolicy__
