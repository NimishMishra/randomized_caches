#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSPolicy.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/policy.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSPolicy");
    py::class_<QoSPolicyParams, SimObjectParams, std::unique_ptr<QoSPolicyParams, py::nodelete>>(m, "QoSPolicyParams")
        ;

    py::class_<QoS::Policy, SimObject, std::unique_ptr<QoS::Policy, py::nodelete>>(m, "QoS_COLONS_Policy")
        ;

}

static EmbeddedPyBind embed_obj("QoSPolicy", module_init, "SimObject");
