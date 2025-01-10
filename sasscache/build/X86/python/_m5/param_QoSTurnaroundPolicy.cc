#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSTurnaroundPolicy.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/turnaround_policy.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSTurnaroundPolicy");
    py::class_<QoSTurnaroundPolicyParams, SimObjectParams, std::unique_ptr<QoSTurnaroundPolicyParams, py::nodelete>>(m, "QoSTurnaroundPolicyParams")
        ;

    py::class_<QoS::TurnaroundPolicy, SimObject, std::unique_ptr<QoS::TurnaroundPolicy, py::nodelete>>(m, "QoS_COLONS_TurnaroundPolicy")
        ;

}

static EmbeddedPyBind embed_obj("QoSTurnaroundPolicy", module_init, "SimObject");
