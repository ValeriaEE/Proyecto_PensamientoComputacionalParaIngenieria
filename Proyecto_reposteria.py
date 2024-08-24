# Este codigo es el proyecto de la clase de programación 
# Reposteria Automatizada :P

#Medidas en gramos 
"""Determine las cantidades en gramos de cada ingrediente"""

TAZA_HARINA_G = float(150)
TAZA_CHISPAS_G = float(200)
BARRA_MANTEQUILLA_G = float(227)
TAZA_AZUCAR_G = float(200)
HUEVO_G = float(60)
CUCHARADITA_G_ML = float(5)
TAZA_NUECES = float(100)
    
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
        
        harina_galletas = ((TAZA_HARINA_G*2) / 60) * cantidad_galletas
        print (harina_galletas, "gramos de harina")
        
        chispas_galletas = ((TAZA_CHISPAS_G*2) / 60) * cantidad_galletas
        print (chispas_galletas, "gramos de chispas de chocolate ")
        
        mantequilla_galletas = ((BARRA_MANTEQUILLA_G)*2 / 60) * cantidad_galletas
        print (mantequilla_galletas, "gramos de mantequilla suavizada")
        
        azucar_galletas = ((TAZA_AZUCAR_G)*1.5 / 60) * cantidad_galletas
        print (azucar_galletas, "gramos de azucar")
        
        
        
        
        
        
#Espacio de panaderia
if opciones_cocina == "B" or opciones_cocina == "b": 
    print("panaderia")
    
    
#Espacio de Pasteleria
if opciones_cocina == "C" or opciones_cocina == "c": 
    print("pasteleria")
    

    
 

    
    
    

    
