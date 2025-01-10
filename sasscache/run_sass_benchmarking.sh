#!/bin/bash

cd ./sass/perlbench/
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=perlbench --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16  &
cd ../../


cd  ./sass/gcc
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=gcc --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../


cd ./sass/mcf
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=mcf --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../



cd ./sass/namd
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=namd --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../


cd ./sass/povray
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=povray --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/lbm
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=lbm --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/omnetpp
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=omnetpp --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/xalancbmk
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=xalancbmk --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/cactu
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=cactu --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/x264
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=x264 --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../


cd ./sass/blender
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=blender --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../


cd ./sass/imagick
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=imagick --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../


cd ./sass/leela
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=leela --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/nab
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=nab --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/fotonik
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=fotonik --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../

cd ./sass/xz
../../build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=xz --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 &
cd ../../



































