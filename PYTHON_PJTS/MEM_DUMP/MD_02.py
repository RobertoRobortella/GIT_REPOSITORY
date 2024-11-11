import subprocess
import numpy as np
from PIL import Image

# Funzione per ottenere la risoluzione dello schermo con xrandr
def get_screen_resolution():
    # Esegui il comando xrandr per ottenere la risoluzione
    result = subprocess.run(['xrandr'], capture_output=True, text=True)
    output = result.stdout

    # Cerca la risoluzione attiva
    for line in output.splitlines():
        if "*" in line:  # La linea con "*" di solito contiene la risoluzione attuale
            parts = line.split()
            width, height = map(int, parts[0].split('x'))
            depth = 24  # Profondità di colore di default, tipicamente 24 bit (RGB)
            return width, height, depth
    raise ValueError("Impossibile ottenere la risoluzione dello schermo")

# Ottieni risoluzione e profondità del colore
width, height, depth = get_screen_resolution()

# Determina il numero di byte per pixel in base alla profondità del colore
bytes_per_pixel = depth // 8

# Legge dal framebuffer e mostra l'immagine
with open("/dev/fb0", "rb") as fb:
    # Calcola il numero di byte da leggere in base alla risoluzione e alla profondità di colore
    data = fb.read(width * height * bytes_per_pixel)
    
    # Converte i dati in un array NumPy
    img_array = np.frombuffer(data, dtype=np.uint8).reshape((height, width, bytes_per_pixel))
    
    # Se il framebuffer è in formato RGB (3 canali), crea un'immagine RGB
    if bytes_per_pixel == 3:
        img = Image.fromarray(img_array, 'RGB')
    elif bytes_per_pixel == 4:  # RGBA
        img = Image.fromarray(img_array[:, :, :3], 'RGB')  # Ignora l'ultimo canale se presente
    else:
        raise ValueError("Formato di colore non supportato")

img.show()
