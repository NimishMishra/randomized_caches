#!/bin/bash

THREADS=1

# Install virtualenv
sudo apt install virtualenv

# Setup python2.7
sudo apt install python2.7 python2.7-dev

# Setup virtualenv
virtualenv -p python2.7 venv27
. venv27/bin/activate

# Install scons

wget https://sourceforge.net/projects/scons/files/scons/3.1.2/scons-3.1.2.tar.gz

tar -xvf scons-3.1.2.tar.gz

rm scons-3.1.2.tar.gz

cd scons-3.1.2

python setup.py install

cd ..

# Install six

pip install six


# Build binaries for MIRAGE, Scatter-Cache, and Baseline cache

cd ../mirage/perf_analysis/gem5

scons -j$THREADS ./build/X86/gem5.opt

cd ../../../randomized_cache_hello_world/

# Build binary for CEASER

cd ../ceaser/perf_analysis/gem5/

scons -j$THREADS ./build/X86/gem5.opt

cd ../../../randomized_cache_hello_world/

# Build binary for CEASER-S

cd ../ceaser-s/perf_analysis/gem5/

scons -j$THREADS ./build/X86/gem5.opt

cd ../../../randomized_cache_hello_world/

# Build binary for sasscache

cd ../sasscache/

scons -j$THREADS ./build/X86/gem5.opt

cd ../randomized_cache_hello_world/

# Build a test binary

gcc -o spurious_occupancy spurious_occupancy.c -static

# Run MIRAGE test

../mirage/perf_analysis/gem5/build/X86/gem5.opt --outdir ./stats/ ../mirage/perf_analysis/gem5/configs/example/spec06_config_multiprogram.py --num-cpus=1 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=skew-vway-rand --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz

# Run Scatter-cache test

../mirage/perf_analysis/gem5/build/X86/gem5.opt --outdir ./stats/ ../mirage/perf_analysis/gem5/configs/example/spec06_config_multiprogram.py --num-cpus=1 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz



rm spurious_occupancy
