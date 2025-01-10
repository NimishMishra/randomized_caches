#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/PS2Mouse.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "dev/ps2/mouse.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_PS2Mouse");
    py::class_<PS2MouseParams, PS2DeviceParams, std::unique_ptr<PS2MouseParams, py::nodelete>>(m, "PS2MouseParams")
        .def(py::init<>())
        .def("create", &PS2MouseParams::create)
        ;

    py::class_<PS2Mouse, PS2Device, std::unique_ptr<PS2Mouse, py::nodelete>>(m, "PS2Mouse")
        ;

}

static EmbeddedPyBind embed_obj("PS2Mouse", module_init, "PS2Device");
