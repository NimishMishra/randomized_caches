#ifndef __PARAMS__BaseTrafficGen__
#define __PARAMS__BaseTrafficGen__

class BaseTrafficGen;

#include <cstddef>
#include <cstddef>
#include "base/types.hh"
#include <vector>
#include "base/types.hh"
#include <vector>
#include "base/types.hh"
#include <cstddef>
#include "enums/StreamGenType.hh"
#include <cstddef>
#include "params/System.hh"

#include "params/MemObject.hh"

#include "enums/StreamGenType.hh"

struct BaseTrafficGenParams
    : public MemObjectParams
{
    bool elastic_req;
    Tick progress_check;
    std::vector< unsigned > sids;
    std::vector< unsigned > ssids;
    Enums::StreamGenType stream_gen;
    System * system;
    unsigned int port_port_connection_count;
};

#endif // __PARAMS__BaseTrafficGen__
