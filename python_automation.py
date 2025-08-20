import pandas as pd
import matplotlib.pyplot as plt
import os

# Absolute path to local plots folder
plots_dir = '/home/omrez/Downloads/MAt_working/python_jenkins/plots'
os.makedirs(plots_dir, exist_ok=True)

# Load CSV
csv_path = '/home/omrez/Downloads/MAt_working/python_jenkins/air_spring_output.csv'
df = pd.read_csv(csv_path)

time = df['time']
displacement = df['displacement']
velocity = df['velocity']
force = df['force']

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

axs[0].plot(time, displacement, 'b'); axs[0].set_ylabel('Displacement [m]'); axs[0].grid(True); axs[0].set_title('Air Spring Simulation Signals')
axs[1].plot(time, velocity, 'g'); axs[1].set_ylabel('Velocity [m/s]'); axs[1].grid(True)
axs[2].plot(time, force, 'r'); axs[2].set_ylabel('Force [N]'); axs[2].set_xlabel('Time [s]'); axs[2].grid(True)

plt.tight_layout()

# Save figure directly to local plots folder
save_path = os.path.join(plots_dir, 'air_spring_subplots.png')
plt.savefig(save_path)
plt.close(fig)  # close figure to avoid memory issues

print(f"✅ Plots saved in '{save_path}'")
