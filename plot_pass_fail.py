import os
import matplotlib.pyplot as plt

# File storing previous build statuses
status_file = "build_status.txt"

# Determine current build status from environment variable
# You can set BUILD_STATUS=1 in Jenkins for success, 0 for failure
status = int(os.environ.get("BUILD_STATUS", "1"))

# Append current status to file
if os.path.exists(status_file):
    with open(status_file, "r") as f:
        statuses = [int(line.strip()) for line in f if line.strip()]
else:
    statuses = []

statuses.append(status)

with open(status_file, "w") as f:
    for s in statuses:
        f.write(f"{s}\n")

# Plot trend
plt.figure(figsize=(8,4))
plt.plot(range(1, len(statuses)+1), statuses, marker='o')
plt.title("Pass/Fail Trend")
plt.xlabel("Build Number")
plt.ylabel("Status (1=Pass, 0=Fail)")
plt.ylim(-0.1, 1.1)

