import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Funzione per creare una sfera
def create_sphere(radius, center, num_points=100):
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, np.pi, num_points)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# Funzione per l'animazione
def update(num, ax, sphere_data, t):
    ax.cla()  # Clear the axis
    ax.set_box_aspect([1, 1, 1])  # Equal scaling
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Fasi sfasate di 30° per il movimento oscillatorio
    x_offset = np.sin(t + 0)  # Oscillazione in x
    y_offset = np.sin(t + np.pi / 6)  # Oscillazione in y, sfasata di 30°
    z_offset = np.sin(t + np.pi / 3)  # Oscillazione in z, sfasata di 60°

    # Ruotiamo la sfera e applica l'oscillazione
    x, y, z = sphere_data
    ax.plot_surface(x + x_offset, y + y_offset, z + z_offset, color=plt.cm.RdYlBu(num / 100), rstride=5, cstride=5)

# Creazione della figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dati della sfera
radius = 1
center = [0, 0, 0]
sphere_data = create_sphere(radius, center)

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(ax, sphere_data, np.linspace(0, 2 * np.pi, 100)), interval=100)

plt.show()
