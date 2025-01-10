#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/MemDelay.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/mem_delay.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_MemDelay");
    py::class_<MemDelayParams, MemObjectParams, std::unique_ptr<MemDelayParams, py::nodelete>>(m, "MemDelayParams")
        .def_readwrite("port_master_connection_count", &MemDelayParams::port_master_connection_count)
        .def_readwrite("port_slave_connection_count", &MemDelayParams::port_slave_connection_count)
        ;

    py::class_<MemDelay, MemObject, std::unique_ptr<MemDelay, py::nodelete>>(m, "MemDelay")
        ;

}

static EmbeddedPyBind embed_obj("MemDelay", module_init, "MemObject");
