#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 01:09:40 2025

@author: localadmin
"""
import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval
from collections import defaultdict



def read_file_to_list(file_name, array_name):
    with open(file_name, "r") as file:
        for line in file:
            array_name.append(line)
    
def group_data(dataset):
    sender_accesses = []; num_of_misses = []
    for item in dataset:
        sender_accesses.append(item[0])
        num_of_misses.append(item[1])
        
    grouped_data = defaultdict(list)
    for access, miss in zip(sender_accesses, num_of_misses):
        grouped_data[access].append(miss)
    
    return grouped_data
    
def plotting(dataset_0, dataset_1, ax, label, marker, color_0, color_1):
    y_values_0 = [np.mean(values) for values in dataset_0.values()]
    y_values_1 = [np.mean(values) for values in dataset_1.values()]
    max_values_0 = [np.max(values) for values in dataset_0.values()]
    min_values_0 = [np.min(values) for values in dataset_0.values()]
    max_values_1 = [np.max(values) for values in dataset_1.values()]
    min_values_1 = [np.min(values) for values in dataset_1.values()]
    
    ax.plot(x_labels, y_values_0, label=label+str(label_val[0]), marker=marker, alpha=0.8)
    ax.plot(x_labels, y_values_1, label=label+str(label_val[1]), marker=marker, alpha=0.8)

    ax.fill_between(
        x_labels,
        min_values_0,
        max_values_0,
        color=color_0,
        alpha=0.2
    )

    ax.fill_between(
        x_labels,
        min_values_1,
        max_values_1,
        color=color_1,
        alpha=0.2
    )

    

file_mirage_0 = "Mirage_cache_occupancy/outfile_v10_for_0.txt"
file_mirage_1 = "Mirage_cache_occupancy/outfile_v10_for_1.txt"
file_scatter_0 = "ScatterCache_cache_occupancy/outfile_v10_for_0.txt"
file_scatter_1 = "ScatterCache_cache_occupancy/outfile_v10_for_1.txt"
file_ceaser_0 = "Ceaser_cache_occupancy/outfile_v10_for_0.txt"
file_ceaser_1 = "Ceaser_cache_occupancy/outfile_v10_for_1.txt"
file_baseline_0 = "Normal_cache_occupancy/outfile_v10_for_0.txt"
file_baseline_1 = "Normal_cache_occupancy/outfile_v10_for_1.txt"


# Initialize an empty list to store the data
mirage_0 = []; mirage_1 = []; scatter_0 = []; scatter_1 = []
ceaser_0 = []; ceaser_1 = []; baseline_0 = []; baseline_1 = []

read_file_to_list(file_mirage_0, mirage_0)
read_file_to_list(file_mirage_1, mirage_1)
read_file_to_list(file_scatter_0, scatter_0)
read_file_to_list(file_scatter_1, scatter_1)
read_file_to_list(file_ceaser_0, ceaser_0)
read_file_to_list(file_ceaser_1, ceaser_1)
read_file_to_list(file_baseline_0, baseline_0)
read_file_to_list(file_baseline_1, baseline_1)


mirage_0 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), mirage_0))))))
mirage_1 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), mirage_1))))))
scatter_0 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), scatter_0))))))
scatter_1 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), scatter_1))))))
ceaser_0 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), ceaser_0))))))
ceaser_1 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), ceaser_1))))))
baseline_0 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), baseline_0))))))
baseline_1 = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), baseline_1))))))


mirage_grouped_0 = group_data(mirage_0)
mirage_grouped_1 = group_data(mirage_1)
scatter_grouped_0 = group_data(scatter_0)
scatter_grouped_1 = group_data(scatter_1)
ceaser_grouped_0 = group_data(ceaser_0)
ceaser_grouped_1 = group_data(ceaser_1)
baseline_grouped_0 = group_data(baseline_0)
baseline_grouped_1 = group_data(baseline_1)


x_labels = ['1000', '2000', '3000', '5000','10000','15000','20000','25000','30000', '35000', '40000']

fig = plt.figure(figsize=(14,6))
ax1 = fig.add_subplot(111)

label_val = ["'0'","'1'"]



plotting(mirage_grouped_0, mirage_grouped_1, ax1, 'mirage ', '.', 'blue', 'orange')
plotting(scatter_grouped_0, scatter_grouped_1, ax1, 'scatter ', '*', 'green', 'red')
plotting(ceaser_grouped_0, ceaser_grouped_1, ax1, 'ceaser ', 's', 'black', 'grey')
plotting(baseline_grouped_0, baseline_grouped_1, ax1, 'baseline ', '^', 'yellow', 'pink')


# Set labels and title
ax1.set_xlabel('No. of accesses from receiver')
ax1.set_ylabel('No. of cache misses observed by receiver')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
plt.xticks(x_labels, rotation=20)

ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()
plt.tight_layout()
plt.savefig('cache_occupancy_comparison.png', dpi=1200, bbox_inches='tight')  
plt.show()


