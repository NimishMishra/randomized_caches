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
