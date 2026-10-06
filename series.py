import pandas as pd
import numpy as np

# Generate 10 random numbers
np.random.seed(42)
numbers = np.random.randint(1, 101, 10)

# Create Pandas Series
s = pd.Series(numbers)

# Display the Series
print(s)python --version
