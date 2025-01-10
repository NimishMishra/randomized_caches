#ifndef __ENUM__Enums__StreamGenType__
#define __ENUM__Enums__StreamGenType__

namespace Enums {
    enum StreamGenType {
        none = 0,
        fixed = 1,
        random = 2,
        Num_StreamGenType = 3
    };
extern const char *StreamGenTypeStrings[Num_StreamGenType];
}

#endif // __ENUM__Enums__StreamGenType__
