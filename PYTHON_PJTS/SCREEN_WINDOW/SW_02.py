import cv2

# Caricamento dei modelli pre-addestrati per il rilevamento facciale e degli occhi
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Usa gli indici corretti per le webcam
cam1 = cv2.VideoCapture(2)  # Webcam su /dev/video2 per il rilevamento del viso
cam2 = cv2.VideoCapture(0)  # Webcam su /dev/video0 per la visualizzazione dinamica

# Controllo dell'apertura delle webcam
if not cam1.isOpened():
    print("Errore: Webcam 1 non trovata o non disponibile.")
    exit()
if not cam2.isOpened():
    print("Errore: Webcam 2 non trovata o non disponibile.")
    exit()

# Funzione per calcolare la sotto-porzione dell'immagine in base alla posizione degli occhi
def get_subregion(center_x, center_y, width, height, zoom=0.6):
    sub_width, sub_height = int(width * zoom), int(height * zoom)
    x1 = max(0, min(center_x - sub_width // 2, width - sub_width))
    y1 = max(0, min(center_y - sub_height // 2, height - sub_height))
    return x1, y1, sub_width, sub_height

while True:
    # Lettura dei frame da entrambe le webcam
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if not ret1 or not ret2:
        print("Errore nella lettura delle webcam")
        break

    # Conversione del frame della prima webcam in scala di grigi per il rilevamento
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Rilevamento del volto nella webcam principale
    faces = face_cascade.detectMultiScale(gray1, 1.3, 5)
    if len(faces) > 0:
        # Prendo il primo volto rilevato
        (x, y, w, h) = faces[0]

        # Estraggo la regione facciale e cerco gli occhi
        face_roi_gray = gray1[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi_gray)

        if len(eyes) >= 2:
            # Prendo le posizioni dei primi due occhi rilevati
            eye1 = eyes[0]
            eye2 = eyes[1]

            # Calcolo del punto centrale tra i due occhi
            eye1_center = (x + eye1[0] + eye1[2] // 2, y + eye1[1] + eye1[3] // 2)
            eye2_center = (x + eye2[0] + eye2[2] // 2, y + eye2[1] + eye2[3] // 2)
            center_x = (eye1_center[0] + eye2_center[0]) // 2
            center_y = (eye1_center[1] + eye2_center[1]) // 2

            # Definizione della sotto-porzione da visualizzare sulla seconda webcam
            height, width = frame2.shape[:2]
            x1, y1, sub_width, sub_height = get_subregion(center_x, center_y, width, height)

            # Estraggo e ridimensiono la sotto-porzione per adattarla alla finestra
            sub_frame2 = frame2[y1:y1+sub_height, x1:x1+sub_width]
            sub_frame2_resized = cv2.resize(sub_frame2, (width, height))

            # Mostra la sotto-porzione nella finestra della seconda webcam
            cv2.imshow('Webcam 2 - Porzione', sub_frame2_resized)

    # Visualizza il frame della prima webcam per riferimento
    cv2.imshow('Webcam 1 - Riconoscimento Viso', frame1)

    # Premere 'q' per uscire
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia le risorse e chiudi le finestre
cam1.release()
cam2.release()
cv2.destroyAllWindows()
