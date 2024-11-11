import cv2
import time
import os

# Percorsi dell'immagine e delle cartelle
#input_image_path = '~/Pictures/DisplayDump/DUMP.png'
input_image_path = os.path.expanduser("~/Pictures/DisplayDump/DUMP.png")
output_folder = os.path.expanduser("~/Pictures/DisplayDump/")

# Percorsi dei file Haar per il viso e gli occhi
face_cascade_path = '/home/rr/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/home/rr/haarcascades/haarcascade_eye.xml'

sample_time = 3

# Verifica dell'esistenza dei file Haar
if not os.path.isfile(face_cascade_path):
    print(f"Errore: Il file Haar per il viso non è stato trovato in {face_cascade_path}")
    exit()
if not os.path.isfile(eye_cascade_path):
    print(f"Errore: Il file Haar per gli occhi non è stato trovato in {eye_cascade_path}")
    exit()

# Carica i classificatori Haar
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Verifica che i file Haar siano stati caricati correttamente
if face_cascade.empty():
    print(f"Errore: Impossibile caricare il classificatore Haar per il viso da {face_cascade_path}")
    exit()
if eye_cascade.empty():
    print(f"Errore: Impossibile caricare il classificatore Haar per gli occhi da {eye_cascade_path}")
    exit()

# Funzione per elaborare l'immagine
def process_image():
    # Verifica se l'immagine di input esiste
    if not os.path.isfile(input_image_path):
        print(f"Errore: Immagine {input_image_path} non trovata o non leggibile.")
        return

    # Carica l'immagine originale
    img = cv2.imread(input_image_path)
    if img is None:
        print(f"Errore: Immagine {input_image_path} non caricata correttamente.")
        return

    # Converte l'immagine in scala di grigio per migliorare la rilevazione
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Rileva i volti nell'immagine
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        print("Nessun volto rilevato.")
        return

    # Per ogni volto rilevato, cerca gli occhi
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Rileva gli occhi all'interno del volto
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            print("Nessun occhio rilevato.")
            continue

        # Crea un'immagine nera con gli occhi ritagliati
        eyes_only_img = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
        eyes_only_img[:] = 0  # Imposta sfondo nero

        for (ex, ey, ew, eh) in eyes:
            # Copia solo gli occhi dalla regione del volto alla nuova immagine con sfondo nero
            eyes_only_img[ey:ey+eh, ex:ex+ew] = roi_color[ey:ey+eh, ex:ex+ew, 0]

        # Salva l'immagine degli occhi
        timestamp = int(time.time())
        output_path = os.path.join(output_folder, f"DUMP_EYE_{timestamp}.png")
        cv2.imwrite(output_path, eyes_only_img)
        print(f"Immagine degli occhi salvata in: {output_path}")

# Esegui il processo ogni "sample_time"  secondi
while True:
    process_image()
    time.sleep(sample_time)
