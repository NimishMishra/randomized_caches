import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as mpatches

# X-axis labels
x_labels = [
    'omnetpp', 'lbm', 'mcf', 'perlbench', 'namd', 'povray', 'gcc', 'imagick', 
    'xz', 'cactu', 'xalancbmk', 'nab', 'fotonik', 'x264', 'blender', 'leela'
]

# Categories
categories = ['ceaser', 'ceaser_s', 'mirage', 'scatter', 'sass']


#Baseline

# rrip
y_values = np.array([
    [100.1596169, 99.8669859, 111.4325619, 99.88028731, 112.9356212],
    [100.8311869, 100.9006587, 109.7606029, 100.9006587, 125.0446475],
    [150, 96.31615625, 69.67100821, 96.31615625, 150],
    [107.8869926, 108.4046957, 134.244282, 108.4046957, 190.2296198],
    [100.0034366, 100.0111689, 100.7792431, 100.0111689, 100.2763821],
    [100, 100, 100, 100, 99.9402991],
    [100.2156491, 100.3713197, 103.5846961, 100.3713197, 103.4609144],
    [99.90602531, 100.5097946, 102.9234277, 100.5097946, 69.20529883],
    [100.0154531, 100.0417995, 101.5981325, 100.0417995, 106.8160458],
    [99.84304507, 99.61128294, 99.16062518, 99.61128294, 101.8428285],
    [100.1084676, 100.0420491, 108.0132264, 100.0420491, 100.0087064],
    [100, 100, 100, 100, 99.29441017],
    [100, 100, 100, 100, 84.06965695],
    [100.2581694, 100.3671122, 114.822827, 100.3671122, 138.8602315],
    [100.1694559, 100.1597438, 100.0757746, 100.1597438, 100.0778991],
    [98.25061025, 94.19388585, 84.76362066, 94.19388585, 102.1378778]
])

# Create a DataFrame
data = pd.DataFrame(y_values, columns=categories)
data['x'] = x_labels

# Reshape the DataFrame to long format for Seaborn
data_long = pd.melt(data, id_vars=['x'], var_name='category', value_name='value')

# Set the style of the plot
sns.set(style="whitegrid")

# Create the plot
plt.figure(figsize=(14, 3))

# Create the column chart with customized design (using 'hue' for color)
barplot = sns.barplot(x='x', y='value', hue='category', data=data_long, palette='Set2')

# Add hatch patterns to each bar to make them visually distinct
for i, bar in enumerate(barplot.patches):
    # Add alternating hatch patterns for better identification
    if i < 16:
        bar.set_hatch('/')
    elif i >= 16 and i < 32:
        bar.set_hatch('x')
    elif i >= 32 and i < 48:
        bar.set_hatch('\\')
    elif i >= 48 and i < 64:
        bar.set_hatch('-')
    else:
        bar.set_hatch('o')
    
    # Optional: add black edge color for each bar
    bar.set_edgecolor('black')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=14)

# Set the y-axis label and title
plt.ylabel('LLC miss ratio in %', fontsize=14)
plt.xlabel('SPEC 2017 benchmark', fontsize=14)

# Increase the font size of the axes ticks
plt.tick_params(axis='both', which='major', labelsize=14)

# Add a grid to make the plot easier to read
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)

# Improve the layout to avoid overlap
plt.tight_layout()

# Create a color palette (same as used in Seaborn barplot)
palette = sns.color_palette('Set2', n_colors=len(categories))

# Create legend handles with hatch patterns and matching colors
hatch_legend = [
    mpatches.Patch(hatch='/', color=palette[0], label='ceaser'),
    mpatches.Patch(hatch='x', color=palette[1], label='ceaser_s'),
    mpatches.Patch(hatch='\\', color=palette[2], label='mirage'),
    mpatches.Patch(hatch='-', color=palette[3], label='scatter'),
    mpatches.Patch(hatch='o', color=palette[4], label='sass')
]

# Update the legend with hatch patterns and matching colors
plt.legend(handles=hatch_legend, bbox_to_anchor=(0.5, 1.15), ncol=5, fontsize=12)

# Show the plot
plt.savefig('rriprp.pdf', format='pdf')
#plt.show()
