#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSTurnaroundPolicyIdeal.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/turnaround_policy_ideal.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSTurnaroundPolicyIdeal");
    py::class_<QoSTurnaroundPolicyIdealParams, QoSTurnaroundPolicyParams, std::unique_ptr<QoSTurnaroundPolicyIdealParams, py::nodelete>>(m, "QoSTurnaroundPolicyIdealParams")
        .def(py::init<>())
        .def("create", &QoSTurnaroundPolicyIdealParams::create)
        ;

    py::class_<QoS::TurnaroundPolicyIdeal, QoS::TurnaroundPolicy, std::unique_ptr<QoS::TurnaroundPolicyIdeal, py::nodelete>>(m, "QoS_COLONS_TurnaroundPolicyIdeal")
        ;

}

static EmbeddedPyBind embed_obj("QoSTurnaroundPolicyIdeal", module_init, "QoSTurnaroundPolicy");
