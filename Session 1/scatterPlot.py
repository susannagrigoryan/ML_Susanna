import random
import matplotlib.pyplot as plt

random.seed(42)
x = [random.random() for _ in range(50)]
y = [random.random() for _ in range(50)]
colors = [random.random() for _ in range(50)]
sizes = [random.randint(10,100) for _ in range(50)]
plt.scatter(x, y, c = colors, s = sizes, marker = "o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
plt.grid(True)
plt.show()
