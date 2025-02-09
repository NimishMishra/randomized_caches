# Randomized Cache Test Run

This run is intended to be a test run of the randomized cache designs in this repo. This involves setup and test run for a sample program.

Run through `bash setup.sh`. We have tested the following on Ubuntu. Please use an appropriate package manager (like yum) for your system (say Redhat). This scripts does the following:

Pre-requisite: `export BASE_DIR=...`. Point this to the top-level directory of this repository. 

1. Setup python2.7

2. Setup virtualenv

3. Install dependencies: `scons` and `six`

4. Build gem5 binaries for `MIRAGE`, `Scatter-cache` and `Baseline cache`. The build is performed with a single thread. Change parameter `THREADS` in the script to engage multiple cores. Building parallely on multiple cores risks exhausting the RAM, and thus should be carefully set.

5. Build gem5 binaries for CEASER

6. Build gem5 binaries for CEASER-S

7. Build gem5 binaries for Sasscache.  

This setup needs to be done only once for all experiments in this repository.
