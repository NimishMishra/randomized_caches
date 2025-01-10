#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:15:21 2023

@author: anirban
"""
from ast import literal_eval
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

with open("outfile_v100.txt", "r") as f:
    file = f.readlines()
    
iterations = 100
num_of_victim_access = 16

timing = list(filter(None, list(map(lambda each:each.strip("\n"), file))))
    
miss_count = [[0 for j in range(iterations)] for i in range(num_of_victim_access)]
num_access = [[0 for j in range(iterations)] for i in range(num_of_victim_access)]
tup = []

for line in timing:
    tup.append(literal_eval(line))


for i in range(num_of_victim_access):
    for j in range(iterations):
        miss_count[i][j] = tup[i*iterations + j][1]
        
for i in range(num_of_victim_access):
    for j in range(iterations):
        num_access[i][j] = tup[i*iterations + j][0]


bar_width = 7

# Set the x positions of the bars
x_positions = np.arange(len(miss_count[0]))

# Create a figure and axis object
fig, ax = plt.subplots()


#for i, set_data in enumerate(miss_count):
    # if (i % 2 == 0):
    #     x_values = list(range(len(set_data)))
    #     ax.plot(x_values, set_data)
# Loop through each set of values and create a bar plot
for i, set_data in enumerate(miss_count):
    print(set_data)
    if (i % 2 == 0):
        set_data = miss_count[i]
        mu = np.mean(set_data)
        sd = np.std(set_data)
        x = np.linspace(mu - 3*sd, mu + 3*sd, 100)
        ax.plot(x, norm.pdf(x, mu, sd), label=num_access[i][0])
#         # Create the bar plot
#    ax.hist(np.mean(set_data), width=bar_width, label=f'Set {i+1}')

# # Add labels, title, and legend
ax.set_xlabel('No of misses observed by attacker')
#ax.set_ylabel('probability distribution function')
# ax.set_title('Bar Plots with Multiple Sets of Data')
# ax.set_xticks(x_positions + bar_width * (len(miss_count) - 1) / 2)
# ax.set_xticklabels(['A', 'B', 'C', 'D'])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fancybox=True, shadow=True)






# Show the plot
plt.show()