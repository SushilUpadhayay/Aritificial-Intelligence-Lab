import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs #epoch is one complete pass through the entire training dataset.
        self.weights = None
        self.bias = None

    def activation(self, x):
        """Step function for activation."""
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        """
        Train the perceptron.
        :param X: Input features (2D array)
        :param y: Labels (1D array)
        """
        n_samples, n_features = X.shape
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            for idx, x_i in enumerate(X):
                # Calculate linear output
                linear_output = np.dot(x_i, self.weights) + self.bias
                # Apply activation function
                y_pred = self.activation(linear_output)
                # Compute the error
                error = y[idx] - y_pred
                # Update weights and bias
                self.weights += self.learning_rate * error * x_i
                self.bias += self.learning_rate * error

    def predict(self, X):
        """
        Make predictions.
        :param X: Input features (2D array)
        :return: Predicted labels
        """
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation(x) for x in linear_output])

# Example usage
if __name__ == "__main__":
    # Input data (AND gate example)
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([0, 0, 0, 1])  # AND gate labels

    # Create and train the perceptron
    perceptron = Perceptron(learning_rate=0.1, epochs=10)
    perceptron.fit(X, y)

    # Predict
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)
