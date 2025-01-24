import seaborn as sns
import matplotlib.pyplot as plt

x_axis = ['ceaser', 'ceaser-s', 'mirage', 'scatter', 'sass']
y_axis = [81.9, 74.6, 86.1, 67.1, 13.5]


plt.figure(figsize=(10, 4))  
sns.barplot(x=x_axis, y=y_axis, palette='Set2') 

plt.xlabel('Cache Design', fontsize=14)
plt.ylabel('Fingerprinting Prediction Accuracy', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=12)


plt.tight_layout()
plt.savefig('accuracy.pdf', format='pdf')