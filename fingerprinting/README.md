# Process Fingerprinting

## Pre-requisites

1. Point `$BASE_DIR` to the top-level directory of the repository

2. Activate the created vend through `. ${BASE_DIR}/randomized_cache_hello_world/venv27/bin/activate`

3. Point `SPEC_PATH` to the SPEC2017 installation. We do not provide SPEC2017 sources due to licensing issues.

## Data Collection

1. Replace the spurious occupancy code in `${BASE_DIR}/randomized_cache_hello_world` with the code given in this directory. That is: `cp fingerprint.c ../randomized_cache_hello_world/spurious_occupancy.c`
2. For 500 runs of a cache design (say CEASER), execute `bash ${BASE_DIR}/randomized_cache_hello_world/run_ceaser.sh ${benchmark_name}` where `benchmark_name` represents the chosen benchmark. Once the run ends, execute `grep "system.l2.overall_misses::.cpu0.data" stats.txt` and append the result to `ceaser.log`.

3. Execute `./data/ceaser.py` to mount the attack

## Execute on prerun results

We have open-sourced our runs for the data collection phase mentioned above. The log files `ceaser.log`, `ceaser_s.log`, `mirage.log`, `sass.log`, and `scatter.log` constitute the benchmark runs against each of these randomized cache designs. 

The scripts `ceaser.py`, `ceaser_s.py`, `mirage.py`, `sass.py`, and `scatter.py` help in the fingerprinting: for each entry in the corresponding log file, the script will compare it with a pre-created template, and then emits its guess of the benchmark. Accuracy is reported as the number of correct guesses made.

Current script output:

`python3 ceaser.py`: (CEASER) Accuracy: 0.8196392785571143

`python3 ceaser_s.py`: (CEASER-S) Accuracy: 0.746

`python3 mirage.py`: (MIRAGE) Accuracy: 0.8617234468937875

`python3 scatter.py` : (Scatter-cache) Accuracy: 0.6713426853707415

`python3 sass.py`: (Sass-cache) Accuracy: 0.1342685370741483
