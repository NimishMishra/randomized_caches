#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/NoncoherentCache.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/noncoherent_cache.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_NoncoherentCache");
    py::class_<NoncoherentCacheParams, BaseCacheParams, std::unique_ptr<NoncoherentCacheParams, py::nodelete>>(m, "NoncoherentCacheParams")
        .def(py::init<>())
        .def("create", &NoncoherentCacheParams::create)
        ;

    py::class_<NoncoherentCache, BaseCache, std::unique_ptr<NoncoherentCache, py::nodelete>>(m, "NoncoherentCache")
        ;

}

static EmbeddedPyBind embed_obj("NoncoherentCache", module_init, "BaseCache");
