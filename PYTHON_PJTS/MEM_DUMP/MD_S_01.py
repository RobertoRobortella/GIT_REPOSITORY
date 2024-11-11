import subprocess
import numpy as np
from PIL import Image

# Funzione per ottenere la risoluzione dello schermo per fb1 (secondo schermo)
def get_screen_resolution():
    result = subprocess.run(['xrandr'], capture_output=True, text=True)
    output = result.stdout

    # Cerca la risoluzione attiva per il secondo schermo
    for line in output.splitlines():
        if "connected" in line and "HDMI-1" in line:  # Assumendo che HDMI-1 sia il secondo schermo
            parts = line.split()
            width, height = map(int, parts[3].split('x')[0].split('+'))
            depth = 24  # Imposta la profondità di default a 24 bit (RGB)
            return width, height, depth
    raise ValueError("Impossibile ottenere la risoluzione del secondo schermo")

# Ottieni risoluzione e profondità del colore
width, height, depth = get_screen_resolution()
bytes_per_pixel = depth // 8

# Usa il framebuffer del secondo schermo
framebuffer_device = "/dev/fb1"

print(f"Risoluzione rilevata (secondo schermo): {width}x{height}")
print(f"Profondità di colore: {depth} bit")
print(f"Byte per pixel: {bytes_per_pixel}")

# Legge dal secondo framebuffer
with open(framebuffer_device, "rb") as fb:
    data = fb.read(width * height * bytes_per_pixel)
    img_array = np.frombuffer(data, dtype=np.uint8).reshape((height, width, bytes_per_pixel))
    
    # Gestisci RGB o RGBA
    if bytes_per_pixel == 3:
        img = Image.fromarray(img_array, 'RGB')
    elif bytes_per_pixel == 4:
        img = Image.fromarray(img_array[:, :, :3], 'RGB')
    else:
        raise ValueError("Formato di colore non supportato")

# Visualizza informazioni di debug e mostra l'immagine
print("Immagine del secondo schermo letta con successo.")
print(f"Dimensioni immagine: {img.size}")
print(f"Formato immagine: {img.mode}")
img.show()
