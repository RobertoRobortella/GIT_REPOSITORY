import time
import curses
from PIL import ImageGrab
import os

# Funzione per acquisire e salvare lo screenshot del secondo schermo
def capture_and_save():
    # Acquisisce uno screenshot dell'intero desktop
    screenshot = ImageGrab.grab()

    # Ritaglia l'area corrispondente al secondo schermo (DP-0: 900x1600 partendo da (0, 0))
    second_screen_area = (0, 0, 900, 1600)  # Coordinate x0, y0, x1, y1
    second_screen = screenshot.crop(second_screen_area)

    # Assicurati che l'immagine sia nel formato RGB
    second_screen = second_screen.convert('RGB')

    # Salva l'immagine nella cartella /home/rr/Pictures/DisplayDump/DUMP.png
    save_path = "/home/rr/Pictures/DisplayDump/DUMP.png"
    second_screen.save(save_path)

    # Stampa il percorso dove l'immagine è stata salvata
    print(f"\nImmagine salvata in: {save_path}")
    print("Premi 'Q' per interrompere il ciclo di acquisizione.\n")

# Funzione per eseguire il ciclo con il controllo della tastiera
def main(stdscr):
    # Nasconde il cursore e imposta la modalità non bloccante
    curses.curs_set(0)
    stdscr.nodelay(1)  # Non bloccare l'input da tastiera
    stdscr.timeout(500)  # Imposta il timeout a 500ms (per evitare che il programma si blocchi)

    # Assicurati che la cartella esista
    output_folder = "/home/rr/Pictures/DisplayDump/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Stampa le informazioni iniziali (Fuori da curses)
    print("Acquisizione immagini in corso...")
    print(f"L'immagine verrà salvata in: {output_folder}")
    print("Premi 'Q' per interrompere l'esecuzione.\n")

    while True:
        capture_and_save()
        time.sleep(0.5)  # Aspetta 0.5 secondi

        # Controlla se la tecla 'Q' è stata premuta per uscire
        key = stdscr.getch()
        if key == ord('q'):  # Se premi 'Q', interrompi il ciclo
            print("\nUscita... premiato Q")
            break

# Avvia il programma con curses
curses.wrapper(main)
