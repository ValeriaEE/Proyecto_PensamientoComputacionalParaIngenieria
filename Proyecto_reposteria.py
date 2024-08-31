# Este codigo es el proyecto de la clase de programación 
# Reposteria Automatizada :P

#Medidas en gramos 

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

    
"""Hice un menu para que eligieran lo que querian cocinar y dento de cada opcion del menu 
hay recetas que pueen elegir"""
#Menu 
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
        cantidad_galletas = float( input("¿Cuantas galletas quieres hacer? \n"))
        print("Estos son los ingredientes en gramos para ", cantidad_galletas, "galletas")
        
        """Creamos una funcion para los calculos necesarios"""
        
        def medida_gramos_galletas(cantidad_galletas):
            harina_galletas = ((TAZA_HARINA_G*2) / 60) * cantidad_galletas
            chispas_galletas = ((TAZA_CHISPAS_G*2) / 60) * cantidad_galletas
            mantequilla_galletas = ((BARRA_MANTEQUILLA_G*2) / 60) * cantidad_galletas
            azucar_galletas = ((TAZA_AZUCAR_G*1.5) / 60) * cantidad_galletas
            nueces_galletas = (TAZA_NUECES /60) * cantidad_galletas
            
            
            return harina_galletas, chispas_galletas, mantequilla_galletas, azucar_galletas, \
            nueces_galletas
            
        def medida_enteros_galletas(cantidad_galletas):
            if cantidad_galletas >= 60: 
                num_enteros_galletas = cantidad_galletas // 60
               
                vainilla_galletas = CUCHARADITA * num_enteros_galletas
                huevos_galletas = (HUEVO * 2) * num_enteros_galletas
                bicarbonato_galletas = CUCHARADITA * num_enteros_galletas
                sal_galletas= (CUCHARADITA/2) * num_enteros_galletas
            
            elif cantidad_galletas <= 60 and cantidad_galletas >= 30: 
                
                num_enteros_galletas = 1
               
                vainilla_galletas = CUCHARADITA * num_enteros_galletas
                huevos_galletas = (HUEVO * 2) * num_enteros_galletas
                bicarbonato_galletas = CUCHARADITA * num_enteros_galletas
                sal_galletas= (CUCHARADITA/2) * num_enteros_galletas
                
            else: 
                num_enteros_galletas = 1/2
               
                vainilla_galletas = CUCHARADITA * num_enteros_galletas
                huevos_galletas = (HUEVO * 2) * num_enteros_galletas
                bicarbonato_galletas = CUCHARADITA * num_enteros_galletas
                sal_galletas= (CUCHARADITA/2) * num_enteros_galletas
                
            return vainilla_galletas, huevos_galletas, bicarbonato_galletas, \
            sal_galletas
            
            
            
        """Llammos a la funcion y se guardan en las variables los datos"""
        
        harina, chispas, mantequilla, azucar, nueces\
        = medida_gramos_galletas(cantidad_galletas)
        
        vainilla, huevos, bicarbonato, sal = medida_enteros_galletas(cantidad_galletas)

        print (harina, "gramos de harina")
        print (chispas, "gramos de chispas de chocolate")
        print (mantequilla, "gramos de mantequilla suavizada")
        print (azucar, "gramos de azucar ") 
        print (nueces, "gramos de nueces") 
        print (vainilla, "cucharaditas de vainilla")
        print (huevos, "huevos")
        print (bicarbonato, "cucharaditas de bicarbonato de sodio")
        print (sal, "cucharaditas de sal ")
        
    
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
    
#Espacio de Pasteleria
if opciones_cocina == "C" or opciones_cocina == "c": 
    print("pasteleria")
    

    
 

    
    
    

    
