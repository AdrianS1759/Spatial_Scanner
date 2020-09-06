# Import libraries 
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
  
  
# Creating dataset 
r = 10
x = []
y = []
z = []
n = 50
for i in np.linspace(0, 2 * np.pi, num = n):
    for j in np.linspace(0, np.pi, num = n):
        x.append(r * np.sin(i) * np.cos(j))
        y.append(r * np.sin(i) * np.sin(j))
        z.append(r * np.cos(i))

# Creating figure 
fig = plt.figure() 
ax = plt.axes(projection ="3d") 
  
# Creating plot 
ax.scatter3D(x, y, z, color = "green"); 
plt.title("simple 3D scatter plot") 
  
# show plot 
plt.show() 