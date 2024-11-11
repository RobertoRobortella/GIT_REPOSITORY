import Jetson.GPIO as GPIO
import time
import random  # Per variare il BPM in modo casuale

# Configura il pin GPIO per emulare la trasmissione seriale
GPIO.setmode(GPIO.BCM)  # Usa la numerazione BCM (canali Broadcom)
GPIO.setup(17, GPIO.OUT)  # Pin GPIO 17 per l'uscita

def send_midi_message(message):
    """Funzione per inviare un messaggio MIDI."""
    for byte in message:
        for bit in range(8):
            # Inverte il bit (logica negativa per MIDI)
            GPIO.output(17, not ((byte >> (7 - bit)) & 1))
            time.sleep(1 / 31250)  # 31250 baud per MIDI

def calculate_note_duration(bpm):
    """Calcola la durata di una nota in millisecondi in base al BPM."""
    return 60 * 1000 / bpm  # Durata di un battito in ms

def play_sequence(bpm):
    """Riproduce una sequenza di note con un BPM variabile in loop."""
    # Sequenza di note MIDI (Note On / Off per ogni nota)
    notes = [
        [0x90, 0x3C, 0x7F],  # Nota C4, velocity 127 (Note On)
        [0x80, 0x3C, 0x00],  # Nota C4, velocity 0 (Note Off)
        [0x90, 0x3E, 0x7F],  # Nota D4
        [0x80, 0x3E, 0x00],  # Nota D4
        [0x90, 0x40, 0x7F],  # Nota E4
        [0x80, 0x40, 0x00],  # Nota E4
        [0x90, 0x41, 0x7F],  # Nota F4
        [0x80, 0x41, 0x00],  # Nota F4
    ]
    
    # Calcola la durata di una nota in base al BPM
    note_duration = calculate_note_duration(bpm)
    
    # Calcola il tempo totale per un ciclo di 4 battiti (in millisecondi)
    total_cycle_duration = note_duration * 4  # 4 note in 4/4
    
    while True:
        start_time = time.time()  # Memorizza l'inizio del ciclo
        
        # Ripete ciclicamente la sequenza di note
        for note in notes:
            send_midi_message(note)  # Invia la nota
            time.sleep(note_duration / 1000)  # Aspetta per la durata della nota

            # Calcola il tempo di attesa per mantenere il BPM costante
            elapsed_time = time.time() - start_time
            remaining_time = total_cycle_duration - elapsed_time
            if remaining_time > 0:
                time.sleep(remaining_time / 1000)  # Aspetta il tempo residuo per completare il ciclo

# Funzione principale
def main():
    try:
        # Imposta un BPM variabile (per esempio tra 90 e 150)
        bpm = random.randint(90, 150)
        print(f"Avvio con BPM: {bpm}")

        # Esegui la sequenza di note ciclicamente
        play_sequence(bpm)
    
    except KeyboardInterrupt:
        print("Esecuzione interrotta.")
    finally:
        # Pulisci la configurazione dei pin GPIO quando il programma termina
        GPIO.cleanup()

if __name__ == "__main__":
    main()
