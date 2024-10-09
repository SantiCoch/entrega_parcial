
def cargar_pacientes(pacientes):
    """Esta función permite ingresar datos de pacientes en la lista 'pacientes'
    
    Pregunta cuantos pacientes se van a registrar y pide los datos de cada uno.
    Luego, agrega la información a la lista

    """
    n = int(input("Ingrese la cantidad de pacientes a registrar: "))
    for _ in range(n):
        historia_clinica = int(input("Ingrese el numero de historia clinica: "))
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnostico del paciente: ")
        dias_internacion = int(input("Cantidad de dias de internacion: "))
        pacientes.append([historia_clinica, nombre, edad, diagnostico, dias_internacion])

def buscar_paciente(pacientes, historia_clinica):
    """
    Busca un paciente en la lista usando el numero de historia clínica.

    Si no hay pacientes, informa que la lista esta vacía
    Si lo encuentra, devuelve los datos del paciente: SI no, indica que no se encontró.
    
    """
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            return pacientes
    return None

def ordenar_pacientes(pacientes):
    """
    Ordena la lista de pacientes por el numero de historia clínica.

    Usa el ordenamiento de burbuja para reorganizar los pacientes
    
    """

    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) - i - 1):
            if pacientes[j][1] > pacientes[j + 1][1]: 
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    print("Pacientes ordenados por historia clinica")

def mostrar_max_dias(pacientes):
    """
    Muestra el paciente que tiene mas dias de internación.

    Si no hay pacientes, indica que la lista esta vacía

    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    max_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > max_paciente[4]:
            max_paciente = paciente
    print(f"Paciente con mas dias de internacion: {max_paciente}")



def mostrar_min_dias(pacientes):
    """
    Muestra el paciente que tiene menos dias de internación

    Si no hay pacientes, indica que la lista esta vacía

    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    min_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > min_paciente[4]:
            min_paciente = paciente
    print(f"Paciente con menos dias de internacion: {min_paciente}")


def mostrar_pacientes_mas_5_dias(pacientes):
    """
    Muestra todos los pacientes con mas de 5 días de internación

    Si no hay pacientes, informa que la lista está vacía
    """

    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("Pacientes con mas de 5 dias de internación:")
    for paciente in pacientes:
        if paciente in pacientes:
            if paciente[4] > 5:
                print(f"Historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Dias de internacion: {paciente[4]}")



def mostrar_todos_los_pacientes(pacientes):
    """
    Muestra todos los pacientes registrados en el sistema

    Si no hay pacientes, indica que la lista esta vacía

    """
    if not pacientes:
        print("No hay productos disponibles.")
        return
    print("Lista de todos los pacientes registrados")
    for paciente in pacientes:
        print(f"Historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de internacion: {paciente[4]}")


def promedio_dias_internacion(pacientes):
    """
    Calcula y muestra el promedio de días de intervención de todos los pacientes

    Si no hay pacientes, indica que la lista esta vacía
    
    """

    if not pacientes:
        print("No hay pacientes registrados")
        return
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    promedio = total_dias / len(pacientes)
    print(f"Promedio de dias de internacion: {promedio}")



def menu():

    """
    Muestra el menú principal del codigo y permite el usuario poder elegir entre:
    Cargar pacientes, buscar, ordenar y mostrar información sobre ellos.
    
    """
    pacientes = []
    continuar = True  
    
    while continuar:
        print("Menú Principal")
        print("1. Cargar pacientes")
        print("2. Buscar paciente por historia clinica")
        print("3. Ordenar pacientes por historia clinica")
        print("4. Mostrar pacientes con mas dias de internacion ")
        print("5. Mostrar pacientes con menos dias de internacion")
        print("6. Cantidad de pacientes con mas de 5 dias de internacion")
        print("7. Mostrar todos los pacientes")
        print("8. Promedio de dias de internacion de todos los pacientes")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cargar_pacientes(pacientes)
        elif opcion == '2':
            historial_clinica = input("Ingrese el numero de historia clinica a buscar: ")
            paciente = buscar_paciente(pacientes, historial_clinica)
            if paciente:
                print(f"Paciente encontrado: {paciente}")
            else:
                print("Paciente no encontrado.")
        elif opcion == '3':
            ordenar_pacientes(pacientes)
        elif opcion == '4':
            mostrar_max_dias(pacientes)
        elif opcion == '5':
            mostrar_min_dias(pacientes)
        elif opcion == '6':
            mostrar_pacientes_mas_5_dias(pacientes)
        elif opcion == "7":
            mostrar_todos_los_pacientes(pacientes)
        elif opcion == '8':
            promedio_dias_internacion(pacientes)
        elif opcion == '9':
            print("Saliendo del menú...")
            continuar = False 
        else:
            print("Opcion invalida. Intente nuevamente.")

menu()

