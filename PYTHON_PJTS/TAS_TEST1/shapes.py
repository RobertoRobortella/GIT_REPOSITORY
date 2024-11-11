import pygame
import math

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
