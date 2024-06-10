import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Define the directory where the files are located
data_directory = os.path.join(os.path.dirname(__file__), '../data/')

# Use glob to get all CSV files starting with A or D and sort them
csv_files = sorted(glob.glob(os.path.join(data_directory, '[AD]*.csv')), key=lambda x: os.path.basename(x))

# Order the files as A2, A1, A0, D0, D1, ..., D7
ordered_files = sorted([f for f in csv_files if 'A' in os.path.basename(f)], reverse=True) + \
                sorted([f for f in csv_files if 'D' in os.path.basename(f)], key=lambda x: int(x.split('D')[1].split('.')[0]))

# Check if any files were found
if not ordered_files:
    raise ValueError(f"No CSV files found in directory: {data_directory}")

# Create a figure
plt.figure(figsize=(15, 10))

# Define a list of colors with enough distinct colors for all signals
color_list = [
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'
]

# Plot each file with an offset
for i, file in enumerate(ordered_files):
    data = pd.read_csv(file)
    time = data.iloc[:, 0]  # Assuming first column is time
    signal = data.iloc[:, 1]  # Assuming second column is the signal
    offset = len(ordered_files) - 1 - i  # Define offset to invert the order
    plt.plot(time, signal + offset * 1.2, color=color_list[i % len(color_list)])
    plt.text(time.iloc[-1], offset * 1.2, os.path.basename(file).split('.')[0], 
             verticalalignment='center', fontsize=16, color=color_list[i % len(color_list)])

# Adding labels, title, and grid
plt.xlabel('Time (100ns simulation)')
plt.yticks([])  # Remove y-axis labels
plt.title('Simulation of Decoder')

plt.grid(True, linestyle='--')

# Show the plot
plt.show()
