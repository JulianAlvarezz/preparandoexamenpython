bandas = []  # Lista de bandas
contador_id = 1  # Inicializamos el contador de ID en 1

# Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:

    print("1. Registrar Banda")
    print("2. Buscar Informacion de la Banda")
    print("3. Agenda del Evento")
    print("4. Modificar una Banda")
    print("5. Salir")
    print("6. Eliminar una Banda")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        banda = {}  # Crear un diccionario para almacenar los datos de la banda
        
        # Asignamos el ID utilizando el contador_id y luego incrementamos el contador
        banda["id"] = contador_id
        contador_id += 1

        banda["nombre"] = input("Nombre de la Banda: ")
        banda["genero"] = input("Tipo de Genero: ")
        banda["clasificacion"] = input("Clasificacion: ")
        banda["tiempo"] = int(input("Tiempo: "))
        banda["costo"] = int(input("Costo: $"))

        # Agregar el diccionario de banda a la lista de bandas
        bandas.append(banda)
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    elif opcion == 2:
        # Buscar información de la banda por nombre
        bandaBuscar = input("Digita el nombre de la banda que desea buscar: ").upper()  # Convertimos a Convertimos a mayúsculas
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"].upper() == bandaBuscar:  # Convertimos a minúsculas para comparar
                # Mostrar los datos de la banda encontrada
                print(f"id {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
   
                break  # Detener la búsqueda después de encontrar la primera coincidencia
        else:
            print("No se encuentra la banda.")
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    elif opcion == 3:
        print(bandas)
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    elif opcion == 4:
        # Buscar la banda por nombre
        nombre_modificar = input("Digita el nombre de la banda que desea modificar: ").upper()  # Convertimos a mayúsculas
        for banda in bandas:
            if banda["nombre"].upper() == nombre_modificar:  # Convertimos a mayúsculas para comparar
                print("Seleccione qué información desea modificar:")
                print("1. Nombre de la Banda")
                print("2. Tipo de Genero")
                print("3. Clasificacion")
                print("4. Tiempo")
                print("5. Costo")
                opcion_modificacion = int(input("Digite una opcion: "))

                if opcion_modificacion == 1:
                    nueva_nombre = input("Nuevo nombre de la Banda: ").upper()  # Convertimos a mayúsculas
                    banda["nombre"] = nueva_nombre
                elif opcion_modificacion == 2:
                    nueva_genero = input("Nuevo tipo de Genero: ")
                    banda["genero"] = nueva_genero
                elif opcion_modificacion == 3:
                    nueva_clasificacion = input("Nueva clasificacion: ")
                    banda["clasificacion"] = nueva_clasificacion
                elif opcion_modificacion == 4:
                    nuevo_tiempo = int(input("Nuevo tiempo: "))
                    banda["tiempo"] = nuevo_tiempo
                elif opcion_modificacion == 5:
                    nuevo_costo = int(input("Nuevo costo: "))
                    banda["costo"] = nuevo_costo
                else:
                    print("Opción inválida.")
                print("Banda modificada correctamente.")
                break
        else:
            print("No se encontró ninguna banda con el nombre proporcionado.")
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    elif opcion == 5:
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    elif opcion == 6:
        id_eliminar = int(input("Digite el ID de la banda que desea eliminar: "))
        for i, banda in enumerate(bandas):
            if banda["id"] == id_eliminar:
                del bandas[i]
                print("Banda eliminada correctamente.")
                break
        else:
            print("No se encontró ninguna banda con el ID proporcionado.")
        print()
        print("Muchas gracias por utilizar el servicio")
        print()
    else:
        print("Opción no válida.")
