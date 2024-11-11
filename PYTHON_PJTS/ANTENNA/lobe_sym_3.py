import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_cone_volume(origin, target, angle, height_factor=1.2, num_points=1000):
    """
    Generate points filling a 3D cone volume from the origin towards the target.
    """
    # Extend the cone height beyond the target by the height_factor
    direction = np.array(target) - np.array(origin)
    height = np.linalg.norm(direction) * height_factor
    direction = direction / np.linalg.norm(direction)  # Normalize direction

    # Convert angle to radians and compute radius at the base of the cone
    angle_rad = np.deg2rad(angle)
    cone_points = []

    for _ in range(num_points):
        # Random distance along the cone's height
        h = np.random.uniform(0, height)
        
        # Calculate the radius at this height
        r = h * np.tan(angle_rad)
        
        # Random angle around the cone axis
        theta = np.random.uniform(0, 2 * np.pi)
        
        # Convert polar to Cartesian coordinates for the point
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = h
        
        # Create the point in the cone's local coordinate system
        point = np.array([x, y, z])
        
        # Rotate the point to align with the direction vector
        rotation_matrix = get_rotation_matrix(direction)
        rotated_point = rotation_matrix @ point
        
        # Translate the point to the origin of the cone
        final_point = rotated_point + np.array(origin)
        cone_points.append(final_point)

    # Convert list to numpy array for easier handling
    cone_points = np.array(cone_points)
    return cone_points[:, 0], cone_points[:, 1], cone_points[:, 2]

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

# Define radar positions and target
positions = [
    [0, 0, 0],    # Position of first radar
    [10, 0, 0],   # Position of second radar
    [5, 10, 0]    # Position of third radar
]
target = [5, 5, 10]  # Target position

angle = 15           # Cone angle in degrees
height_factor = 1.2  # Extend height 20% beyond target

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each cone volume as a scatter plot of points
colors = ['blue', 'green', 'red']
for pos, color in zip(positions, colors):
    x, y, z = generate_cone_volume(pos, target, angle, height_factor)
    ax.scatter(x, y, z, color=color, alpha=0.1, s=1)

# Mark the target point where the cones are intersecting
ax.scatter(*target, color='black', s=100, label="Target Point")

# Set plot limits and labels
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)
ax.set_zlim(0, 20)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Radar Lobes with Volume')
plt.legend()
plt.show()
