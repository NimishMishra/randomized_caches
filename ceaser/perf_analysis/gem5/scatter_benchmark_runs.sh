#!/bin/bash

# Perlbench 500
./build/X86/gem5.opt --outdir ./scatter_perf_runs/perlbench configs/example/spec06_config_multiprogram.py --benchmark=perlbench --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &


# gcc 502
./build/X86/gem5.opt --outdir ./scatter_perf_runs/gcc configs/example/spec06_config_multiprogram.py --benchmark=gcc --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# mcf 505
./build/X86/gem5.opt --outdir ./scatter_perf_runs/mcf configs/example/spec06_config_multiprogram.py --benchmark=mcf --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# namd 508
./build/X86/gem5.opt --outdir ./scatter_perf_runs/namd configs/example/spec06_config_multiprogram.py --benchmark=namd --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 511 povray
./build/X86/gem5.opt --outdir ./scatter_perf_runs/povray configs/example/spec06_config_multiprogram.py --benchmark=povray --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 519 lbm
./build/X86/gem5.opt --outdir ./scatter_perf_runs/lbm configs/example/spec06_config_multiprogram.py --benchmark=lbm --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 520 omnetpp
./build/X86/gem5.opt --outdir ./scatter_perf_runs/omnetpp configs/example/spec06_config_multiprogram.py --benchmark=omnetpp --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 521 wrf = DOES NOT WORK
#taskset -c 7 ./build/X86/gem5.opt --outdir ./scatter_perf_runs/wrf configs/example/spec06_config_multiprogram.py --benchmark=wrf --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 523 xalancbmk
./build/X86/gem5.opt --outdir ./scatter_perf_runs/xalancbmk configs/example/spec06_config_multiprogram.py --benchmark=xalancbmk --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 531 deepsjeng
#taskset -c 8 ./build/X86/gem5.opt --outdir ./scatter_perf_runs/deepsjeng configs/example/spec06_config_multiprogram.py --benchmark=deepsjeng --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 507 cactuBSSN
./build/X86/gem5.opt --outdir ./scatter_perf_runs/cactu configs/example/spec06_config_multiprogram.py --benchmark=cactu --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 525 x264
./build/X86/gem5.opt --outdir ./scatter_perf_runs/x264 configs/example/spec06_config_multiprogram.py --benchmark=x264 --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 526 blender
./build/X86/gem5.opt --outdir ./scatter_perf_runs/blender configs/example/spec06_config_multiprogram.py --benchmark=blender --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 538 imagick
./build/X86/gem5.opt --outdir ./scatter_perf_runs/imagick configs/example/spec06_config_multiprogram.py --benchmark=imagick --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 541 leela
./build/X86/gem5.opt --outdir ./scatter_perf_runs/leela configs/example/spec06_config_multiprogram.py --benchmark=leela --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 544 nab
./build/X86/gem5.opt --outdir ./scatter_perf_runs/nab configs/example/spec06_config_multiprogram.py --benchmark=nab --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 549 fotonik
./build/X86/gem5.opt --outdir ./scatter_perf_runs/fotonik configs/example/spec06_config_multiprogram.py --benchmark=fotonik --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &

# 557 xz
./build/X86/gem5.opt --outdir ./scatter_perf_runs/xz configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 &
