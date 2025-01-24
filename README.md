This repository contains code for "Systematic Evaluation of Randomized Cache Designs against Cache Occupancy", to appear at USENIX Security 2025.

**Note**: The repository currently contains implementations of all cache designs considered in the paper as well as the in-house python simulator, and is self-sufficient for reproducibility of the results presented in the paper. For ease of use however, we are in the process of adding automated scripts to help with reproducibility.



## LLC simulator

In-house simulator to reproduce results of Section 5 related to covert channels. Each subdirectory within this directory corresponds to a specific randomized cache design. 
Our results can be reproduced by running `python3 main.py` in each subdirectory, followed by executing the `plot.py` script.


## Randomized Cache designs

We also open-source all cache designs evaluated in the paper

- **ceaser**: Implementation of CEASER (including rekeying, but restricting the number of skews to 1).

CEASER is implemented on top of MIRAGE by adding the relevant functionality to `SkewedAssocRand` in `src/mem/cache/tags/indexing_policies/skewed_assoc_randomized.hh`.
To build and run CEASER, navigate to `ceaser/` and follow the commands in README.md to build. A sample run of CEASER:

```
./build/X86/gem5.opt --outdir ./stats configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 
```

This runs the SPEC2017 benchmark xz on our CEASER implementation (note `--mirage_mode=ceaser`).

- **ceaser-s**: Implementation of CEASER-S (including rekeying, but with no restrictions on the number of skews).

CEASER-S is implemented on top of MIRAGE by adding the relevant functionality to `SkewedAssocRand` in `src/mem/cache/tags/indexing_policies/skewed_assoc_randomized.hh`.
To build and run CEASER-S, navigate to `ceaser-s/` and follow the commands in README.md to build. A sample run of CEASER-S:

```
./build/X86/gem5.opt --outdir ./stats configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=ceaser --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 
```

This runs the SPEC2017 benchmark xz on our CEASER-S implementation (note `--mirage_mode=ceaser` and `--l2_numSkews=2`). Other SPEC2017 benchmarks supported are listed in a subsequent section of the README.

- **mirage**: Borrowed from https://github.com/gururaj-s/mirage; has the implementation of MIRAGE, SCATTER, and baseline set-associative.

Navigate to `/mirage/` and follow the build and run instructions in README for MIRAGE, SCATTER-Cache, and Baseline. We do not make any structural modifications
to these cache designs. For completeness, the commands to run SPEC2017 benchmark xz on each of these designs (note the only difference is --mirage\_mode`).

```
./build/X86/gem5.opt --outdir ./stats configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=mirage --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 
```

```
./build/X86/gem5.opt --outdir ./stats configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 
```

```
./build/X86/gem5.opt --outdir ./stats configs/example/spec06_config_multiprogram.py --benchmark=xz --num-cpus=2 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=Baseline --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz --maxinsts=1000000000 
```

- **sasscache** Implementation of sass-cache (adapted from the implementation shared with us by the sass-cache authors, upon request)

Navigate to `/sasscache` and follow the sequence of steps:
1. `scons ./build/X86/gem5.opt` to build the sasscache implementation
2. `./build/X86/gem5.opt ../../configs/example/se.py --cpu-type=TimingSimpleCPU --num-cpus=2 --cmd=xz --maxinsts=1000000000 --mem-size=8GB --mem-type=DDR4_2400_8x8 --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16` to run the SPEC2017 xz benchmark on Sasscache

## Performance evaluation and fingerprinting

To reproduce our performance evaluation results, follow the commands above with two changes:

-- Benchmark: Change the `--benchmark` to the particular SPEC2017 benchmark being tried.

-- Replacement policy: Use the flag `--replacement_policy` to the replacement policy of choice. We have the following policies supported: `RandomRP`, `TreePLRURP`, `WeightedLRURP`, `RRIPRP`, and `FIFORP` as valid values for this flag.

**Note**: We do not provide the SPEC2017 source due to its licensing.

## AES 

In each of the cache design subdirectories, we have provided a reference AES-TBOX implementation under `AES\_TBOX` with a CMakeList to help build it. It can be integrated into
any of the cache designs by the `--benchmark` flag
