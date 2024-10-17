# Proyecto Pensamiento computacional para ingenieria
# Valeria Escalante A01709023

import random
# Importamos random para que la computadora elija un dato aleatorio 

""" Funcion para dar tips randoms despues de cada receta"""
def dar_tips():
    tips = [
        "Tip: Usa los igredientes a temp ambiente para mezclarlo mejor",
        "Tip: La azucar morena da mejor consistencia a algunas recetas",
        "Tip: Recuerda precalentar tu horn antes de hornear ",
        "¿Sabias que? La levadura se usa desde tiempos inmemoriables",
        "OJO primero junta tus solidas y luego incluye los humedos"
        ]
    # Crear una lista con tips 
    return random.choice(tips)
    # Pedirle a la computadora que elija una opcion random 
    # https://docs.python.org/es/3/library/random.html#random.choice
    


"""Funcion para calcular los gramos necesarios para cada receta"""
def calculo_ingredientes(unidades,ingredientes,unidades_receta_orginal):
    # Pide las unidades dependiendo de la cantidad del usuario
    # la lista de ingredientes
    # y las unidades que estan preestablecidas en la receta original
    
    resultado_calculos=[]
    # Crea una lista vacia donde pondremos los resultados de los calculos 
    
    for ingrediente in ingredientes: 
        # Se crea un ciclo for para repasar cada ingrediente en a lista
        
        nombre = ingrediente[0]
        cantidad_original = ingrediente[1]
        sistema_de_medicion = ingrediente[2]
        # Se le asigna una variable a los elementos de la lista en la lista
        
        cantidad_calculada = (cantidad_original/unidades_receta_orginal) \
        * unidades
        # dividir las cantidades originales entre las unidades por las que la
        # receta estaba hecha y luego multiplicar por el num de unidades que 
        # el usuario pida
        
        if cantidad_calculada < 1:
            cantidad_calculada = 1
            # Si la cantidad calculada es menor a uno redondearlo a 1 para 
            # evitar dimensiones demasiado pequeñas para cocinar 
         
        if cantidad_calculada > 1:
            sistema_de_medicion = sistema_de_medicion + "s"
            # Si la cantidad calculada es mas de uno volverlo plural 
            
        resultado_calculos.append([nombre,cantidad_calculada,\
        sistema_de_medicion])
        # Agregar todos los datos y calculos a la lista de resultados 
        
    return resultado_calculos
       

# Menu principal para elegir el tipo de cocina. Se repite infinitamente hasta
# que el usuario quiera salir"""
print("Bienvenide :)")
while True:
    
    print("Escribe la opcion que estas buscando")
    print("A Reposteria")
    print("B Panaderia")
    print("S Salir")
    opcion_menu_principal = input("Opcion: ")
    # Mostrar las opciones del menu y pedir una letra para la seleccion
    
    
    if opcion_menu_principal == "A" or opcion_menu_principal == "a":
        # Si la opcion es A entra al menu del espacio de reposteria 
        
        print("Este es el menu de reposteria")
        print("Escribe el numero de la receta que quieras cocinar")
        print("1 Galletas con chispas de chocolate")
        print("2 Galletas de mantequilla")
        opcion_menu_reposteria = input("Numero: ")
        # Mostrar las opciones del menu y pedir un numero para la seleccion
        
        if opcion_menu_reposteria == "1": 
            # Si la opcion es uno entra a la receta de galletas con chispas 
            
            unidades = int(input\
            ("¿Cuantas galletas de chispas de chocolate quieres hacer?\n"))
            # Determinar cuantas galletas se van a hacer para el calculo 
            
            ingredientes = [
                ["Harina", 300, "gramo"],  
                ["Chispas de chocolate", 400, "gramo"],
                ["Mantequilla", 460, "gramo"],
                ["Azúcar", 300, "gramo"],
                ["Nueces", 100, "gramo"],
                ["Vainilla", 1, "cucharadita"],  
                ["Huevos", 2, "huevo" ],  
                ["Bicarbonato", 1,"cucharadita"],  
                ["Sal", 1, "cucharadita"] 
                ]
            # Crear una lista con el nombre del ingrediente, la cantidad en la
            # receta y la forma en la que se mide 
                
            unidades_receta_orginal = 60 
            #Determinar para cuantas galletas eran en la receta original 
            
            for ingrediente in calculo_ingredientes(unidades,ingredientes,\
            unidades_receta_orginal):
                nombre = ingrediente[0]
                cantidad = ingrediente[1]
                sistema_de_medicion = ingrediente[2]
                
                print(nombre, ":",f"{cantidad:.0f}",sistema_de_medicion)
            # For para imprimir los resultados de manera mas ordenada 
            # Redondear el resultado para evitar mediciones demasiado pequeñas
            
            print(dar_tips())
            # Imprimir la funcion para poner un tip random 
            
            break 
            # Se cierra el ciclo while y con eso se termina el codigo 
           
             
            
            
            
        elif opcion_menu_reposteria == "2": 
         # Si la opcion es dos entra a la receta de galletas de matequilla    
        
            
            unidades = int(input\
            ("¿Cuantas galletas de matequilla quieres hacer?\n"))
            # Determinar cuantas galletas se van a hacer para el calculo 
            
            ingredientes = [
                ["Harina", 350, "gramo"],  
                ["Mantequilla", 100, "gramo"],
                ["Azúcar", 200, "gramo"],
                ["Vainilla", 1, "cucharadita"],  
                ["Huevos", 2, "huevo" ],  
                ["Bicarbonato", 1,"cucharadita"],  
                ]
            # Crear una lista con el nombre del ingrediente, la cantidad en la
            # receta y la forma en la que se mide 
                
            unidades_receta_orginal = 12 
            #Determinar para cuantas galletas eran en la receta original 
            
            for ingrediente in calculo_ingredientes(unidades,ingredientes,\
            unidades_receta_orginal):
                nombre = ingrediente[0]
                cantidad = ingrediente[1]
                sistema_de_medicion = ingrediente[2]
                
                print(nombre, ":",f"{cantidad:.0f}",sistema_de_medicion)
            # For para imprimir los resultados de manera mas ordenada 
            # Redondear el resultado para evitar mediciones demasiado pequeñas
            
            print(dar_tips())
            # Imprimir la funcion para poner un tip random 
            
            break 
            #Cierra el ciclo while y con eso termina el codigo 
            
        else: 
            print("Opcion invalida")
            # Si la respuesta por el usuario no es lo indicado se imprime
            # opcion invalida y se repite el codigo 
          
    elif opcion_menu_principal == "B" or opcion_menu_principal == "b":
        # Si la opcion es A entra al menu del espacio de panaderia 
        
        print("Este es el menu de panaderia")
        print("Escribe el numero de la receta que quieras cocinar")
        print("1 Croissants")
        print("2 Pan de Muerto")
        opcion_menu_reposteria = input("Numero: ")
        # Mostrar las opciones del menu y pedir un numero para la seleccion
        
        if opcion_menu_reposteria == "1": 
            # Si la opcion es uno entra a la receta de croissants 
            
            unidades = int(input("¿Cuantos croissants quieres hacer?\n"))
            # Determinar cuantos croissants se van a hacer para el calculo 
            
            ingredientes = [
                ["Harina", 1000, "gramo"],  
                ["Mantequilla", 640, "gramo"],
                ["Agua Fria", 520, "mililitro"],
                ["Azucar", 100, "gramo"], 
                ["Levadura", 22,"gramo"],  
                ["Sal", 18, "gramo"] 
                ]
            # Crear una lista con el nombre del ingrediente, la cantidad en la
            # receta y la forma en la que se mide 
                
            unidades_receta_orginal = 30 
            #Determinar para cuantos croissants eran en la receta original 
            
            for ingrediente in calculo_ingredientes(unidades,ingredientes,\
            unidades_receta_orginal):
                nombre = ingrediente[0]
                cantidad = ingrediente[1]
                sistema_de_medicion = ingrediente[2]
                
                print(nombre, ":",f"{cantidad:.0f}",sistema_de_medicion)
            # For para imprimir los resultados de manera mas ordenada
            # Redondear el resultado para evitar mediciones demasiado pequeñas
            
            print(dar_tips())
            # Imprimir la funcion para poner un tip random 
            
            break 
            # Se cierra el ciclo while y con eso se termina el codigo 
           
            
        elif opcion_menu_reposteria == "2": 
         # Si la opcion es dos entra a la receta de pan de muerto     
        
            
            unidades = int(input\
            ("¿Cuantos panes de muerto quieres hacer?\n"))
            # Determinar cuantos panes se van a hacer para el calculo 
            
            ingredientes = [
                ["Harina", 250, "gramo"],  
                ["Mantequilla", 105, "gramo"],
                ["Azúcar", 250, "gramo"],
                ["Vainilla", 1, "cucharadita"], 
                ["Sal", 4, "gramo"],
                ["Huevos", 3, "huevo" ],  
                ["Jugo de naranja", 2,"cucharada"],
                ["Agua de Azahar", 1, "cucharadita"]
                ]
            # Crear una lista con el nombre del ingrediente, la cantidad en la
            # receta y la forma en la que se mide 
                
            unidades_receta_orginal = 6
            #Determinar para cuantos panes eran en la receta original 
            
            for ingrediente in calculo_ingredientes(unidades,ingredientes,\
            unidades_receta_orginal):
                nombre = ingrediente[0]
                cantidad = ingrediente[1]
                sistema_de_medicion = ingrediente[2]
                
                print(nombre, ":",f"{cantidad:.0f}",sistema_de_medicion)
            # For para imprimir los resultados de manera mas ordenada

            print(dar_tips())
            # Imprimir la funcion para poner un tip random 
            
            break 
            #Cierra el ciclo while y con eso termina el codigo
            
    
            
        else: 
            print("Opcion invalida")
            # Si la respuesta por el usuario no es lo indicado se imprime
            # opcion invalida y se repite el codigo             
            
    elif opcion_menu_principal == "S" or opcion_menu_principal == "s":
        break
        #Si se escribe s se termina el codigo cerrando el ciclo 
        
    else: 
        print("Opcion invalida")
        # Si la respuesta por el usuario no es lo indicado se imprime
        # opcion invalida y se repite el codigo 
