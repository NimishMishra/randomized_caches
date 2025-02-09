#!/bin/bash

# Build a test binary

gcc -o spurious_occupancy spurious_occupancy.c -static

# Run Sass-cache test

../sasscache/build/X86/gem5.opt ../sasscache/configs/example/se.py --cmd=xz --cpu-type=TimingSimpleCPU --num-cpus=1 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16


