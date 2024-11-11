import cv2
import time
import os

# Percorso dell'immagine di input
input_image_path = '/home/Pictures/DisplayDump/DUMP.png'
output_folder = '/home/Pictures/DisplayDump/'

# Percorsi assoluti per i file Haar
face_cascade_path = '/home/rr/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/home/rr/haarcascades/haarcascade_eye.xml'

# Carica il classificatore Haar per il viso e gli occhi
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Controllo di errore per il caricamento dei file Haar
if face_cascade.empty():
    print(f"Errore: Impossibile caricare il classificatore Haar per il viso da {face_cascade_path}")
    exit()
if eye_cascade.empty():
    print(f"Errore: Impossibile caricare il classificatore Haar per gli occhi da {eye_cascade_path}")
    exit()

# Funzione per elaborare l'immagine
def process_image():
    # Carica l'immagine originale
    img = cv2.imread(input_image_path)
    
    if img is None:
        print(f"Errore: Immagine {input_image_path} non trovata o non leggibile.")
        return

    # Converte l'immagine in scala di grigio per migliorare la rilevazione
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Rileva i volti
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Se non vengono rilevati volti, esci
    if len(faces) == 0:
        print("Nessun volto rilevato.")
        return

    # Per ogni volto rilevato, cerca gli occhi
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Rileva gli occhi all'interno del volto
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Crea un'immagine nera e disegna solo gli occhi
            eye_img = cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 255), -1)

            # Salva l'immagine degli occhi
            timestamp = int(time.time())
            output_path = os.path.join(output_folder, f"DUMP_EYE_{timestamp}.png")
            cv2.imwrite(output_path, eye_img)
            print(f"Immagine degli occhi salvata in: {output_path}")

# Esegui il processo ogni 10 secondi
while True:
    process_image()
    time.sleep(10)
