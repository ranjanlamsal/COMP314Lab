#graph.py
import matplotlib.pyplot as plt
from time_complexity import calculate_insertion_time, calculate_selection_time

sizes = [10, 100, 1000, 10000, 100000]
insertion_time= []
selection_time = []

for size in sizes:
    insertion_time.append(calculate_insertion_time(size))
    selection_time.append(calculate_selection_time(size))


# Graph
x = sizes
y1 = insertion_time
y2 = selection_time
print(f"Insertion sort time:{insertion_time}")
print(f"selection sort time:{selection_time}")
# Plotting
plt.plot(x, y1, marker='o', color='b', label='Insertion sort')
plt.plot(x, y2, marker='s', color='r', label='Selection Sort')

# Adding labels and title
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Insertion and Selection Sort')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
