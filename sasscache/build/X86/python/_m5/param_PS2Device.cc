#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/PS2Device.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "dev/ps2/device.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_PS2Device");
    py::class_<PS2DeviceParams, SimObjectParams, std::unique_ptr<PS2DeviceParams, py::nodelete>>(m, "PS2DeviceParams")
        ;

    py::class_<PS2Device, SimObject, std::unique_ptr<PS2Device, py::nodelete>>(m, "PS2Device")
        ;

}

static EmbeddedPyBind embed_obj("PS2Device", module_init, "SimObject");
