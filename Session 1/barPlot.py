import matplotlib.pyplot as plt

products = ["Product 1", "Product 2", "Product 3", "Product 4"]
sales = [350, 480, 290, 520]

plt.bar(products, sales, color = ["red", "blue", "green", "orange"])
plt.xlabel("Pruducts")
plt.ylabel("Sales")
plt.title("Sales data")
plt.show()

