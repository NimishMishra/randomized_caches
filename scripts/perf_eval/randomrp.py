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
    [101.9712122, 98.16174345, 96.85530956, 98.16174345, 98.16174345],
    [99.84311929, 99.81394542, 99.57131585, 99.81394542, 114.8172839],
    [150, 124.3489245, 102.8456892, 124.3489245, 125.5103097],
    [102.7389825, 102.3278168, 101.3896554, 102.3278168, 150.3364589],
    [100.1851836, 100.1561687, 100.1032591, 100.1561687, 101.443223],
    [100, 100, 100, 100, 100.4705224],
    [100.1563604, 100.1279613, 100.0884997, 100.1279613, 104.9933427],
    [100.4984511, 100.5219468, 100.6129043, 100.5219468, 69.17069838],
    [99.85101712, 99.83533471, 99.83234758, 99.83533471, 108.2261506],
    [100.0346044, 99.99292939, 100.0093997, 99.99292939, 102.8195047],
    [100.7071313, 100.5103605, 100.4059786, 100.5103605, 117.3272623],
    [100, 100, 100, 100, 99.29441017],
    [100, 100, 100, 100, 84.06965695],
    [101.9808793, 101.9403699, 101.6592257, 101.9403699, 126.9115516],
    [100.0178988, 100.0339774, 100.0318538, 100.0339774, 100.0339774],
    [100.7997103, 100.0734128, 99.93050254, 100.0734128, 123.3822554]
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
plt.savefig('random_rp.pdf', format='pdf')
