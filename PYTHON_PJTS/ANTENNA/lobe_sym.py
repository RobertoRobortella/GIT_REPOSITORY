import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def cone(origin, direction, angle, height, color='blue'):
    """
    Generate points to visualize a cone in 3D.
    """
    # Angle in radians
    angle = np.deg2rad(angle)
    radius = np.tan(angle) * height

    # Generate circular base
    theta = np.linspace(0, 2 * np.pi, 30)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)
    z_circle = np.zeros_like(theta)

    # Rotate the base circle to align with the direction
    rotation_matrix = get_rotation_matrix(direction)
    circle_points = np.dot(rotation_matrix, np.array([x_circle, y_circle, z_circle]))

    # Shift the circle to the tip of the cone
    cone_points = circle_points + np.array(origin).reshape(-1, 1)

    # Create the cone by connecting the tip with the base circle
    x = [origin[0]] + list(cone_points[0])
    y = [origin[1]] + list(cone_points[1])
    z = [origin[2]] + list(cone_points[2])

    return x, y, z

def get_rotation_matrix(direction):
    """
    Return a rotation matrix that aligns [0, 0, 1] with the given direction.
    """
    z_axis = np.array([0, 0, 1])
    direction = direction / np.linalg.norm(direction)
    v = np.cross(z_axis, direction)
    c = np.dot(z_axis, direction)
    s = np.linalg.norm(v)

    if s == 0:
        return np.eye(3)  # No rotation needed

    # Compute the rotation matrix using the Rodrigues' rotation formula
    k = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + k + k @ k * ((1 - c) / (s ** 2))
    return rotation_matrix

# Define radar antenna positions and directions
positions = [
    [0, 0, 0],   # Position of first radar
    [10, 0, 0],  # Position of second radar
    [5, 10, 0]   # Position of third radar
]
directions = [
    [5, 5, 10],  # Direction vector pointing toward the target
    [-5, 5, 10],
    [0, -10, 10]
]
angle = 20  # Cone angle in degrees
height = 10  # Height of each cone

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each cone
colors = ['blue', 'green', 'red']
for pos, dir, color in zip(positions, directions, colors):
    x, y, z = cone(pos, dir, angle, height, color=color)
    ax.plot_trisurf(x, y, z, color=color, alpha=0.5)

# Mark the target point where the cones are intersecting
target = [5, 5, 10]
ax.scatter(*target, color='black', s=100, label="Target Point")

# Set plot limits and labels
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)
ax.set_zlim(0, 15)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Radar Lobes Intersecting')

plt.legend()
plt.show()
