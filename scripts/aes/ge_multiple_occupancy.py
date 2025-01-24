import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x_labels = [40, 50, 70]
category_1 = [102.41, 90.56, 86.14]  
category_2 = [97.41, 30.05, 28.12]  
category_3 = [108.31, 108.42, 106.32]

data = pd.DataFrame({
    'x': [40, 50, 70, 40, 50, 70, 40, 50, 70],
    'category': ['scatter', 'scatter', 'scatter',
                 'mirage', 'mirage', 'mirage',
                 'sass-cache', 'sass-cache', 'sass-cache'],
    'value': category_1 + category_2 + category_3
})

plt.figure(figsize=(8, 6))
sns.barplot(x='x', y='value', hue='category', data=data)

plt.xlabel('Rates of LLC Occupancy', fontsize=14)
plt.ylabel('GE', fontsize=14)

plt.legend(title='Category', fontsize=14)
plt.savefig('different_occupancy.pdf', format='pdf')
