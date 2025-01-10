This repository contains code for "Systematic Evaluation of Randomized Cache Designs against Cache Occupancy", submitted to USENIX Security 2025.

**Note**: The repository currently contains implementations of all cache designs considered in the paper as well as the in-house python simulator, and is self-sufficient for reproducibility of the results presented in the paper. For ease of use however, we are in the process of adding automated scripts to help with reproducibility.

**Directory Structure**:

1. **llc_simulator**: In-house simulator to reproduce results of Section 5.
2. **ceaser**: Implementation of CEASER (including rekeying, but restricting the number of skews to 1).
3. **ceaser-s**: Implementation of CEASER-S (including rekeying, but with no restrictions on the number of skews).
4. **mirage**: Borrowed from https://github.com/gururaj-s/mirage; has the implementation of MIRAGE, SCATTER, and baseline set-associative.
5. **sasscache** Implementation of sass-cache (adapted from the implementation shared with us by the sass-cache authors, upon request)
