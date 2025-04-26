# Importa el módulo assistant, que contiene funciones de voz como 'speak' y 'listen'
import assistant
# Importa el módulo carwash, que debe estar en el mismo directorio (carwash.py contiene la lógica del negocio)
import carwash  

# Función principal que mantiene el programa en ejecución continua hasta que el usuario decida salir
def show():
    while True:  # Bucle infinito hasta que el usuario diga "salir"
        action = welcome_menu()  # Muestra el menú de opciones y obtiene la acción del usuario

        if action == 'ingreso':
            carwash.register_entry()  # Registra el ingreso de un vehículo
        elif action == 'egreso':
            carwash.register_exit()  # Registra la salida de un vehículo
        elif action == 'estadisticas':
            carwash.show_stats()  # Muestra estadísticas del día
        elif action == 'salir':
            # Despedida con voz y salida del bucle
            assistant.speak("Me dio gusto acompañarte el día de hoy. ¡Hasta luego!")
            print("Me dio gusto acompañarte el día de hoy. ¡Hasta luego!")
            break  

# Función que presenta el menú de opciones mediante voz y espera de voz hablada del usuario
def welcome_menu():
    assistant.speak("Hola, soy tu asistente de voz del lavaautos LAVA YA")  # Saludo
    assistant.speak("¿Qué deseas hacer hoy? Por favor, elige una opción:")

    # Enumera las opciones disponibles
    assistant.speak("1. Registrar el ingreso de un vehículo.")
    assistant.speak("2. Registrar la salida de un vehículo.")
    assistant.speak("3. Ver las estadísticas del día.")
    assistant.speak("4. Salir.")

    response = assistant.listen().lower()  # Escucha la respuesta del usuario y la convierte a minúsculas

    # Mapeo de la respuesta a una acción específica (reconoce números y palabras clave)
    if 'uno' in response or '1' in response or 'ingreso' in response:
        return 'ingreso'
    elif 'dos' in response or '2' in response or 'egreso' in response:
        return 'egreso'
    elif 'tres' in response or '3' in response or 'estadísticas' in response:
        return 'estadisticas'
    elif 'cuatro' in response or '4' in response or 'salir' in response:
        return 'salir'
    else:
        # Si no se entendió la respuesta, se informa al usuario y se repite el menú
        assistant.speak("No entendí tu respuesta. Por favor, intenta de nuevo.")
        print("No entendí tu respuesta. Por favor, intenta de nuevo.")
        return welcome_menu()  # Volver a mostrar el menú
