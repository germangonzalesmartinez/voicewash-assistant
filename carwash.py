# Se importa el módulo 'assistant' que maneja la interacción por voz
import assistant

# Listas en memoria para registrar vehículos que han ingresado y salido
vehicles_in = []   # Lista de vehículos actualmente en el lavaautos
vehicles_out = []  # Lista de vehículos que ya salieron del lavaautos

# Función para registrar el ingreso de un vehículo
def register_entry():
    assistant.speak("Por favor, dime la placa del vehículo que ingresa.")
    plate = assistant.listen().upper()  # Escucha y convierte la placa a mayúsculas
    spelled_plate = assistant.spell_out(plate)  # Deletrea la placa para claridad al usuario

    # Verifica si el vehículo ya está registrado como ingresado
    if any(vehicle['plate'] == plate for vehicle in vehicles_in):
        assistant.speak(f"El vehículo con placa {spelled_plate} ya se encuentra en proceso de lavado en el lavaautos LAVA YA.")
        print(f"El vehículo con placa {spelled_plate} ya se encuentra en proceso de lavado en el lavaautos LAVA YA.")
        return  # Finaliza si ya está ingresado

    # Si no está registrado, pide el nombre del propietario
    assistant.speak("Ahora, por favor dime el nombre del propietario.")
    owner = assistant.listen().title()  # Escucha y convierte el nombre a formato título

    # Crea el registro del vehículo y lo añade a la lista de ingresados
    vehicle = {"plate": plate, "owner": owner}
    vehicles_in.append(vehicle)

    spelled_plate = assistant.spell_out(plate)  # Vuelve a deletrear la placa para confirmación
    assistant.speak(f"Vehículo con placa {spelled_plate} y propietario {owner} registrado exitosamente para lavado.")

    print(f"Vehículo con placa {spelled_plate} y propietario {owner} registrado exitosamente para lavado.")

# Función para registrar la salida de un vehículo
def register_exit():
    assistant.speak("Por favor, dime la placa del vehículo que va a salir.")
    plate = assistant.listen().upper()  # Escucha y convierte a mayúsculas
    spelled_plate = assistant.spell_out(plate)  # Vuelve a deletrear la placa para confirmación

    # Busca el vehículo en la lista de ingresados
    vehicle = next((v for v in vehicles_in if v['plate'] == plate), None)
    
    if vehicle:
        vehicles_in.remove(vehicle)      # Lo elimina de la lista de ingresados
        vehicles_out.append(vehicle)     # Lo agrega a la lista de salidos
        assistant.speak(f"Vehículo con placa {spelled_plate} ha salido del lavaautos. ¡Hasta pronto!")
        print(f"Vehículo con placa {spelled_plate} ha salido del lavaautos. ¡Hasta pronto!")
    else:
        assistant.speak(f"No encontré el vehículo con placa {spelled_plate} en el sistema.")  # Si no se encuentra
        print(f"No encontré el vehículo con placa {spelled_plate} en el sistema.")

# Función para mostrar las estadísticas del día
def show_stats():
    total = len(vehicles_in) + len(vehicles_out)  # Total de vehículos registrados hoy

    if total == 0:
        assistant.speak("No hay vehículos registrados hoy.")  # Si no hay datos
        print("No hay vehículos registrados hoy.")
        return

    # Calcula los porcentajes de vehículos en el sitio y los que ya salieron
    percent_in = (len(vehicles_in) / total) * 100
    percent_out = (len(vehicles_out) / total) * 100

    # Informa los resultados con voz
    assistant.speak(f"Actualmente hay {len(vehicles_in)} vehículos en el lavaautos, lo que representa el {percent_in:.2f}% del total.")
    print(f"Actualmente hay {len(vehicles_in)} vehículos en el lavaautos, lo que representa el {percent_in:.2f}% del total.")
    assistant.speak(f"{len(vehicles_out)} vehículos ya han salido, equivalente al {percent_out:.2f}%.")
    print(f"{len(vehicles_out)} vehículos ya han salido, equivalente al {percent_out:.2f}%.")

