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
y_values = np.array([
    [88.0418655, 86.73858122, 67.18931708, 87.22781409, 68.09560091],
    [100.0499856, 100.0023064, 109.7700849, 100.0023064, 123.2908317],
    [150, 67.03994524, 107.915832, 67.03994524, 150],
    [108.4047255, 101.4953977, 131.585948, 101.4953977, 187.2094091],
    [100.0368659, 100.0214337, 100.5684205, 100.0214337, 100.4216669],
    [100, 100, 100, 100, 101.5717555],
    [100.0494515, 99.94303051, 101.2733767, 99.94303051, 104.2196899],
    [100.1227075, 100.4428812, 102.8835228, 100.4428812, 67.52031186],
    [100.060881, 100.0143026, 101.5232905, 100.0143026, 107.4817614],
    [99.78709424, 99.9202323, 98.86861437, 99.9202323, 101.6909966],
    [100.7059921, 100.1389601, 105.40872, 100.1389601, 113.1816205],
    [100, 100, 100, 100, 99.29441017],
    [100, 100, 100, 100, 84.06965695],
    [100.2934168, 100.0651036, 107.2015076, 100.0607967, 111.6678508],
    [100.2909639, 100.0888439, 99.86935904, 100.0888439, 99.87147918],
    [98.18569114, 99.57644195, 83.9640099, 99.57644195, 104.4483847]
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
plt.savefig('fiforp.pdf', format='pdf')
#plt.show()
