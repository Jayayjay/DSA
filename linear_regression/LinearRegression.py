import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

# Part 1: Manual implementation of Linear Regression using numpy
class LinearRegressionManual:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        """
        Implements the normal equation: β = (X^T X)^(-1) X^T y
        """
        # Add column of ones for intercept
        X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))
        
        # Normal equation solution
        XTX = np.dot(X_with_intercept.T, X_with_intercept)
        XTX_inv = np.linalg.inv(XTX)
        XTy = np.dot(X_with_intercept.T, y)
        beta = np.dot(XTX_inv, XTy)
        
        # Store results
        self.intercept = beta[0]
        self.coefficients = beta[1:]
        
        return self
    
    def predict(self, X):
        """
        Make predictions using the fitted model
        """
        X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))
        beta = np.concatenate(([self.intercept], self.coefficients))
        return np.dot(X_with_intercept, beta)
    
    def score(self, X, y):
        """
        Calculate R^2 score
        """
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y))**2)
        ss_residual = np.sum((y - y_pred)**2)
        return 1 - (ss_residual / ss_total)

# Part 2: Gradient Descent Implementation
class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.coefficients = None
        self.intercept = None
        self.cost_history = []
    
    def fit(self, X, y):
        """
        Fit linear model using gradient descent
        """
        # Initialize parameters
        m, n = X.shape
        self.coefficients = np.zeros(n)
        self.intercept = 0
        
        # Gradient descent
        for i in range(self.iterations):
            # Make predictions with current params
            y_pred = self.predict(X)
            
            # Calculate gradients
            dw = (1/m) * np.dot(X.T, (y_pred - y))
            db = (1/m) * np.sum(y_pred - y)
            
            # Update parameters
            self.coefficients -= self.learning_rate * dw
            self.intercept -= self.learning_rate * db
            
            # Calculate and store cost
            cost = (1/(2*m)) * np.sum((y_pred - y)**2)
            self.cost_history.append(cost)
        
        return self
    
    def predict(self, X):
        """
        Make predictions using the fitted model
        """
        return np.dot(X, self.coefficients) + self.intercept

# Part 3: Examples using the implementations

def simple_example():
    """
    Example 1: Simple linear regression with synthetic data
    """
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2 + 3 * X.squeeze() + np.random.randn(100) * 2
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train our manual model
    model_manual = LinearRegressionManual().fit(X_train, y_train)
    
    # Train scikit-learn model for comparison
    model_sklearn = LinearRegression().fit(X_train, y_train)
    
    # Make predictions
    y_pred_manual = model_manual.predict(X_test)
    y_pred_sklearn = model_sklearn.predict(X_test)
    
    # Print results
    print("Manual Implementation:")
    print(f"Intercept: {model_manual.intercept:.4f}, Coefficient: {model_manual.coefficients[0]:.4f}")
    print(f"R^2 Score: {model_manual.score(X_test, y_test):.4f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred_manual):.4f}")
    
    print("\nScikit-learn Implementation:")
    print(f"Intercept: {model_sklearn.intercept_:.4f}, Coefficient: {model_sklearn.coef_[0]:.4f}")
    print(f"R^2 Score: {r2_score(y_test, y_pred_sklearn):.4f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred_sklearn):.4f}")
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, alpha=0.7, label='Data')
    X_line = np.linspace(0, 10, 100).reshape(-1, 1)
    plt.plot(X_line, model_manual.predict(X_line), 'r-', linewidth=2, label='Manual LR')
    plt.plot(X_line, model_sklearn.predict(X_line), 'g--', linewidth=2, label='Scikit-learn LR')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title('Linear Regression: Manual vs Scikit-learn')
    plt.show()

def multiple_regression_example():
    """
    Example 2: Multiple linear regression with the boston housing dataset
    """
    # Create a small housing dataset
    data = {
        'size': [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0],
        'bedrooms': [2, 3, 3, 4, 4, 5, 5],
        'age': [10, 15, 8, 12, 5, 7, 10],
        'price': [2.5, 3.2, 4.0, 4.8, 5.5, 6.2, 7.0]
    }
    
    df = pd.DataFrame(data)
    X = df[['size', 'bedrooms', 'age']].values
    y = df['price'].values
    
    # Train our manual model
    model_manual = LinearRegressionManual().fit(X, y)
    
    # Make predictions
    y_pred = model_manual.predict(X)
    
    # Print results
    print("Multiple Regression Results:")
    print(f"Intercept: {model_manual.intercept:.4f}")
    print(f"Coefficients: Size={model_manual.coefficients[0]:.4f}, " + 
          f"Bedrooms={model_manual.coefficients[1]:.4f}, " + 
          f"Age={model_manual.coefficients[2]:.4f}")
    print(f"R^2 Score: {model_manual.score(X, y):.4f}")
    
    # Create table of actual vs predicted
    results = pd.DataFrame({
        'Actual': y,
        'Predicted': y_pred.round(2),
        'Error': (y - y_pred).round(2)
    })
    print("\nPredictions:")
    print(results)

def gradient_descent_example():
    """
    Example 3: Linear regression using gradient descent
    """
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2 + 3 * X.squeeze() + np.random.randn(100) * 2
    
    # Train models
    model_gd = LinearRegressionGD(learning_rate=0.01, iterations=1000).fit(X, y)
    model_normal = LinearRegressionManual().fit(X, y)
    
    # Print results
    print("Gradient Descent Results:")
    print(f"Intercept: {model_gd.intercept:.4f}, Coefficient: {model_gd.coefficients[0]:.4f}")
    
    print("\nNormal Equation Results:")
    print(f"Intercept: {model_normal.intercept:.4f}, Coefficient: {model_normal.coefficients[0]:.4f}")
    
    # Plot cost history
    plt.figure(figsize=(10, 6))
    plt.plot(model_gd.cost_history)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Gradient Descent Cost History')
    plt.grid(True)
    plt.show()
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, alpha=0.7, label='Data')
    X_line = np.linspace(0, 10, 100).reshape(-1, 1)
    plt.plot(X_line, model_gd.predict(X_line), 'r-', linewidth=2, label='Gradient Descent')
    plt.plot(X_line, model_normal.predict(X_line), 'g--', linewidth=2, label='Normal Equation')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title('Linear Regression: Gradient Descent vs Normal Equation')
    plt.show()

# Run the examples
if __name__ == "__main__":
    print("Example 1: Simple Linear Regression")
    simple_example()
    
    print("\nExample 2: Multiple Linear Regression")
    multiple_regression_example()
    
    print("\nExample 3: Gradient Descent")
    gradient_descent_example()