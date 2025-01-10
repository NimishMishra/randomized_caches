#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "params/SassAssoc.hh"
#include "python/pybind11/core.hh"
#include "sim/init.hh"
#include "sim/sim_object.hh"

#include "mem/cache/tags/sass_assoc.hh"

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("param_SassAssoc");
    py::class_<SassAssocParams, BaseSetAssocParams, std::unique_ptr<SassAssocParams, py::nodelete>>(m, "SassAssocParams")
        .def(py::init<>())
        .def("create", &SassAssocParams::create)
        ;

    py::class_<SassAssoc, BaseSetAssoc, std::unique_ptr<SassAssoc, py::nodelete>>(m, "SassAssoc")
        ;

}

static EmbeddedPyBind embed_obj("SassAssoc", module_init, "BaseSetAssoc");
