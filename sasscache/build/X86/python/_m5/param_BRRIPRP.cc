#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/BRRIPRP.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/replacement_policies/brrip_rp.hh"

#include "base/types.hh"
#include "base/types.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_BRRIPRP");
    py::class_<BRRIPRPParams, BaseReplacementPolicyParams, std::unique_ptr<BRRIPRPParams, py::nodelete>>(m, "BRRIPRPParams")
        .def(py::init<>())
        .def("create", &BRRIPRPParams::create)
        .def_readwrite("btp", &BRRIPRPParams::btp)
        .def_readwrite("hit_priority", &BRRIPRPParams::hit_priority)
        .def_readwrite("max_RRPV", &BRRIPRPParams::max_RRPV)
        ;

    py::class_<BRRIPRP, BaseReplacementPolicy, std::unique_ptr<BRRIPRP, py::nodelete>>(m, "BRRIPRP")
        ;

}

static EmbeddedPyBind embed_obj("BRRIPRP", module_init, "BaseReplacementPolicy");
