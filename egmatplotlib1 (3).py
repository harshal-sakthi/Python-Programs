import matplotlib.pyplot as plt
import pylab as pl

x = [1,2,3,4,5]
y = [5,20,15,25,10]

plt.scatter(x,y,color="red")
plt.title("Simple Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
pl.show()