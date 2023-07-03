import numpy as np
import matplotlib.pyplot as plt

np.list1 = [100]
np.hights = [165, 172, 168, 175, 160, 170, 180, 176, 172, 165, 163, 168, 174, 169, 177, 170, 162, 168, 171, 175]
plt.hist(np.divide(np.hights, np.list1), bins = 30, color = "blue", alpha = 0.7)
plt.ylabel("Hights(in centimetres)")
plt.title("Data Distribution Analisys")
plt.show()
max_val = np.max(np.hights)
mean_val = np.mean(np.hights)
print(f"Max: {max_val/100}, Mean: {mean_val/100}")
