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
def update(num, ax, sphere_data):
    ax.cla()  # Clear the axis
    ax.set_box_aspect([1, 1, 1])  # Equal scaling
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Calcoliamo il valore di t per ogni frame
    t = num * 0.1  # Incrementiamo t per ogni frame

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

# Imposta il background del grafico a nero
fig.patch.set_facecolor('black')
ax.set_facecolor('black')  # Colore di sfondo dell'area 3D

# Rimuovi gli assi e disabilita la visualizzazione della griglia 3D
ax.set_axis_off()
ax.grid(False)  # Disabilita la griglia 3D

# Disabilita i pannelli di sfondo 3D
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Disabilita le linee degli assi
ax.xaxis.line.set_visible(False)
ax.yaxis.line.set_visible(False)
ax.zaxis.line.set_visible(False)

# Dati della sfera
radius = 1
center = [0, 0, 0]
sphere_data = create_sphere(radius, center)

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(ax, sphere_data), interval=100)

plt.show()
