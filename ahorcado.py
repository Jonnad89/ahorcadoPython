import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "juego", "computadora", "aprendizaje"]
    return random.choice(palabras)

def mostrar_tablero(intentos):
    partes_cuerpo = [
        " O ",
        "/|\\",
        "/ \\"
    ]
    
    print(" +---+")
    print(" |   |")
    print(f" {partes_cuerpo[intentos >= 1]}")
    print(f"{partes_cuerpo[intentos >= 3]}{partes_cuerpo[intentos >= 2]}{partes_cuerpo[intentos >= 4]}")
    print(" |")
    print("=====")

def main():
    palabra_secreta = seleccionar_palabra()
    palabra_adivinada = ["_"] * len(palabra_secreta)
    intentos = 0
    letras_intentadas = []
    
    print("¡Bienvenido al juego del ahorcado!")
    
    while True:
        mostrar_tablero(intentos)
        print("Palabra: " + " ".join(palabra_adivinada))
        print("Letras intentadas: " + ", ".join(letras_intentadas))
        
        letra = input("Ingresa una letra: ").lower()
        
        if letra in letras_intentadas:
            print("Ya intentaste esa letra.")
            continue
        
        letras_intentadas.append(letra)
        
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1
        
        if "_" not in palabra_adivinada:
            mostrar_tablero(intentos)
            print("¡Ganaste! La palabra era: " + palabra_secreta)
            break
        
        if intentos >= 5:
            mostrar_tablero(intentos)
            print("¡Perdiste! La palabra era: " + palabra_secreta)
            break

if __name__ == "__main__":
    main()
