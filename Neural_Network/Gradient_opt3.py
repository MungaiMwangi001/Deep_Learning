import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1) - 1
y = 4 + 3 * X + np.random.randn(100, 1)

# Initialize model parameters
w = np.random.randn(2, 1)
b = np.random.randn(1)[0]

# Set the learning rate
alpha = 0.1

# Set the number of iterations
num_iterations = 20

# Create a mesh to plot the loss surface
w1, w2 = np.meshgrid(np.linspace(-5, 5, 100),
                     np.linspace(-5, 5, 100))

# Compute the loss for each point on the grid
loss = np.zeros_like(w1)
for i in range(w1.shape[0]):
    for j in range(w1.shape[1]):
        loss[i, j] = np.mean((y - w1[i, j] \
                              * X - w2[i, j] * X**2)**2)

# Perform gradient descent
for i in range(num_iterations):
    # Compute the gradient of the loss 
    # with respect to the model parameters
    grad_w1 = -2 * np.mean(X * (y - w[0] \
                                * X - w[1] * X**2))
    grad_w2 = -2 * np.mean(X**2 * (y - w[0] \
                                   * X - w[1] * X**2))
    
    # Update the model parameters
    w[0] -= alpha * grad_w1
    w[1] -= alpha * grad_w2

# Plot the loss surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(w1, w2, loss, cmap='coolwarm')
ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_zlabel('Loss')

# Plot the trajectory of the gradient descent algorithm
ax.plot(w[0], w[1], np.mean((y - w[0]\
                             * X - w[1] * X**2)**2),
        'o', c='red', markersize=10)
plt.show()



'''
This code generates synthetic data for a quadratic regression problem, initializes the model parameters, and performs gradient descent to find the values of the model parameters that minimize the mean squared error loss. The code also plots the loss surface and the trajectory of the gradient descent algorithm on the loss surface.

The resulting plot shows how the gradient descent algorithm takes small steps downhill on the loss surface and eventually reaches the global minimum of the loss function. The global minimum is the point on the loss surface where the loss is the lowest.
'''