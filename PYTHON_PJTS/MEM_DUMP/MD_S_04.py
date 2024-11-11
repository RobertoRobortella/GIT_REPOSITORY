import time
import curses
from PIL import ImageGrab

# Funzione per acquisire e mostrare lo screenshot del secondo schermo
def capture_and_show():
    # Acquisisce uno screenshot dell'intero desktop
    screenshot = ImageGrab.grab()

    # Ritaglia l'area corrispondente al secondo schermo (DP-0: 900x1600 partendo da (0, 0))
    second_screen_area = (0, 0, 900, 1600)  # Coordinate x0, y0, x1, y1
    second_screen = screenshot.crop(second_screen_area)

    # Mostra lo screenshot ritagliato del secondo schermo
    second_screen.show()

# Funzione per eseguire il ciclo con il controllo della tastiera
def main(stdscr):
    # Nasconde il cursore e imposta la modalità non bloccante
    curses.curs_set(0)
    stdscr.nodelay(1)  # Non bloccare l'input da tastiera
    stdscr.timeout(500)  # Imposta il timeout a 500ms (per evitare che il programma si blocchi)

    while True:
        capture_and_show()
        time.sleep(0.5)  # Aspetta 0.5 secondi

        # Controlla se la tecla 'Q' è stata premuta per uscire
        key = stdscr.getch()
        if key == ord('q'):  # Se premi 'Q', interrompi il ciclo
            print("Uscita... premiato Q")
            break

# Avvia il programma con curses
curses.wrapper(main)
