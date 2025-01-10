#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/QoSMemSinkCtrl.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/qos/mem_sink.hh"

#include "base/types.hh"
#include "base/types.hh"
#include "base/types.hh"
#include "base/types.hh"
#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_QoSMemSinkCtrl");
    py::class_<QoSMemSinkCtrlParams, QoSMemCtrlParams, std::unique_ptr<QoSMemSinkCtrlParams, py::nodelete>>(m, "QoSMemSinkCtrlParams")
        .def(py::init<>())
        .def("create", &QoSMemSinkCtrlParams::create)
        .def_readwrite("memory_packet_size", &QoSMemSinkCtrlParams::memory_packet_size)
        .def_readwrite("read_buffer_size", &QoSMemSinkCtrlParams::read_buffer_size)
        .def_readwrite("request_latency", &QoSMemSinkCtrlParams::request_latency)
        .def_readwrite("response_latency", &QoSMemSinkCtrlParams::response_latency)
        .def_readwrite("write_buffer_size", &QoSMemSinkCtrlParams::write_buffer_size)
        .def_readwrite("port_port_connection_count", &QoSMemSinkCtrlParams::port_port_connection_count)
        ;

    py::class_<QoS::MemSinkCtrl, QoS::MemCtrl, std::unique_ptr<QoS::MemSinkCtrl, py::nodelete>>(m, "QoS_COLONS_MemSinkCtrl")
        ;

}

static EmbeddedPyBind embed_obj("QoSMemSinkCtrl", module_init, "QoSMemCtrl");
