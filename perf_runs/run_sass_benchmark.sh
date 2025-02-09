#!/bin/bash

gcc -o ../randomized_cache_hello_world/spurious_occupancy ../randomized_cache_hello_world/spurious_occupancy.c -static

# Run Sasscache SPEC2017 benchmark

../sasscache/build/X86/gem5.opt ../sasscache/configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=$1 --l2_rp=$2 --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16

