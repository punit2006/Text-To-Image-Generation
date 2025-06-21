import matplotlib.pyplot as plt

# Line plot
plt.plot([1,2,3,4,5], [10,20,30,40,50])
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar plot
plt.bar(['A', 'B', 'C', 'D'], [3,7,5,10], color='blue')
plt.title("Basic Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Scatter plot
plt.scatter([5,7,8,10,15], [20,10,30,40,70], color='green', marker='x')
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Custom plot
plt.plot([5,7,8,10,15], [20,10,30,40,70], color='red', linestyle='--', marker='o', linewidth=2)
plt.title("Custom Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
