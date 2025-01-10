/** \file DMA_TBE.cc
 *
 * Auto generated C++ code started by /home/user1/mirage_runs/sasscache/src/mem/slicc/symbols/Type.py:411
 */

#include <iostream>
#include <memory>

#include "mem/protocol/DMA_TBE.hh"
#include "mem/ruby/system/RubySystem.hh"

using namespace std;
/** \brief Print the state of this object */
void
DMA_TBE::print(ostream& out) const
{
    out << "[DMA_TBE: ";
    out << "TBEState = " << m_TBEState << " ";
    out << "DataBlk = " << m_DataBlk << " ";
    out << "]";
}
