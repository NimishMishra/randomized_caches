#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/SectorTags.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/tags/sector_tags.hh"

#include "base/types.hh"
#include "base/types.hh"
#include "mem/cache/replacement_policies/base.hh"
namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_SectorTags");
    py::class_<SectorTagsParams, BaseTagsParams, std::unique_ptr<SectorTagsParams, py::nodelete>>(m, "SectorTagsParams")
        .def(py::init<>())
        .def("create", &SectorTagsParams::create)
        .def_readwrite("assoc", &SectorTagsParams::assoc)
        .def_readwrite("num_blocks_per_sector", &SectorTagsParams::num_blocks_per_sector)
        .def_readwrite("replacement_policy", &SectorTagsParams::replacement_policy)
        ;

    py::class_<SectorTags, BaseTags, std::unique_ptr<SectorTags, py::nodelete>>(m, "SectorTags")
        ;

}

static EmbeddedPyBind embed_obj("SectorTags", module_init, "BaseTags");
