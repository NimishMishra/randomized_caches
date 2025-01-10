#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/NonCachingSimpleCPU.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "cpu/simple/noncaching.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_NonCachingSimpleCPU");
    py::class_<NonCachingSimpleCPUParams, AtomicSimpleCPUParams, std::unique_ptr<NonCachingSimpleCPUParams, py::nodelete>>(m, "NonCachingSimpleCPUParams")
        .def(py::init<>())
        .def("create", &NonCachingSimpleCPUParams::create)
        ;

    py::class_<NonCachingSimpleCPU, AtomicSimpleCPU, std::unique_ptr<NonCachingSimpleCPU, py::nodelete>>(m, "NonCachingSimpleCPU")
        ;

}

static EmbeddedPyBind embed_obj("NonCachingSimpleCPU", module_init, "AtomicSimpleCPU");
