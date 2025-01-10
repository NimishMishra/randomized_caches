#include "enums/QoSQPolicy.hh"
namespace Enums {
     const char *QoSQPolicyStrings[Num_QoSQPolicy] =
    {
        "fifo",
        "lifo",
        "lrg",
    };
    } // namespace Enums
#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include <sim/init.hh>

namespace py = pybind11;

static void
module_init(py::module &m_internal)
{
    py::module m = m_internal.def_submodule("enum_QoSQPolicy");

    py::enum_<Enums::QoSQPolicy>(m, "enum_QoSQPolicy")
        .value("fifo", Enums::fifo)
        .value("lifo", Enums::lifo)
        .value("lrg", Enums::lrg)
        .value("Num_QoSQPolicy", Enums::Num_QoSQPolicy)
        .export_values()
        ;
    }

static EmbeddedPyBind embed_enum("enum_QoSQPolicy", module_init);
