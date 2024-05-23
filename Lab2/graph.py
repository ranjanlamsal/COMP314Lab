#graph.py
import matplotlib.pyplot as plt
from time_complexity import calculate_merge_time, calculate_quick_time

sizes = [10, 100, 1000, 10000, 100000]
merge_time= []
quick_time = []

for size in sizes:
    merge_time.append(calculate_merge_time(size))
    quick_time.append(calculate_quick_time(size))


# Graph
x = sizes
y1 = merge_time
y2 = quick_time
print(f"Merge sort time:{merge_time}")
print(f"Quick sort time:{quick_time}")

# Plotting
plt.plot(x, y1, marker='o', color='b', label='Merge sort')
plt.plot(x, y2, marker='s', color='r', label='Quick Sort')

# Adding labels and title
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Merge and Quick Sort')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
