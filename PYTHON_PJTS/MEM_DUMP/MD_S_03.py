import time
import keyboard
from PIL import ImageGrab

# Funzione per acquisire e mostrare lo screenshot del secondo schermo
def capture_and_show():
    # Acquisisce uno screenshot dell'intero desktop
    screenshot = ImageGrab.grab()

    # Ritaglia l'area corrispondente al secondo schermo (DP-0: 900x1600 partendo da (0, 0))
    second_screen_area = (0, 0, 900, 1600)  # Coordinate x0, y0, x1, y1
    second_screen = screenshot.crop(second_screen_area)

    # Mostra lo screenshot ritagliato del secondo schermo
    second_screen.show()

# Ciclo per acquisire l'immagine ogni 0.5 secondi
while True:
    capture_and_show()
    time.sleep(0.5)  # Aspetta 0.5 secondi

    # Controlla se la tecla 'Q' è stata premuta per uscire
    if keyboard.is_pressed('q'):  # Se premi 'Q', interrompi il ciclo
        print("Uscita... premiato Q")
        break
