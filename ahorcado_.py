import pygame
import random
import sys

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Ahorcado")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "juego", "computadora", "aprendizaje"]
    return random.choice(palabras)

def mostrar_tablero(intentos):
    partes_cuerpo = [
        (100, 100, 50, 50),      # Cabeza
        (125, 150, 10, 100),     # Cuerpo
        (90, 150, 50, 10),       # Brazos
        (130, 150, 50, 10),      # Brazos
        (100, 200, 10, 100),     # Piernas
        (120, 200, 10, 100)      # Piernas
    ]

    for i in range(intentos):
        pygame.draw.rect(PANTALLA, NEGRO, partes_cuerpo[i])

def main():
    pygame.init()
    palabra_secreta = seleccionar_palabra()
    palabra_adivinada = ["_"] * len(palabra_secreta)
    intentos = 0
    letras_intentadas = []

    fuente = pygame.font.Font(None, 36)
    mensaje = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.fill(BLANCO)

        mostrar_tablero(intentos)

        palabra_mostrada = " ".join(palabra_adivinada)
        palabra_render = fuente.render(palabra_mostrada, True, NEGRO)
        PANTALLA.blit(palabra_render, (ANCHO // 2 - palabra_render.get_width() // 2, 400))

        letras_intentadas_render = fuente.render(", ".join(letras_intentadas), True, NEGRO)
        PANTALLA.blit(letras_intentadas_render, (ANCHO // 2 - letras_intentadas_render.get_width() // 2, 450))

        pygame.display.flip()

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_intentadas:
            mensaje = "Ya intentaste esa letra."
        else:
            letras_intentadas.append(letra)
            if letra in palabra_secreta:
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        palabra_adivinada[i] = letra
            else:
                intentos += 1

        if "_" not in palabra_adivinada:
            mensaje = "¡Ganaste! La palabra era: " + palabra_secreta
            break

        if intentos >= 6:
            mensaje = "¡Perdiste! La palabra era: " + palabra_secreta
            break

        fuente_mensaje = pygame.font.Font(None, 48)
        mensaje_render = fuente_mensaje.render(mensaje, True, NEGRO)
        PANTALLA.blit(mensaje_render, (ANCHO // 2 - mensaje_render.get_width() // 2, 100))
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()
