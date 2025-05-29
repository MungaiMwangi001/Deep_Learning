import tensorflow as tf
import matplotlib.pyplot as plt


# Set up the data and model
X = tf.constant([[1.], [2.], [3.], [4.]])
y = tf.constant([[2.], [4.], [6.], [8.]])

w = tf.Variable(0.)
b = tf.Variable(0.)

# Define the model and loss function
def model(x):
    return w * x + b

def loss(predicted_y, true_y):
    return tf.reduce_mean(tf.square(predicted_y - true_y))

# Set the learning rate
learning_rate = 0.001

# Training loop
losses = []
for i in range(250):
    with tf.GradientTape() as tape:
        predicted_y = model(X)
        current_loss = loss(predicted_y, y)
    gradients = tape.gradient(current_loss, [w, b])
    w.assign_sub(learning_rate * gradients[0])
    b.assign_sub(learning_rate * gradients[1])
    
    losses.append(current_loss.numpy())

# Plot the loss
plt.plot(losses)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.show()