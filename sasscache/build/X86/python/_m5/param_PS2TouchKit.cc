#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/PS2TouchKit.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "dev/ps2/touchkit.hh"

#include "base/vnc/vncinput.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_PS2TouchKit");
    py::class_<PS2TouchKitParams, PS2DeviceParams, std::unique_ptr<PS2TouchKitParams, py::nodelete>>(m, "PS2TouchKitParams")
        .def(py::init<>())
        .def("create", &PS2TouchKitParams::create)
        .def_readwrite("vnc", &PS2TouchKitParams::vnc)
        ;

    py::class_<PS2TouchKit, PS2Device, std::unique_ptr<PS2TouchKit, py::nodelete>>(m, "PS2TouchKit")
        ;

}

static EmbeddedPyBind embed_obj("PS2TouchKit", module_init, "PS2Device");
