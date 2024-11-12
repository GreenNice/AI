import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2

class Problem:
    def __init__(self, image_path):
        self.image_path = image_path
        self.state_space = None
        self.z_values = None
        self.load_data()

    def load_data(self):
        # Load the image using OpenCV
        image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"Unable to load image from {self.image_path}")

        # Assuming each pixel corresponds to a state and its intensity to the evaluation value
        height, width = image.shape
        self.state_space = np.array([[x, y] for y in range(height) for x in range(width)])
        self.z_values = image.flatten()

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        xs = self.state_space[:, 0]
        ys = self.state_space[:, 1]
        zs = self.z_values

        ax.scatter(xs, ys, zs, c=zs, cmap='gray')

        plt.show()

    def draw_path(self, path):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        zs = [self.z_values[p[1] * self.state_space[-1][0] + p[0]] for p in path]

        ax.scatter(xs, ys, zs, c='red', marker='o')  # Path points in red
        ax.plot(xs, ys, zs, color='green')  # Path line in green

        self.show()  # Reuse the show method to display the plot

# Example usage
image_path = "C:\\Users\\Admin\\Desktop\\HK1_2024\\AI\\process2\\LocalSearch\\monalisa.jpg"  # Replace with the correct path to the image
problem = Problem(image_path)

# Suppose we have a path which is a list of (x, y) tuples
example_path = [(10, 10), (20, 20), (30, 30)]
problem.draw_path(example_path)
