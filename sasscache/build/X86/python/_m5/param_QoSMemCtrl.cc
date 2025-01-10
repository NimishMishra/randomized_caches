#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSMemCtrl.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/mem_ctrl.hh"

#include <vector>
#include <string>
#include "mem/qos/policy.hh"
#include "base/types.hh"
#include "enums/QoSQPolicy.hh"
#include "mem/qos/turnaround_policy.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSMemCtrl");
    py::class_<QoSMemCtrlParams, AbstractMemoryParams, std::unique_ptr<QoSMemCtrlParams, py::nodelete>>(m, "QoSMemCtrlParams")
        .def_readwrite("qos_masters", &QoSMemCtrlParams::qos_masters)
        .def_readwrite("qos_policy", &QoSMemCtrlParams::qos_policy)
        .def_readwrite("qos_priorities", &QoSMemCtrlParams::qos_priorities)
        .def_readwrite("qos_priority_escalation", &QoSMemCtrlParams::qos_priority_escalation)
        .def_readwrite("qos_q_policy", &QoSMemCtrlParams::qos_q_policy)
        .def_readwrite("qos_syncro_scheduler", &QoSMemCtrlParams::qos_syncro_scheduler)
        .def_readwrite("qos_turnaround_policy", &QoSMemCtrlParams::qos_turnaround_policy)
        ;

    py::class_<QoS::MemCtrl, AbstractMemory, std::unique_ptr<QoS::MemCtrl, py::nodelete>>(m, "QoS_COLONS_MemCtrl")
        ;

}

static EmbeddedPyBind embed_obj("QoSMemCtrl", module_init, "AbstractMemory");
