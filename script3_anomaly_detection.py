import numpy as np

session_times = np.array([175, 182, 190, 168, 185, 3600, 179, 181, 5, 192])

mean = np.mean(session_times)
std_dev = np.std(session_times)

threshold = 2
outliers = []

for time in session_times:
    z_score = (time - mean) / std_dev
    if np.abs(z_score) > threshold:
        outliers.append(time)

print(outliers)
