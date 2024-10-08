# Este codigo es el proyecto de la clase de programación 
# Reposteria Automatizada :P

#Medidas en gramos 

#0123456789012345678901234567890123456789012345678901234567890123456789

"""Determine las cantidades en gramos de cada ingrediente"""

TAZA_HARINA_G = float(150)
TAZA_CHISPAS_G = float(200)
BARRA_MANTEQUILLA_G = float(230)
TAZA_AZUCAR_G = float(200)
HUEVO = int(1)
CUCHARADITA = int(1)
CUCHARADITA_GRAM = float(5)
TAZA_NUECES = float(100)
TAZA_AGUA = float(250)
TAZA_ACEITE_ML = float (200)
TAZA_LECHE_CONDENSADA = float (300)
TAZA_LECHE_ML = float (250)

    
"""Hice un menu para que eligieran lo que querian cocinar y dento de cada opcion del menu 
hay recetas que pueen elegir"""
#Menu 
while True: 
    print("Bienvenido/a \nEscribe la opcion que estas buscando")
    opciones_cocina = input (" A. Reposteria B. Panaderia C. Pasteleria \n")
#Espacio de reposteria
    if opciones_cocina == "A" or opciones_cocina == "a": 
        print("Este es el menu de reposteria\nEscribe el numero de la receta \n")
        recetas_reposteria = input("1. Galletas de chispas")
        if recetas_reposteria == "1":
            """Con una receta de 60 galletas cada ingrediente se multiplica por los parametros
dados en la receta y luego se divide por las 60 unidades para luego multiplicarlo por
el numero de unidades dadas por el usuario """
            print("Receta de galletas de chispas de chocolates")
            # Lista anidada para almacenar ingredientes y sus cantidades base
            ingredientes_galletas = [
                ["Harina", 300],  # En gramos
                ["Chispas de chocolate", 400],
                ["Mantequilla", 460],
                ["Azúcar", 300],
                ["Nueces", 100]
                ]

            ingredientes_enteros_galletas = [
                ["Vainilla", 1],  # En cucharaditas
                ["Huevos", 2],  # En unidades
                ["Bicarbonato", 1],  # Cucharaditas
                ["Sal", 0.5]  # Cucharaditas
                ]

            # Función para calcular las cantidades en gramos
            def medida_gramos_galletas(cantidad_galletas):
                proporciones = cantidad_galletas / 60  # Calcula la proporción en base a 60 galletas
                cantidades_totales_galletas = []  # Lista vacía para guardar las cantidades finales

                # Recorrer la lista de ingredientes
                for ingrediente in ingredientes_galletas:
                    nombre = ingrediente[0]  # El nombre del ingrediente (ej. "Harina")
                    cantidad_base = ingrediente[1]  # La cantidad base del ingrediente (ej. 300 gramos)

                    # Calcular la cantidad ajustada
                    cantidad_ajustada = cantidad_base * proporciones

                    # Añadir el ingrediente y la cantidad ajustada a la lista final
                    cantidades_totales_galletas.append([nombre, cantidad_ajustada])

                return cantidades_totales_galletas

            # Función para calcular los ingredientes enteros
            def medida_enteros_galletas(cantidad_galletas):
                if cantidad_galletas >= 60:
                    factor = cantidad_galletas // 60
                elif cantidad_galletas >= 30:
                    factor = 1
                else:
                    factor = 0.5
                cantidades_totales_enteros = [
                    [ingrediente[0], ingrediente[1] * factor] for ingrediente in ingredientes_enteros_galletas
                    ]
                return cantidades_totales_enteros

            # Recibe la cantidad de galletas que el usuario quiere hacer
            cantidad_galletas = float(input("¿Cuántas galletas quieres hacer? \n"))

            # Calcula las cantidades necesarias
            cantidades_galletas = medida_gramos_galletas(cantidad_galletas)
            cantidades_enteros = medida_enteros_galletas(cantidad_galletas)

            # Mostrar resultados
            print(f"Estos son los ingredientes en gramos para {cantidad_galletas} galletas:")
            for ingrediente in cantidades_galletas:
                print(f"{ingrediente[1]:.2f} gramos de {ingrediente[0]}")
            for ingrediente in cantidades_enteros:
                print(f"{ingrediente[1]:.2f} cucharaditas de {ingrediente[0]}")

                break
        
    
#Espacio de panaderia
    if opciones_cocina == "B" or opciones_cocina == "b": 
        print("Este es el menu de panaderia\nEscribe el numero de la receta \n")
        recetas_reposteria = input("1. Croissant: ")
        if recetas_reposteria == "1":
            print("Receta de croissant")
            cantidad_croissants = float( input("¿Cuantos croissants quieres hacer? \n"))
            print("Estos son los ingredientes en gramos para ", cantidad_croissants, "croissants")
        
            def medidas_croissants (cantidad_croissants): 
                harina_croissant = ((TAZA_HARINA_G * 7) / 30) * cantidad_croissants 
                sal_croissant = ((CUCHARADITA_GRAM * 4) / 30) * cantidad_croissants
                levadura_creoissant = ((CUCHARADITA_GRAM * 5) / 30) * cantidad_croissants
                agua_croissant = ((TAZA_AGUA * 2) / 30) * cantidad_croissants
                azucar_croissant = (( TAZA_AZUCAR_G /2) / 30) * cantidad_croissants
                mantequilla_croissant = (( BARRA_MANTEQUILLA_G /2) / 30) * cantidad_croissants
            
                return harina_croissant, sal_croissant, levadura_creoissant, agua_croissant, \
            azucar_croissant, mantequilla_croissant
            
        harina, sal, levadura, agua, azucar, mantequilla =\
        medidas_croissants(cantidad_croissants)
    
        print (harina, "gramos de harina")
        print (sal, "gramos de sal")
        print (levadura, "gramos de levadura") 
        print (agua, "mililitros de agua")
        print (azucar, "gramos de azucar ")
        print (mantequilla, "gramos de mantequilla suavizada")
        opcion = input ("si quieres hacer otra receta teclea 1 para salir teclea 2: ")
        if opcion == "2":
            break
    
#Espacio de Pasteleria
    if opciones_cocina == "C" or opciones_cocina == "c": 
        print("Este es el menu de pasteleria\nEscribe el numero de la receta \n")
        recetas_reposteria = input("1. Pastel de tres leches :  ")
        if recetas_reposteria == "1":
            print("Receta de Pastel de 3 Leches")
            cantidad_pasteles_3L = float( input("¿Cuantos pasteles quieres hacer? \n"))
            print("Estos son los ingredientes en gramos para ", cantidad_pasteles_3L, \
        "pasteles")
        
            def medidas_pastel_3L (cantidad_pasteles_3L): 
                harina_3_leches = (TAZA_HARINA_G * 1.5) * cantidad_pasteles_3L
                aceite_3_leches = (TAZA_ACEITE_ML * .75) * cantidad_pasteles_3L
                levadura_3_leches = CUCHARADITA  * cantidad_pasteles_3L
                vainilla_3_leches = CUCHARADITA * cantidad_pasteles_3L
                azucar_3_leches = ( TAZA_AZUCAR_G /2) * cantidad_pasteles_3L
                huevo_3_leches = (HUEVO *5) * cantidad_pasteles_3L
                leche_3_leches = (TAZA_LECHE_ML * 2.5) * cantidad_pasteles_3L
                condensada_3_leches = TAZA_LECHE_CONDENSADA * cantidad_pasteles_3L
            
            
            
                return harina_3_leches, aceite_3_leches, levadura_3_leches, vainilla_3_leches,\
                azucar_3_leches, huevo_3_leches, leche_3_leches, condensada_3_leches
            
        harina, aceite, levadura, vainilla, azucar, huevo, leche, condensada =\
        medidas_pastel_3L(cantidad_pasteles_3L)
    
        print (harina, "gramos de harina")
        print (aceite, "ml de aceite")
        print (levadura, "cucharaditas de levadura") 
        print (vainilla, "cucharaditas de vainilla")
        print (azucar, "gramos de azucar ")
        print (huevo, "huevos")
        print (leche, "ml de leche")
        print (condensada, "gramos de leche condensada")
        opcion = input ("si quieres hacer otra receta teclea 1 para salir teclea 2: ")
        if opcion == "2":
            break
                
  

    
 

    
    
    

    
