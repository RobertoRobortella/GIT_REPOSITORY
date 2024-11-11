from PIL import ImageGrab

# Acquisisce uno screenshot dell'intero desktop
screenshot = ImageGrab.grab()

# Ritaglia l'area corrispondente al secondo schermo (DP-0: 900x1600 partendo da (0, 0))
second_screen_area = (0, 0, 900, 1600)  # Coordinate x0, y0, x1, y1
second_screen = screenshot.crop(second_screen_area)

# Mostra lo screenshot ritagliato del secondo schermo
second_screen.show()
