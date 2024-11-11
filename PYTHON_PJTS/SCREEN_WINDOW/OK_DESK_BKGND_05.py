import cv2
import subprocess
import time
import os

# Funzione per catturare un'immagine dalla webcam
def capture_image():
    # Apre la webcam (indice 0 per la prima webcam)
    cap = cv2.VideoCapture(0)
    # per verificare se la camera funziona: ffplay /dev/video0
    if not cap.isOpened():
        print("Errore nell'aprire la webcam")
        return None

    # Cattura un singolo fotogramma
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Errore nella lettura dell'immagine")
        return None

    # Definisci il percorso per salvare l'immagine nella cartella Pictures/SH
    img_directory = os.path.expanduser('~/Pictures/SH')
    if not os.path.exists(img_directory):
        os.makedirs(img_directory)

    # Salva l'immagine come file temporaneo nella cartella specificata
    img_path = os.path.join(img_directory, 'webcam_background.jpg')
    cv2.imwrite(img_path, frame)
    return img_path

# Funzione per impostare l'immagine come sfondo
def set_background(image_path):
    try:
        # Assicurati che l'URI sia nel formato corretto
        image_uri = f"file://{os.path.abspath(image_path)}"
        command = f"gsettings set org.gnome.desktop.background picture-uri-dark {image_uri}"
        subprocess.run(command, shell=True, check=True)
        print(f"Immagine impostata come sfondo: {image_uri}")
    except Exception as e:
        print(f"Errore nel cambiamento dello sfondo: {e}")

# Ciclo principale per aggiornare il background continuamente
def main():
    while True:
        # Cattura un'immagine dalla webcam
        image_path = capture_image()
        if image_path:
            # Imposta l'immagine come sfondo
            set_background(image_path)
        
        # Aggiorna lo sfondo ogni 5 secondi (puoi cambiare la frequenza)
        time.sleep(5)

if __name__ == "__main__":
    main()
