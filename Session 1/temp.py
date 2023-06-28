import matplotlib.pyplot as plt 
import random

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
temperature = [25.3, 27.1, 24.8, 26.5, 22.9, 23.7, 25.2, 26.8, 24.5, 23.9, 26.1, 28.3]
humidity = [33.4, 26.2, 35.1, 34.9, 30.5, 29.6, 29.6, 30.1, 31.2, 29.6, 26.5, 30.1]

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

for m, zlow, zhigh, in [("o", -50, -25), ("^", -30, -5)]:
    xs = years
    ys = temperature
    zs = humidity
    ax.scatter(xs, ys, zs, color = "green")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature")
ax.set_zlabel("Humidity")
plt.show()
