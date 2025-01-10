# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Steve Reinhardt

# Simple test script
#
# "m5 test.py"

from __future__ import print_function

import optparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath, fatal, warn

addToPath('../')

from ruby import Ruby

from common import Options
from common import Simulation
from common import CacheConfig
from common import CpuConfig
from common import MemConfig
from common.Caches import *
from common.cpu2000 import *

def get_processes(options):
    """Interprets provided options and returns a list of processes"""

    multiprocesses = []
    inputs = []
    outputs = []
    errouts = []
    pargs = []

    workloads = options.cmd.split(';')
    if options.input != "":
        inputs = options.input.split(';')
    if options.output != "":
        outputs = options.output.split(';')
    if options.errout != "":
        errouts = options.errout.split(';')
    if options.options != "":
        pargs = options.options.split(';')

    idx = 0
    for wrkld in workloads:
        process = Process(pid = 100 + idx)
        process.executable = wrkld
        process.cwd = os.getcwd()

        if options.env:
            with open(options.env, 'r') as f:
                process.env = [line.rstrip() for line in f]

        if len(pargs) > idx:
            process.cmd = [wrkld] + pargs[idx].split()
        else:
            process.cmd = [wrkld]

        if len(inputs) > idx:
            process.input = inputs[idx]
        if len(outputs) > idx:
            process.output = outputs[idx]
        if len(errouts) > idx:
            process.errout = errouts[idx]

        multiprocesses.append(process)
        idx += 1

    if options.smt:
        assert(options.cpu_type == "DerivO3CPU")
        return multiprocesses, idx
    else:
        return multiprocesses, 1


parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)

if '--ruby' in sys.argv:
    Ruby.define_options(parser)

(options, args) = parser.parse_args()

if args:
    print("Error: script doesn't take any positional arguments")
    sys.exit(1)

multiprocesses = []
numThreads = 1
spurious = Process(pid=100)
spurious.executable = "/home/user1/mirage_runs/benchmark_wrappers/spurious_occupancy"
spurious.cmd = [spurious.executable]

multiprocesses.append(spurious)

spec = Process(pid=101)

if(options.cmd == "perlbench"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/500.perlbench_r/build/build_base_perfcount-m64.0000/perlbench_r"
    spec.cmd = [spec.executable] + ['-I/home/user1/mirage_runs/SPEC2017/benchspec/CPU/500.perlbench_r/run/run_base_refrate_perfcount-m64.0000/lib', '/home/user1/mirage_runs/SPEC2017/benchspec/CPU/500.perlbench_r/run/run_base_refrate_perfcount-m64.0000/checkspam.pl', '2500', '5', '25', '11', '150', '1', '1', '1', '1']

elif(options.cmd == "cactu"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/507.cactuBSSN_r/run/run_base_refrate_perfcount-m64.0000/cactusBSSN_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/507.cactuBSSN_r/run/run_base_refrate_perfcount-m64.0000/spec_ref.par"]

elif(options.cmd == "x264"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/525.x264_r/run/run_base_refrate_perfcount-m64.0000/x264_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["--pass", "1", "--stats", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/525.x264_r/run/run_base_refrate_perfcount-m64.0000/x264_stats.log", "--bitrate", "1000",
            "--frames", "1000", "-o", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/525.x264_r/run/run_base_refrate_perfcount-m64.0000/BuckBunny_New.264", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/525.x264_r/run/run_base_refrate_perfcount-m64.0000/BuckBunny.yuv", "1280x720"]

elif(options.cmd == "blender"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/526.blender_r/run/run_base_refrate_perfcount-m64.0000/blender_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/526.blender_r/run/run_base_refrate_perfcount-m64.0000/sh3_no_char.blend", "--render-output", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/526.blender_r/run/run_base_refrate_perfcount-m64.0000/sh3_no_char_", "--threads", "1", "-b", "-F", "RAWTGA", "-s", "849", "-e", "849", "-a"]

elif(options.cmd == "imagick"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/538.imagick_r/run/run_base_refrate_perfcount-m64.0000/imagick_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["-limit", "disk", "0", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/538.imagick_r/run/run_base_refrate_perfcount-m64.0000/refrate_input.tga", "-edge", "41", "-resample", "181%", "-emboss", "31", "-colorspace", "YUV", "-mean-shift", "19x19+15%", "-resize", "30%", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/538.imagick_r/run/run_base_refrate_perfcount-m64.0000/refrate_output.tga"]

elif(options.cmd == "leela"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/541.leela_r/run/run_base_refrate_perfcount-m64.0000/leela_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/541.leela_r/run/run_base_refrate_perfcount-m64.0000/ref.sgf"]

elif(options.cmd == "nab"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/544.nab_r/run/run_base_refrate_perfcount-m64.0000/nab_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/544.nab_r/run/run_base_refrate_perfcount-m64.0000/1am0", "1122214447", "122"]

elif(options.cmd == "fotonik"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/549.fotonik3d_r/run/run_base_refrate_perfcount-m64.0000/fotonik3d_r_base.perfcount-m64"
    spec.cmd = [spec.executable]

elif(options.cmd == "xz"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/557.xz_r/run/run_base_refrate_perfcount-m64.0000/xz_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/557.xz_r/run/run_base_refrate_perfcount-m64.0000/cld.tar.xz", "160",  "19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474", "59796407", "61004416", "6"]

elif(options.cmd == "gcc"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/502.gcc_r/build/build_base_perfcount-m64.0000/cpugcc_r"
    spec.cmd = [spec.executable] + ['/home/user1/mirage_runs/SPEC2017/benchspec/CPU/502.gcc_r/build/build_peak_perfcount-m64.0000/200.c', '-o', '/home/user1/mirage_runs/SPEC2017/benchspec/CPU/502.gcc_r/build/build_peak_perfcount-m64.0000/200.s']

elif(options.cmd == "mcf"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/505.mcf_r/build/build_base_perfcount-m64.0000/mcf_r"
    spec.cmd = [spec.executable] + ['/home/user1/mirage_runs/SPEC2017/benchspec/CPU/505.mcf_r/data/train/input/inp.in']

elif(options.cmd == "namd"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/508.namd_r/build/build_base_perfcount-m64.0000/namd_r"
    spec.cmd = [spec.executable] + ['--input', '/home/user1/mirage_runs/SPEC2017/benchspec/CPU/508.namd_r/data/all/input/apoa1.input', '--output', '/home/user1/mirage_runs/SPEC2017/benchspec/CPU/508.namd_r/data/all/input/namd.out', '--iterations', '38']

elif(options.cmd == "povray"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/511.povray_r/build/build_base_perfcount-m64.0000/povray_r"
    spec.cmd = [spec.executable] + ["/home/user1/mirage_runs/SPEC2017/benchspec/CPU/511.povray_r/data/refrate/input/SPEC-benchmark-ref.ini"]

elif(options.cmd == "lbm"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/519.lbm_r/build/build_base_perfcount-m64.0000/lbm_r"
    spec.cmd = [spec.executable] + ['300', "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/519.lbm_r/data/refrate/input/lbm.in", '0', '0', "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/519.lbm_r/data/refrate/input/100_100_130_ldc.of"]

elif(options.cmd == "omnetpp"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/520.omnetpp_r/run/run_base_refrate_perfcount-m64.0000/omnetpp_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + [omnetpp.executable] + ['-c', "General", "-r", "0"]

elif(options.cmd == "xalancbmk"):
    spec.executable = "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/523.xalancbmk_r/run/run_base_refrate_perfcount-m64.0000/cpuxalan_r_base.perfcount-m64"
    spec.cmd = [spec.executable] + ['-v',"/home/user1/mirage_runs/SPEC2017/benchspec/CPU/523.xalancbmk_r/run/run_base_refrate_perfcount-m64.0000/t5.xml", "/home/user1/mirage_runs/SPEC2017/benchspec/CPU/523.xalancbmk_r/run/run_base_refrate_perfcount-m64.0000/xalanc.xsl"]


multiprocesses.append(spec)
#spec = None


(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if options.smt and options.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = options.num_cpus
system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
                mem_mode = test_mem_mode,
                mem_ranges = [AddrRange(options.mem_size)],
                cache_line_size = options.cacheline_size)

if numThreads > 1:
    system.multi_thread = True

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
                                   voltage_domain = system.voltage_domain)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
                                       voltage_domain =
                                       system.cpu_voltage_domain)

# If elastic tracing is enabled, then configure the cpu and attach the elastic
# trace probe
if options.elastic_trace_en:
    CpuConfig.config_etrace(CPUClass, system.cpu, options)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

if CpuConfig.is_kvm_cpu(CPUClass) or CpuConfig.is_kvm_cpu(FutureClass):
    if buildEnv['TARGET_ISA'] == 'x86':
        system.kvm_vm = KvmVM()
        for process in multiprocesses:
            process.useArchPT = True
            process.kvmInSE = True
    else:
        fatal("KvmCPU can only be used in SE mode with x86")

# Sanity check
if options.simpoint_profile:
    if not CpuConfig.is_atomic_cpu(TestCPUClass):
        fatal("SimPoint/BPProbe should be done with an atomic cpu")
    if np > 1:
        fatal("SimPoint generation not supported with more than one CPUs")

for i in xrange(np):
    if options.smt:
        system.cpu[i].workload = multiprocesses
    elif len(multiprocesses) == 1:
        system.cpu[i].workload = multiprocesses[0]
    else:
        system.cpu[i].workload = multiprocesses[i]

    if options.simpoint_profile:
        system.cpu[i].addSimPointProbe(options.simpoint_interval)

    if options.checker:
        system.cpu[i].addCheckerCpu()

    system.cpu[i].createThreads()

if options.ruby:
    Ruby.create_system(options, False, system)
    assert(options.num_cpus == len(system.ruby._cpu_ports))

    system.ruby.clk_domain = SrcClockDomain(clock = options.ruby_clock,
                                        voltage_domain = system.voltage_domain)
    for i in xrange(np):
        ruby_port = system.ruby._cpu_ports[i]

        # Create the interrupt controller and connect its ports to Ruby
        # Note that the interrupt controller is always present but only
        # in x86 does it have message ports that need to be connected
        system.cpu[i].createInterruptController()

        # Connect the cpu's cache ports to Ruby
        system.cpu[i].icache_port = ruby_port.slave
        system.cpu[i].dcache_port = ruby_port.slave
        if buildEnv['TARGET_ISA'] == 'x86':
            system.cpu[i].interrupts[0].pio = ruby_port.master
            system.cpu[i].interrupts[0].int_master = ruby_port.slave
            system.cpu[i].interrupts[0].int_slave = ruby_port.master
            system.cpu[i].itb.walker.port = ruby_port.slave
            system.cpu[i].dtb.walker.port = ruby_port.slave
else:
    MemClass = Simulation.setMemClass(options)
    system.membus = SystemXBar()
    system.system_port = system.membus.slave
    CacheConfig.config_cache(options, system)
    MemConfig.config_mem(options, system)

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)
