import numpy as np

# Create numbers from 1 to 10
numbers = []

for i in range(1, 11):
    numbers.append(i)

arr = np.array(numbers)

print(arr)
print(arr.ndim)
