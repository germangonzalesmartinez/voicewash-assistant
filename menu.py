import assistant
import carwash  

def show():
    action = welcome_menu()

    if action == 'ingreso':
        carwash.register_entry()
    elif action == 'egreso':
        carwash.register_exit()
    elif action == 'estadisticas':
        carwash.show_stats()


def welcome_menu():
    assistant.speak("Hola, soy tu asistente de voz del lavaautos LAVA YA")
    assistant.speak("¿Qué deseas hacer hoy? Por favor, elige una opción:")

    assistant.speak("1. Registrar el ingreso de un vehículo.")
    assistant.speak("2. Registrar el egreso de un vehículo.")
    assistant.speak("3. Ver las estadísticas del día.")
    assistant.speak("4. Consultar el estado de un vehículo por su placa")


    response = assistant.listen().lower()

    if 'uno' in response or '1' in response or 'ingreso' in response:
        return 'ingreso'
    elif 'dos' in response or '2' in response or 'egreso' in response:
        return 'egreso'
    elif 'tres' in response or '3' in response or 'estadísticas' in response:
        return 'estadisticas'
    else:
        assistant.speak("No entendí tu respuesta. Por favor, intenta de nuevo.")
        return welcome_menu()
