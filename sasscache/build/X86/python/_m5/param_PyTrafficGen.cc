#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/PyTrafficGen.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "cpu/testers/traffic_gen/pygen.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_PyTrafficGen");
    py::class_<PyTrafficGenParams, BaseTrafficGenParams, std::unique_ptr<PyTrafficGenParams, py::nodelete>>(m, "PyTrafficGenParams")
        .def(py::init<>())
        .def("create", &PyTrafficGenParams::create)
        ;

    py::class_<PyTrafficGen, BaseTrafficGen, std::unique_ptr<PyTrafficGen, py::nodelete>>(m, "PyTrafficGen")
        .def("createIdle", &PyTrafficGen::createIdle)
        .def("createExit", &PyTrafficGen::createExit)
        .def("createLinear", &PyTrafficGen::createLinear)
        .def("createRandom", &PyTrafficGen::createRandom)
        .def("createDram", &PyTrafficGen::createDram)
        .def("createDramRot", &PyTrafficGen::createDramRot)
        .def("createTrace", &PyTrafficGen::createTrace, 
            py::arg("duration"), py::arg("trace_file"), py::arg("addr_offset") = 0)
        .def("start", &PyTrafficGen::start, 
            py::arg("meta_generator"))
        ;

}

static EmbeddedPyBind embed_obj("PyTrafficGen", module_init, "BaseTrafficGen");
