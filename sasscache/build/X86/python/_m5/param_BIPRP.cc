#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/BIPRP.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/replacement_policies/bip_rp.hh"

#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_BIPRP");
    py::class_<BIPRPParams, LRURPParams, std::unique_ptr<BIPRPParams, py::nodelete>>(m, "BIPRPParams")
        .def(py::init<>())
        .def("create", &BIPRPParams::create)
        .def_readwrite("btp", &BIPRPParams::btp)
        ;

    py::class_<BIPRP, LRURP, std::unique_ptr<BIPRP, py::nodelete>>(m, "BIPRP")
        ;

}

static EmbeddedPyBind embed_obj("BIPRP", module_init, "LRURP");
