#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/SimpleUart.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "dev/serial/simple.hh"

#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_SimpleUart");
    py::class_<SimpleUartParams, UartParams, std::unique_ptr<SimpleUartParams, py::nodelete>>(m, "SimpleUartParams")
        .def(py::init<>())
        .def("create", &SimpleUartParams::create)
        .def_readwrite("big_endian", &SimpleUartParams::big_endian)
        .def_readwrite("end_on_eot", &SimpleUartParams::end_on_eot)
        .def_readwrite("pio_size", &SimpleUartParams::pio_size)
        ;

    py::class_<SimpleUart, Uart, std::unique_ptr<SimpleUart, py::nodelete>>(m, "SimpleUart")
        ;

}

static EmbeddedPyBind embed_obj("SimpleUart", module_init, "Uart");
