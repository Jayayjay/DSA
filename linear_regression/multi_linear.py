import numpy as np
import pandas as pd

# Input data from the table
X1 = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])  # House Size
X2 = np.array([3, 3, 4, 4, 2, 3, 4, 5, 3, 4])  # Bedrooms
Y = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])  # Price

# Design matrix with a column of ones for β₀ (intercept)
X = np.column_stack((np.ones(len(X1)), X1, X2))
print(X)

# Calculate the regression coefficients using the normal equation: β = (XᵀX)⁻¹XᵀY
beta = np.linalg.inv(X.T @ X) @ X.T @ Y

# Predict price for a house with 1800 sqft and 3 bedrooms
x_new = np.array([1, 1800, 3])
predicted_price = x_new @ beta

print(beta, predicted_price)
