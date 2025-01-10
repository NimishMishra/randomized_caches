from ast import literal_eval
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
from matplotlib.lines import Line2D



# Initialize separate lists for each file
file_list_1k, file_list_2k, file_list_3k, file_list_4k, file_list_5k = [], [], [], [], []
file_list_6k, file_list_7k, file_list_8k, file_list_9k, file_list_10k = [], [], [], [], []
file_list_11k, file_list_12k, file_list_13k, file_list_14k, file_list_15k = [], [], [], [], []

# List of all variable names for easier assignment
file_lists = [
    file_list_1k, file_list_2k, file_list_3k, file_list_4k, file_list_5k,
    file_list_6k, file_list_7k, file_list_8k, file_list_9k, file_list_10k,
    file_list_11k, file_list_12k, file_list_13k, file_list_14k, file_list_15k
]

# Read files and assign their content to the respective list
for i in range(1, 16):  # 1 to 15 inclusive
    filename = f"outfile_v10_{i}k.txt"
    try:
        with open(filename, 'r') as file:
            file_lists[i - 1].extend(file.readlines())  # Append lines to the respective list
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# Output the result (optional)
print("Contents stored in individual lists.")



file_list_1k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_1k))))))
file_list_2k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_2k))))))
file_list_3k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_3k))))))
file_list_4k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_4k))))))
file_list_5k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_5k))))))
file_list_6k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_6k))))))
file_list_7k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_7k))))))
file_list_8k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_8k))))))
file_list_9k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_9k))))))
file_list_10k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_10k))))))
file_list_11k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_11k))))))
file_list_12k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_12k))))))
file_list_13k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_13k))))))
file_list_14k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_14k))))))
file_list_15k = list(map(literal_eval, list(filter(None, list(map(lambda each:each.strip("\n"), file_list_15k))))))




sender_accesses = []; num_of_misses = []
for item in file_list_5k:
    sender_accesses.append(item[0])
    num_of_misses.append(item[1])
    
grouped_data = defaultdict(list)
for access, miss in zip(sender_accesses, num_of_misses):
    grouped_data[access].append(miss)

# Prepare data for the box plot
unique_accesses = sorted(grouped_data.keys())
grouped_misses = [grouped_data[access] for access in unique_accesses]


# Calculate standard deviations and means for annotations
std_devs = [np.std(data) for data in grouped_misses]
means = [np.mean(data) for data in grouped_misses]

# Create the box plot
plt.figure(figsize=(10, 6))
box = plt.boxplot(grouped_misses, tick_labels=unique_accesses, showmeans=False, showfliers=True,
                  flierprops=dict(marker='x', color='red', markersize=5, markerfacecolor='red', markeredgewidth=1))

# Annotate the standard deviation and mean with adjusted positioning
for i, (std, mean) in enumerate(zip(std_devs, means)):
    # Calculate appropriate spacing from the box (to avoid overlap)
    y_top = max(grouped_misses[i])
    y_bottom = min(grouped_misses[i])
    box_height = y_top - y_bottom
    offset = box_height * 0.2  # 10% of box height as offset

    # Annotate standard deviation above the box (top of the box)
    plt.text(i + 1, y_top + offset, f"σ = {std:.2f}", ha='center', fontsize=10, color='blue')
    
    # Annotate mean below the box (bottom of the box)
    plt.text(i + 1, y_bottom - offset, f"$\mu$ = {mean:.2f}", ha='center', fontsize=10, color='green')
    
# Create proxy artist for the outliers (red 'x' markers)
plt.scatter([], [], color='black', marker='x', s=20, label='Outlier')
# Add legend for outliers
plt.legend(loc='upper left')

# Customize the plot
plt.title("Receiver making 5,000 accesses", fontsize=10)
plt.xlabel("No. of accesses from sender", fontsize=10)
plt.ylabel("No. of misses observed by receiver", fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

# Save the plot as a PDF with high DPI
plt.savefig("mirage_5k_access.pdf", dpi=1200, format='pdf')

# Display the plot
plt.show()