bandas = []     #lista
      #objeto

#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("************************")

opcion = 100
while(opcion != 5):
    
    print("1. Registrar Banda")
    print("2. Buscar Informacion de la Banda")
    print("3. Agenda del Evento")
    print("4. Modificar una Banda")
    print("5. Salir")                
    opcion=int(input("Digita una opcion: "))
    
    if opcion == 1:
        banda={}  
        #Crear los datos del diccionario
        banda["id"]=int(input("Digite el ID:  "))
        banda["nombre"]=(input("Nombre de la Banda:  "))
        banda["genero"]=(input("Tipo de Genero:  "))
        banda["clasificacion"]=(input("Clasificacion:  "))
        banda["tiempo"]=int(input("Tiempo:  "))
        banda["costo"]=int(input("Costo: $  "))
        
        # Agregando un diccionario a una lista
        bandas.append(banda)
        
        
    elif opcion ==2:
    
        bandaBuscar=input("Digita el nombre de la banda que desea buscar:  ")
        for bandAuxiliar in bandas:
            if bandAuxiliar ["nombre"]==bandAuxiliar:
                # MOSTRAR EL DATO DE LA BANDA bandAuxiliar
                print(f "id {bandAuxiliar["id"]} --- nombre: {bandAuxiliar["nombre"]}")
            else:
                print("No se encuentra......")
             
    
    elif opcion ==3:
        print (bandas)
    elif opcion ==4:
        pass
    elif opcion ==5:
        pass
    else:
        pass
    #print"Gracias por utilizar el servicio"