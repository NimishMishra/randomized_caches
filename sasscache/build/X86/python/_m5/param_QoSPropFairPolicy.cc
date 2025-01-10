#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSPropFairPolicy.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/policy_pf.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSPropFairPolicy");
    py::class_<QoSPropFairPolicyParams, QoSPolicyParams, std::unique_ptr<QoSPropFairPolicyParams, py::nodelete>>(m, "QoSPropFairPolicyParams")
        .def(py::init<>())
        .def("create", &QoSPropFairPolicyParams::create)
        .def_readwrite("weight", &QoSPropFairPolicyParams::weight)
        ;

    py::class_<QoS::PropFairPolicy, QoS::Policy, std::unique_ptr<QoS::PropFairPolicy, py::nodelete>>(m, "QoS_COLONS_PropFairPolicy")
        .def("initMasterName", &QoS::PropFairPolicy::initMasterName)
        .def("initMasterObj", &QoS::PropFairPolicy::initMasterObj)
        ;

}

static EmbeddedPyBind embed_obj("QoSPropFairPolicy", module_init, "QoSPolicy");
