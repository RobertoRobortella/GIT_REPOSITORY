import cv2

# Caricamento dei modelli pre-addestrati per il rilevamento facciale e degli occhi
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Apertura delle webcam
cam1 = cv2.VideoCapture(0)  # Webcam primaria per il riconoscimento del viso
cam2 = cv2.VideoCapture(1)  # Seconda webcam per visualizzazione in base al movimento degli occhi

# Funzione per calcolare il rettangolo da mostrare su cam2
def get_subregion(center_x, center_y, width, height, zoom=0.6):
    # Calcolo le dimensioni della sotto-porzione da visualizzare
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

    # Conversione del frame della prima webcam in scala di grigi
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Rilevamento dei volti nella webcam principale
    faces = face_cascade.detectMultiScale(gray1, 1.3, 5)
    if len(faces) > 0:
        # Prendo il primo volto rilevato
        (x, y, w, h) = faces[0]

        # Estraggo la regione facciale e cerco gli occhi all'interno
        face_roi_gray = gray1[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi_gray)

        if len(eyes) >= 2:
            # Prendo le posizioni dei primi due occhi rilevati
            eye1 = eyes[0]
            eye2 = eyes[1]

            # Calcolo del punto centrale tra gli occhi
            eye1_center = (x + eye1[0] + eye1[2] // 2, y + eye1[1] + eye1[3] // 2)
            eye2_center = (x + eye2[0] + eye2[2] // 2, y + eye2[1] + eye2[3] // 2)
            center_x = (eye1_center[0] + eye2_center[0]) // 2
            center_y = (eye1_center[1] + eye2_center[1]) // 2

            # Imposto la sotto-porzione dell'immagine della seconda webcam in base alla posizione degli occhi
            height, width = frame2.shape[:2]
            x1, y1, sub_width, sub_height = get_subregion(center_x, center_y, width, height)

            # Estraggo e ridimensiono la sotto-porzione per adattarla all'intera finestra di visualizzazione
            sub_frame2 = frame2[y1:y1+sub_height, x1:x1+sub_width]
            sub_frame2_resized = cv2.resize(sub_frame2, (width, height))

            # Visualizzo la porzione calcolata del secondo frame
            cv2.imshow("Webcam 2 - Visualizzazione sincronizzata", sub_frame2_resized)

        # Disegno il volto e il centro degli occhi per il debug sulla prima webcam
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.circle(frame1, eye1_center, 5, (0, 255, 0), -1)
        cv2.circle(frame1, eye2_center, 5, (0, 255, 0), -1)

    # Visualizzo la prima webcam con il rilevamento del volto e degli occhi
    cv2.imshow("Webcam 1 - Rilevamento Viso", frame1)

    # Uscita premendo 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascio delle risorse
cam1.release()
cam2.release()
cv2.destroyAllWindows()
