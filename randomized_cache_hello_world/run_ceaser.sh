#!/bin/bash

# Build a test binary

gcc -o spurious_occupancy spurious_occupancy.c -static

# Run CEASER test

../ceaser/perf_analysis/gem5/build/X86/gem5.opt --outdir ./stats/ ../ceaser/perf_analysis/gem5/configs/example/spec06_config_multiprogram.py --num-cpus=1 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz


