#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/SimpleMemDelay.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/mem_delay.hh"

#include "base/types.hh"
#include "base/types.hh"
#include "base/types.hh"
#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_SimpleMemDelay");
    py::class_<SimpleMemDelayParams, MemDelayParams, std::unique_ptr<SimpleMemDelayParams, py::nodelete>>(m, "SimpleMemDelayParams")
        .def(py::init<>())
        .def("create", &SimpleMemDelayParams::create)
        .def_readwrite("read_req", &SimpleMemDelayParams::read_req)
        .def_readwrite("read_resp", &SimpleMemDelayParams::read_resp)
        .def_readwrite("write_req", &SimpleMemDelayParams::write_req)
        .def_readwrite("write_resp", &SimpleMemDelayParams::write_resp)
        ;

    py::class_<SimpleMemDelay, MemDelay, std::unique_ptr<SimpleMemDelay, py::nodelete>>(m, "SimpleMemDelay")
        ;

}

static EmbeddedPyBind embed_obj("SimpleMemDelay", module_init, "MemDelay");
