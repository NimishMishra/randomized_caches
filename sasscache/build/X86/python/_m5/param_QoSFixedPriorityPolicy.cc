#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSFixedPriorityPolicy.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/policy_fixed_prio.hh"

#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSFixedPriorityPolicy");
    py::class_<QoSFixedPriorityPolicyParams, QoSPolicyParams, std::unique_ptr<QoSFixedPriorityPolicyParams, py::nodelete>>(m, "QoSFixedPriorityPolicyParams")
        .def(py::init<>())
        .def("create", &QoSFixedPriorityPolicyParams::create)
        .def_readwrite("qos_fixed_prio_default_prio", &QoSFixedPriorityPolicyParams::qos_fixed_prio_default_prio)
        ;

    py::class_<QoS::FixedPriorityPolicy, QoS::Policy, std::unique_ptr<QoS::FixedPriorityPolicy, py::nodelete>>(m, "QoS_COLONS_FixedPriorityPolicy")
        .def("initMasterName", &QoS::FixedPriorityPolicy::initMasterName)
        .def("initMasterObj", &QoS::FixedPriorityPolicy::initMasterObj)
        ;

}

static EmbeddedPyBind embed_obj("QoSFixedPriorityPolicy", module_init, "QoSPolicy");
