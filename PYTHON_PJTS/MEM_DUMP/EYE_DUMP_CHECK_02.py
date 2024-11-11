import cv2

face_cascade_path = '/home/rr/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

if face_cascade.empty():
    print(f"Errore: Impossibile caricare il classificatore Haar per il viso da {face_cascade_path}")
else:
    print("File Haar caricato correttamente.")
