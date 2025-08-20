# Air Spring Suspension Simulation

This repository contains a project for simulating an air spring suspension system using MATLAB/Simulink and Python automation. The workflow demonstrates generating simulation data, exporting it to CSV, and visualizing it in Python.

---

## Project Structure

```
air-spring-simulation/
├── AirSpringModel.slx        # Simulink model
├── air_spring_simulation.m   # MATLAB script to run simulation and export CSV
├── python_automation/        # Python scripts for plotting and analysis
│   ├── plot_air_spring.py
│   └── basics_practice.py
├── air_spring_output.csv     # CSV output from simulation
└── README.md
```

---

## Workflow

### 1. MATLAB/Simulink

* Set parameters in the MATLAB workspace (mass, damping, initial pressure, etc.).
* Run `AirSpringModel.slx` via the script `air_spring_simulation.m`.
* Log key signals (`displacement`, `velocity`, `force`) using Simulink signal logging.
* Export results to `air_spring_output.csv` using the MATLAB table and `writetable`.

### 2. Python Automation

* Use Python scripts in the `python_automation/` folder to:

  * Read the CSV data using `pandas` or `csv` module.
  * Plot the signals using `matplotlib`.
  * Perform basic analysis, e.g., calculate mean, max, min, or visualize multiple signals with subplots.

Example Python snippet:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('air_spring_output.csv')

# Plot displacement, velocity, force
plt.figure(figsize=(10,6))
plt.plot(df['time'], df['displacement'], label='Displacement')
plt.plot(df['time'], df['velocity'], label='Velocity')
plt.plot(df['time'], df['force'], label='Force')
plt.xlabel('Time [s]')
plt.ylabel('Signal Value')
plt.title('Air Spring Simulation Results')
plt.legend()
plt.show()
```

---

## Requirements

* MATLAB/Simulink
* Python 3.x
* Python packages:

  * `pandas`
  * `matplotlib`

Install Python packages:

```bash
pip install pandas matplotlib
```

---

## Future Work

* Integrate with Jenkins for automated simulations.
* Extend Simulink model with more complex suspension parameters.
* Generate automated CSV reports for multiple scenarios.

---

## Author

Omrez Khan
Email: [your.email@example.com](mailto:your.email@example.com)
GitHub: [https://github.com/omrezkhan](https://github.com/omrezkhan)
