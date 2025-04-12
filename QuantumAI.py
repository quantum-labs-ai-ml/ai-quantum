import qsharp
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Simulate the Q# code (assumes QuantumRandom.qs is in the same directory)
from QuantumRandomAI import GenerateRandomBits

# Generate quantum random bits
num_bits = 100
random_bits = GenerateRandomBits.simulate(count=num_bits)
print(f"Quantum Random Bits: {random_bits}")

# Create a synthetic dataset influenced by quantum random bits
np.random.seed(42)  # For reproducibility
X = np.random.rand(num_bits, 2)  # 100 samples, 2 features
y = np.zeros(num_bits, dtype=int)

# Use quantum random bits to flip labels randomly (simulating quantum influence)
for i in range(num_bits):
    if random_bits[i] == 1:  # Q# Result.One maps to 1
        y[i] = np.random.choice([0, 1])  # Randomly flip label
    else:
        y[i] = 0  # Keep label as 0

# Split data into train and test
train_size = int(0.8 * num_bits)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Train a simple logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"AI Model Accuracy: {accuracy:.2f}")

# Optional: Show a few predictions
print(f"Sample Predictions: {y_pred[:5]}")
print(f"Actual Labels: {y_test[:5]}")
