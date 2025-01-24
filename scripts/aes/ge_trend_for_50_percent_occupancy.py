import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
x = [100, 1100, 2100, 3100, 4100, 5100, 6100, 7100, 8100, 9100, 10100, 11100, 12100, 13100, 14100, 15100, 16100, 17100, 18100, 19100]

scatter = [102.05, 105.10, 105.88, 96.86, 93.56, 93.56, 93.56, 93.56, 93.56, 93.56, 91.56, 90.56, 90.56, 90.56, 90.56, 90.56, 90.56, 90.56, 90.56, 90.56]
mirage = [101.10, 45.47, 44.64, 42.08, 38.03, 38.03, 38.03, 38.01, 36.79, 36.01, 36.01, 35.59, 35.59, 35.59, 33.13, 33.13, 33.13, 31.21, 30.05, 30.05]
ceaser = [108.05, 107.61, 81.73, 100.80, 102.50, 101.10, 102.60, 100.42, 100.54, 100.54, 
                101.54, 101.23, 100.15, 100.94, 101.24, 100.14, 99.84, 100.43, 99.14, 100.97]

sass = [100.16, 94.24, 99.57, 101.10, 107.56, 109.31, 109.14, 108.15, 107.18, 109.72, 108.15, 109.15, 107.25, 109.15, 108.82, 107.18, 107.14, 108.42,
            108.26, 109.31]

scatter = np.array(scatter)
mirage = np.array(mirage)
ceaser = np.array(ceaser)
sass = np.array(sass)


data_scatter = pd.DataFrame({'x': x, 'y': scatter})
data_mirage = pd.DataFrame({'x': x, 'y': mirage})
data_ceaser = pd.DataFrame({'x': x, 'y': ceaser})
data_sass = pd.DataFrame({'x': x, 'y': sass})

plt.figure(figsize=(10, 6))
sns.lineplot(x='x', y='y', data=data_scatter,   label='ceaser-s', marker='o')
sns.lineplot(x='x', y='y', data=data_mirage,   label='mirage', marker='s')
sns.lineplot(x='x', y='y', data=data_ceaser, label='scatter', marker='^')
sns.lineplot(x='x', y='y', data=data_sass, label='sass', marker='*')

plt.xlabel('Number of Observations', fontsize=18)
plt.ylabel('Guessing Entropy', fontsize=18)

plt.xticks(fontsize=18, rotation=20)  # Change x-axis tick font size
plt.yticks(fontsize=18)  # Change y-axis tick font size
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend(fontsize=16)
plt.savefig('fifty_occupancy2.pdf', dpi=1200, format='pdf', bbox_inches='tight'  )
