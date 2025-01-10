#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/LFURP.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/replacement_policies/lfu_rp.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_LFURP");
    py::class_<LFURPParams, BaseReplacementPolicyParams, std::unique_ptr<LFURPParams, py::nodelete>>(m, "LFURPParams")
        .def(py::init<>())
        .def("create", &LFURPParams::create)
        ;

    py::class_<LFURP, BaseReplacementPolicy, std::unique_ptr<LFURP, py::nodelete>>(m, "LFURP")
        ;

}

static EmbeddedPyBind embed_obj("LFURP", module_init, "BaseReplacementPolicy");
