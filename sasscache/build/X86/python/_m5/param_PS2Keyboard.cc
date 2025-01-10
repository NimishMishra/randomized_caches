#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/PS2Keyboard.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "dev/ps2/keyboard.hh"

#include "base/vnc/vncinput.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_PS2Keyboard");
    py::class_<PS2KeyboardParams, PS2DeviceParams, std::unique_ptr<PS2KeyboardParams, py::nodelete>>(m, "PS2KeyboardParams")
        .def(py::init<>())
        .def("create", &PS2KeyboardParams::create)
        .def_readwrite("vnc", &PS2KeyboardParams::vnc)
        ;

    py::class_<PS2Keyboard, PS2Device, std::unique_ptr<PS2Keyboard, py::nodelete>>(m, "PS2Keyboard")
        ;

}

static EmbeddedPyBind embed_obj("PS2Keyboard", module_init, "PS2Device");
