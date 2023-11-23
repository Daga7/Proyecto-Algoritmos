import random
import time 

# Lista de preguntas con opciones y respuestas correctas
preguntas = [
    {
        "enunciado": "¿Cuál es la capital de Francia?",
        "opciones": ["Madrid", "Berlín", "París", "Londres"],
        "respuesta_correcta": "París"
    },
    {
        "enunciado": "¿En qué año fue la independencia de Estados Unidos?",
        "opciones": ["1776", "1789", "1801", "1850"],
        "respuesta_correcta": "1776"
    },
    {
        "enunciado": "¿En que año sucedió el desastre de Chernobyl?",
        "opciones": ["1776" , "2000" , "1986" , "1980"],
        "respuesta_correcta":"1986"    
    },
    {
        "enunciado": "¿Cuál es la estrella que está más cerca de nuestro planeta Tierra? ",
        "opciones": ["Centauri" , "Sirio" , "Luyten" , "Sol"],
        "respuesta_correcta":"Centauri" 
    },
    {
        "enunciado": "¿En qué año asesinaron a John F. Kennedy? ",
        "opciones": ["1989" , "1961" , "1962" , "1963"],
        "respuesta_correcta":"1963" 
    },
    {
        "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin" 
    },
    {#
        "enunciado": "¿En que año aterrizo el apolo 11 en lal luna? ",
        "opciones": ["1969" , "1970" , "1968" , "1967"],
        "respuesta_correcta":"1969" 
    },
    {
        "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin" 
    },
    {
        "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin" 
    },
    {
        "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin" 
    },
    {
      "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin"   
    },
    {
      "enunciado": "¿Cómo se llama a la lengua oficial china? ",
        "opciones": ["Chino" , "Mandarin" , "Nipon" , "Nihogo"],
        "respuesta_correcta":"Mandarin"   
    }
]

import time
hola="hola"
def mensaje_centrado(texto):
    # Obtén el ancho de la terminal actual
    terminal_ancho = 160
    # Calcula en blanco
    espacio_en_blanco = (terminal_ancho - len(texto)) // 2

    # Imprime el espacio en blanco antes del mensaje
    print(" " * espacio_en_blanco, end='')

    # Muestra cada letra con un intervalo de tiempo
    for letra in texto:
        print(letra, end='', flush=True)  
    # Salto de línea al final
    print()

# Uso
mensaje = "Bienvenidos a ¿quien quiere ser millonario?"
mensaje_centrado(mensaje)

# Diccionario para almacenar puntajes de jugadores
puntajes = {}

def mostrar_instrucciones():
    print("Responde correctamente y acumula puntos.")
    print("Al final del juego, podrás ver tu puntaje.")
    print("\n")

def obtener_nombre():
    return input("Ingresa tu nombre completo: ")

def mostrar_menu():
    print("MENU:")
    print("1. Iniciar juego")
    print("2. Mirar puntajes")
    print("3. Salir")

def jugar():
    puntaje = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {pregunta['enunciado']}")
        
        for j, opcion in enumerate(pregunta['opciones'], 1):
            print(f"  {j}. {opcion}")

        inicio_tiempo = time.time()
        respuesta_usuario = input("Tu respuesta (ingresa el número de la opción): ")
        fin_tiempo = time.time()

        tiempo_transcurrido = fin_tiempo - inicio_tiempo

        if tiempo_transcurrido > 10:
            print("¡Tiempo agotado! La respuesta se considera incorrecta.\n")
        elif pregunta['opciones'][int(respuesta_usuario) - 1] == pregunta['respuesta_correcta']:
            print("¡Correcto! Ganaste 5 puntos.\n")
            puntaje += 5
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta_correcta']}\n")

    return puntaje

def mostrar_puntajes():
    print("PUNTAJES:")
    for nombre, puntaje in puntajes.items():
        print(f"{nombre}: {puntaje} puntos")
    print("\n")

# Programa principal
mostrar_instrucciones()

while True:
    nombre_jugador = obtener_nombre()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            puntaje_jugador = jugar()
            puntajes[nombre_jugador] = puntaje_jugador
            print(f"¡Fin del juego! Tu puntaje total es: {puntaje_jugador} puntos.\n")
            break
        elif opcion == "2":
            mostrar_puntajes()
        elif opcion == "3":
            exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    nuevo_jugador = input("¿Quieres comenzar como un nuevo jugador? (s/n): ")
    if nuevo_jugador.lower() != 's':
        mostrar_menu()  # Agregado para mostrar el menú después del juego
        opcion_despues_juego = input("Selecciona una opción (1-3): ")

        if opcion_despues_juego == "2":
            mostrar_puntajes()
        elif opcion_despues_juego == "3":
            exit()
        else:
            print("Opción no válida. Volviendo al menú principal.")
        break
        
