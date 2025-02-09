# Randomized Cache Test Run

This run is intended to be a test run of the randomized cache designs in this repo. This involves setup and test run for a sample program.

## (One-time) Setup

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

## Run

Pre-requisites:

1. Point `BASE_DIR` to the top-level directory of the repository

2. Activate the created venv through `. ${BASE_DIR}/randomized_cache_hello_world/venv27/bin/activate`


Invoke `bash run_mirage.sh` to execute a test program in MIRAGE. Alternatively, use `run_scatter.sh` for Scatter-cache, `run_ceaser.sh` for CEASER, and `run_ceaser_s.sh` for CEASER-S.

**Expected Outcome**: At the end of simulation, gem5 shall output a message and exit the thread context, as such:

```
Spurious Occupancy step finished.
Exiting @ tick 67659457149 because exiting with last active thread context
```

This implies the simulations are running as expected.
