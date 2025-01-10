#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/BaseTrafficGen.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "cpu/testers/traffic_gen/traffic_gen.hh"

#include "base/types.hh"
#include <vector>
#include "base/types.hh"
#include <vector>
#include "base/types.hh"
#include "enums/StreamGenType.hh"
#include "sim/system.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_BaseTrafficGen");
    py::class_<BaseTrafficGenParams, MemObjectParams, std::unique_ptr<BaseTrafficGenParams, py::nodelete>>(m, "BaseTrafficGenParams")
        .def_readwrite("elastic_req", &BaseTrafficGenParams::elastic_req)
        .def_readwrite("progress_check", &BaseTrafficGenParams::progress_check)
        .def_readwrite("sids", &BaseTrafficGenParams::sids)
        .def_readwrite("ssids", &BaseTrafficGenParams::ssids)
        .def_readwrite("stream_gen", &BaseTrafficGenParams::stream_gen)
        .def_readwrite("system", &BaseTrafficGenParams::system)
        .def_readwrite("port_port_connection_count", &BaseTrafficGenParams::port_port_connection_count)
        ;

    py::class_<BaseTrafficGen, MemObject, std::unique_ptr<BaseTrafficGen, py::nodelete>>(m, "BaseTrafficGen")
        ;

}

static EmbeddedPyBind embed_obj("BaseTrafficGen", module_init, "MemObject");
