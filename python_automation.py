import pandas as pd
import matplotlib.pyplot as plt
import os

# Use the script's directory as base
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load CSV file
csv_path = os.path.join(base_dir, 'air_spring_output.csv')
df = pd.read_csv(csv_path)

# Extract signals
time = df['time']
displacement = df['displacement']
velocity = df['velocity']
force = df['force']

# Create folder for plots
plots_dir = os.path.join(base_dir, 'plots')
os.makedirs(plots_dir, exist_ok=True)

# Create 3 subplots stacked vertically
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Displacement
axs[0].plot(time, displacement, color='blue')
axs[0].set_ylabel('Displacement [m]')
axs[0].grid(True)
axs[0].set_title('Air Spring Simulation Signals')

# Velocity
axs[1].plot(time, velocity, color='green')
axs[1].set_ylabel('Velocity [m/s]')
axs[1].grid(True)

# Force
axs[2].plot(time, force, color='red')
axs[2].set_ylabel('Force [N]')
axs[2].set_xlabel('Time [s]')
axs[2].grid(True)

plt.tight_layout()

# Save the figure
plot_file = os.path.join(plots_dir, 'air_spring_subplots.png')
plt.savefig(plot_file)

print(f"✅ Plots saved in '{plot_file}'")

# Optional: display the plot
# plt.show()
