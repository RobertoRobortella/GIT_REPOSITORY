import pygame
from shapes import shape1, shape2  # Importa le funzioni di disegno

# Inizializza pygame
pygame.init()

# Impostazioni della finestra
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forme Mobili con Pygame")

# Colore sfondo
background_color = (0, 0, 0)

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
