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


# WeightedLRU
y_values = np.array([
    [101.3572047, 100.3811724, 96.76580999, 100.6237366],
    [100.031835, 100.0020563, 109.7684942, 100.0020563],
    [150, 43.14770243, 57.90160355, 43.14770243],
    [108.1756867, 100.8392215, 134.2019871, 100.8392215],
    [100.0068713, 100.0077302, 100.7524093, 100.0077302],
    [100, 100, 100, 100],
    [100.2850623, 100.1132393, 103.5358659, 100.1134101],
    [100.1206803, 100.4416691, 102.9134485, 100.4416691],
    [100.0435713, 100.0110195, 101.594658, 100.0110195],
    [99.81571759, 99.92798253, 98.95389483, 99.92798253],
    [100.2090782, 100.1011977, 107.9039195, 100.1011977],
    [100, 100, 100, 100],
    [100, 100, 100, 100],
    [100.0019309, 100, 114.8141434, 100],
    [100.2324413, 100.0911574, 99.97069218, 100.0911574],
    [98.15713221, 99.61669012, 84.51941386, 99.61669012]
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

plt.savefig('weighted_LRURP.pdf', format='pdf')
#plt.show()
