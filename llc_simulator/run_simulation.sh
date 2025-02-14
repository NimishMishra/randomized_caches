#!/bin/bash

echo "Running Mirage Cache Occupancy..."
cd Mirage_cache_occupancy || exit
python3 main.py
cd ..

echo "Running Ceaser Cache Occupancy..."
cd Ceaser_cache_occupancy || exit
python3 main.py
cd ..

echo "Running ScatterCache Cache Occupancy..."
cd ScatterCache_cache_occupancy || exit
python3 main.py
cd ..

echo "Running Normal Cache Occupancy..."
cd Normal_cache_occupancy || exit
python3 main.py
cd ..

echo "Generating Covert Channel Plot..."
python3 covert_channel_plot.py

echo "All scripts executed successfully."

