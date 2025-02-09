# SPEC 2017 Perf Runs

## Pre-requisites

1. Point `BASE_DIR` to the top-level directory of the repository

2. Activate the created venv through `. ${BASE_DIR}/randomized_cache_hello_world/venv27/bin/activate`

3. Point `SPEC_PATH` to the SPEC2017 installation. We do not provide SPEC2017 sources due to licensing issues.

## Run Benchmark

Use one of the run-scripts to engage a specific benchmark with the respective cache design.

Ex: `bash run_mirage_benchmark.sh blender` to run blender on MIRAGE.

List of supported benchmarks: `blender`, `cactu`, `fotonik`, `gcc`, `imagick`, `lbm`, `leela`, `mcf`, `nab`, `namd`, `omnetpp`, `perlbench`, `povray`, `wrf`, `x264`, `xalancbmk`, `xz`

Additionally, the second (optional) argument to these scripts helps specify a replacement policy. List of supported policies: `RandomRP`, `TreePLRURP`, `WeightedLRURP`, `RRIPRP`, `FIFORP`.

Ex: `bash run_scatter_benchmark.sh blender TreePLRURP` to run blender on Scatter-cache with `TreePLRURP` policy.
