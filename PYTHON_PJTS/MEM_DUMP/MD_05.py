import subprocess
import numpy as np
from PIL import Image

# Funzione per ottenere la risoluzione dello schermo
def get_screen_resolution():
    result = subprocess.run(['xrandr'], capture_output=True, text=True)
    output = result.stdout

    # Cerca la risoluzione attiva
    for line in output.splitlines():
        if "*" in line:
            parts = line.split()
            width, height = map(int, parts[0].split('x'))
            depth = 24  # Presunzione di 24 bit di profondità; modifica se necessario
            return width, height, depth
    raise ValueError("Impossibile ottenere la risoluzione dello schermo")

# Ottieni risoluzione e profondità del colore
width, height, depth = get_screen_resolution()
bytes_per_pixel = depth // 8

# Calcola il numero di byte per riga con padding
stride = (width * bytes_per_pixel + 3) & ~3  # Allineamento a 4 byte

print(f"Risoluzione rilevata: {width}x{height}")
print(f"Profondità di colore: {depth} bit")
print(f"Byte per pixel: {bytes_per_pixel}")
print(f"Stride (byte per riga con padding): {stride}")

# Legge dal framebuffer gestendo l'interlacciamento delle righe
with open("/dev/fb0", "rb") as fb:
    even_lines = []  # Linee pari
    odd_lines = []   # Linee dispari
    
    # Alterna tra linee pari e dispari
    for i in range(height):
        row = fb.read(stride)[:width * bytes_per_pixel]  # Ignora il padding
        if i % 2 == 0:
            even_lines.append(row)
        else:
            odd_lines.append(row)

    # Combina le righe pari e dispari per ricostruire l'immagine
    img_data = b''.join(even_lines[i // 2] if i % 2 == 0 else odd_lines[i // 2] for i in range(height))
    
    # Converte i dati in un array NumPy
    img_array = np.frombuffer(img_data, dtype=np.uint8).reshape((height, width, bytes_per_pixel))
    
    # Gestisci RGB o RGBA
    if bytes_per_pixel == 3:
        img = Image.fromarray(img_array, 'RGB')
    elif bytes_per_pixel == 4:
        img = Image.fromarray(img_array[:, :, :3], 'RGB')
    else:
        raise ValueError("Formato di colore non supportato")

# Visualizza informazioni di debug e mostra l'immagine
print("Immagine letta e ricostruita dal framebuffer con successo.")
print(f"Dimensioni immagine: {img.size}")
print(f"Formato immagine: {img.mode}")
img.show()
