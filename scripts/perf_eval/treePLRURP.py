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
categories = ['ceaser', 'ceaser_s', 'mirage', 'scatter']

y_values = np.array([
    [100.3331075, 137.1556007, 94.59688347, 137.3814363],
    [100.5676199, 107.0924648, 109.7651841, 107.0924648],
    [150, 139.7137677, 52.63646151, 139.7137677],
    [105.3075481, 120.2965557, 127.2932152, 120.2965557],
    [100.0085891, 100.6476217, 100.7524093, 100.6476217],
    [100, 120.7598372, 100, 120.7598372],
    [100.2330689, 102.7571881, 103.1266959, 102.7292879],
    [99.14129796, 99.72858491, 99.23210117, 99.72858491],
    [100.0674884, 101.1579394, 101.5619836, 101.1579394],
    [99.80665585, 99.4502573, 98.95804868, 99.4502573],
    [100.4082139, 118.1364274, 107.7994602, 118.1364274],
    [100, 100, 100, 100],
    [100, 100, 100, 100.166113],
    [100.2557328, 108.9581034, 114.8126039, 108.9581034],
    [100.2298381, 100.5448427, 99.93736279, 100.5448427],
    [97.9110607, 94.96684026, 84.5271115, 94.96684026]
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
    mpatches.Patch(hatch='-', color=palette[3], label='scatter')
]

# Update the legend with hatch patterns and matching colors
plt.legend(handles=hatch_legend, bbox_to_anchor=(0.5, 1.15), ncol=5, fontsize=12)

# Show the plot
plt.savefig('treePLRURP.pdf', format='pdf')