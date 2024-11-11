import cv2
import time
import os

# Percorso dell'immagine di input
input_image_path = '/home/Pictures/DisplayDump/DUMP.png'
output_folder = '/home/Pictures/DisplayDump/'

# Percorsi assoluti per i classificatori Haar (modifica con il percorso corretto)
face_cascade_path = '/home/rr/Documents/WORKSPACE/GIT_REPOSITORY/PYTHON_PJTS/MEM_DUMP/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/home/rr/Documents/WORKSPACE/GIT_REPOSITORY/PYTHON_PJTS/MEM_DUMP/haarcascades/haarcascade_eye.xml'

# Carica il classificatore Haar per il viso e gli occhi
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Controllo di errore per il caricamento dei file Haar
if face_cascade.empty():
    print("Errore: Impossibile caricare il classificatore Haar per il viso.")
    exit()
if eye_cascade.empty():
    print("Errore: Impossibile caricare il classificatore Haar per gli occhi.")
    exit()

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
        print("Nessun volto rilevato")
        return

    # Trova gli occhi per ogni volto
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]  # Seleziona la regione del volto
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Per ogni occhi rilevato, creiamo un'immagine di solo occhi con sfondo nero
        if len(eyes) > 0:
            for i, (ex, ey, ew, eh) in enumerate(eyes):
                # Ritaglia l'occhio
                eye_img = img[y + ey:y + ey + eh, x + ex:x + ex + ew]
                eye_img_black = cv2.cvtColor(eye_img, cv2.COLOR_BGR2BGRA)  # Aggiungi canale alfa per lo sfondo nero
                eye_img_black[:, :, 3] = 0  # Imposta trasparente il canale alfa

                # Imposta l'immagine degli occhi in un'immagine nera di stessa dimensione
                final_eye_img = 255 * np.ones_like(img, dtype=np.uint8)  # Sfondo nero
                final_eye_img[y + ey:y + ey + eh, x + ex:x + ex + ew] = eye_img

                # Salva l'immagine con un nome incrementale
                file_count = len([f for f in os.listdir(output_folder) if f.startswith('DUMP_EYE')])
                output_image_path = os.path.join(output_folder, f'DUMP_EYE_{file_count + 1}.png')
                cv2.imwrite(output_image_path, final_eye_img)
                print(f"Immagine salvata: {output_image_path}")

# Ciclo che esegue l'analisi ogni 10 secondi
while True:
    process_image()
    time.sleep(10)
