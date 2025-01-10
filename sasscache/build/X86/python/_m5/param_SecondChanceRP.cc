#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/SecondChanceRP.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/replacement_policies/second_chance_rp.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_SecondChanceRP");
    py::class_<SecondChanceRPParams, FIFORPParams, std::unique_ptr<SecondChanceRPParams, py::nodelete>>(m, "SecondChanceRPParams")
        .def(py::init<>())
        .def("create", &SecondChanceRPParams::create)
        ;

    py::class_<SecondChanceRP, FIFORP, std::unique_ptr<SecondChanceRP, py::nodelete>>(m, "SecondChanceRP")
        ;

}

static EmbeddedPyBind embed_obj("SecondChanceRP", module_init, "FIFORP");
