import pygame
import math

# Inizializza pygame
pygame.init()

# Impostazioni della finestra
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forme Mobili con Pygame")

# Colore sfondo
background_color = (0, 0, 0)

# Funzione per disegnare una forma (esempio)
def shape1(screen, x, y, A, B, C, F1, F2, F3, enabled):
    if enabled:
        time = pygame.time.get_ticks() / 1000  # Tempo in secondi
        radius = int(A * math.sin(F1 * time) + B * math.cos(F2 * time) + C)
        radius = max(5, abs(radius))  # Assicura che il raggio sia positivo e maggiore di 5
        color = (255, 0, 0)  # Rosso
        pygame.draw.circle(screen, color, (x, y), radius)

def shape2(screen, x, y, A, B, C, F1, F2, F3, enabled):
    if enabled:
        time = pygame.time.get_ticks() / 1000
        size = int(A * math.sin(F1 * time) + B * math.cos(F2 * time) + C)
        size = max(10, abs(size))  # Assicura che la dimensione sia positiva e maggiore di 10
        color = (0, 255, 0)  # Verde
        pygame.draw.rect(screen, color, (x - size // 2, y - size // 2, size, size))

# Funzione principale
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(background_color)  # Riempie lo sfondo con il colore nero

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Disegna le forme se abilitate
        shape1(screen, 400, 300, 50, 30, 20, 1, 0.5, 0.25, enabled=True)
        shape2(screen, 200, 150, 40, 25, 15, 0.8, 0.6, 0.3, enabled=False)

        # Aggiungi altre forme qui se necessario

        pygame.display.flip()  # Aggiorna la finestra
        clock.tick(60)  # Limita a 60 fotogrammi al secondo

    pygame.quit()

if __name__ == "__main__":
    main()
