import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV file
df = pd.read_csv('air_spring_output.csv')

# Extract signals
time = df['time']
displacement = df['displacement']
velocity = df['velocity']
force = df['force']

# Create folder for plots if it doesn't exist
os.makedirs('plots', exist_ok=True)

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
plt.savefig('plots/air_spring_subplots.png')

# Display the plots
plt.show()

print("✅ Plots saved in 'plots/air_spring_subplots.png'")
