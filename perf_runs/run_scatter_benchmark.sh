#!/bin/bash

gcc -o ../randomized_cache_hello_world/spurious_occupancy ../randomized_cache_hello_world/spurious_occupancy.c -static

# Run Scatter-cache SPEC2017 benchmark

../mirage/perf_analysis/gem5/build/X86/gem5.opt --outdir ./stats/ ../mirage/perf_analysis/gem5/configs/example/spec06_config_multiprogram.py --maxinsts=1000000000 --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --benchmark=$1  --replacement-policy=$2
