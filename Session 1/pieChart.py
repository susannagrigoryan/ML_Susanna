import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Category D", "Caracter E"]
parcentages = [20, 30, 15, 30, 5]
explode = [0, 0.1, 0, 0.1, 0]
colors = ["red", "blue", "green", "orange", "purple"]

plt.pie(parcentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Parcentage Distribution")
plt.legend(categories)
plt.show()
