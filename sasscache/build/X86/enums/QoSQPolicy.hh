#ifndef __ENUM__Enums__QoSQPolicy__
#define __ENUM__Enums__QoSQPolicy__

namespace Enums {
    enum QoSQPolicy {
        fifo = 0,
        lifo = 1,
        lrg = 2,
        Num_QoSQPolicy = 3
    };
extern const char *QoSQPolicyStrings[Num_QoSQPolicy];
}

#endif // __ENUM__Enums__QoSQPolicy__
