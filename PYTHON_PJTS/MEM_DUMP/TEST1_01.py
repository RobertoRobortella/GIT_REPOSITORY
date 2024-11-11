import cv2
import os

# Percorso all'immagine nella cartella ~/Pictures/DisplayDUMP
image_path = os.path.expanduser("~/Pictures/DisplayDump/PROVA.png")

# Carica l'immagine
img = cv2.imread(image_path)

# Verifica se l'immagine è stata caricata correttamente
if img is None:
    print("Errore: Immagine non trovata o non leggibile.")
else:
    # Mostra l'immagine
    cv2.imshow("PROVA.png", img)
    cv2.waitKey(0)  # Aspetta che venga premuto un tasto
    cv2.destroyAllWindows()
