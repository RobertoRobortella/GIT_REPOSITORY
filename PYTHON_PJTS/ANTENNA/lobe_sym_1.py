import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_cone(origin, direction, angle, height, num_points=50):
    """
    Generate the points of a 3D cone from the origin in the given direction.
    """
    # Convert angle to radians and compute radius at the base of the cone
    angle_rad = np.deg2rad(angle)
    radius = np.tan(angle_rad) * height
    
    # Generate points for the circular base of the cone
    theta = np.linspace(0, 2 * np.pi, num_points)
    x_base = radius * np.cos(theta)
    y_base = radius * np.sin(theta)
    z_base = np.full_like(theta, height)

    # Stack points in 3D
    base_points = np.vstack((x_base, y_base, z_base))
    
    # Rotate the base to align with the direction vector
    rotation_matrix = get_rotation_matrix(direction)
    rotated_base = rotation_matrix @ base_points

    # Translate to the origin
    cone_points = rotated_base + np.array(origin).reshape(-1, 1)
    
    # Include the tip of the cone at the origin
    x = [origin[0]] + list(cone_points[0])
    y = [origin[1]] + list(cone_points[1])
    z = [origin[2]] + list(cone_points[2])
    
    return x, y, z

def get_rotation_matrix(direction):
    """
    Calculate a rotation matrix that aligns [0, 0, 1] with the given direction.
    """
    direction = direction / np.linalg.norm(direction)
    z_axis = np.array([0, 0, 1])
    v = np.cross(z_axis, direction)
    s = np.linalg.norm(v)
    c = np.dot(z_axis, direction)

    if s == 0:
        return np.eye(3)  # No rotation needed

    k = np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])
    rotation_matrix = np.eye(3) + k + k @ k * ((1 - c) / (s ** 2))
    return rotation_matrix

# Define radar positions and directions
positions = [
    [0, 0, 0],    # Position of first radar
    [10, 0, 0],   # Position of second radar
    [5, 10, 0]    # Position of third radar
]
directions = [
    [5, 5, 10],   # Direction vector towards the target
    [-5, 5, 10],
    [0, -10, 10]
]
angle = 15       # Cone angle in degrees
height = 15      # Height to extend beyond the target

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each cone representing the radar lobe
colors = ['blue', 'green', 'red']
for pos, dir, color in zip(positions, directions, colors):
    x, y, z = generate_cone(pos, dir, angle, height)
    ax.plot_trisurf(x, y, z, color=color, alpha=0.4)

# Mark the target point at the intersection of the lobe directions
target = [5, 5, 10]
ax.scatter(*target, color='black', s=100, label="Target Point")

# Set plot limits and labels
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)
ax.set_zlim(0, 20)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Radar Lobes Intersecting')
plt.legend()
plt.show()
