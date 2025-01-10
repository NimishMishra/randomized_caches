#include "enums/StreamGenType.hh"
namespace Enums {
     const char *StreamGenTypeStrings[Num_StreamGenType] =
    {
        "none",
        "fixed",
        "random",
    };
    } // namespace Enums
#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include <sim/init.hh>

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("enum_StreamGenType");

    py::enum_<Enums::StreamGenType>(m, "enum_StreamGenType")
        .value("none", Enums::none)
        .value("fixed", Enums::fixed)
        .value("random", Enums::random)
        .value("Num_StreamGenType", Enums::Num_StreamGenType)
        .export_values()
        ;
    }

static EmbeddedPyBind embed_enum("enum_StreamGenType", module_init);
