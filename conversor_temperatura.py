#Sistema de conversión de temperatura entre distintas escalas, Celcius, Farenheit y Kelvin.
#1.Construir un menu
#2.Definir funciones de conversion
#3.Pedir datos al usuario
#4.Realizar conversión
#5.Mostrar resultado

#ºF C°	(T – 32)/1.8	
# °F K    (T-32)*5/9+273.15
# ºC K	(T + 273.15)	
# °C F°   (T * 1.8) + 32
# K C°	(T – 273.15)		
# K F°    (T-273.15)*9/5+32

def cargar_menu():
    print("[1] Convertir °C a K.")
    print("[2] Convertir °C a °F.")
    print("[3] Convertir K a °C.")
    print("[4] Convertir K a °F.")
    print("[5] Convertir °F a °C.")
    print("[6] Convertir °F a K.")
    print("[0] Salir.")

def convertir_celcius_kelvin(temperatura_inicial):
    temperatura = temperatura_inicial + 273.15
    return temperatura

def convertir_celcius_farenheit(temperatura_incial):
    temperatura = (temperatura_incial * 1.8) + 32
    return temperatura

def convertir_kelvin_celcius(temperatura_inicial):
    temperatura = (temperatura_inicial - 273.15)
    return temperatura

def convertir_kelvin_farenheit(temperatura_inicial):
    temperatura = (convertir_kelvin_celcius(temperatura_inicial))* 9/5 + 32
    return temperatura

def convertir_farenheit_celcius(temperatura_inicial):
    temperatura = (temperatura_inicial - 32) /1.8
    return temperatura

def convertir_farenheit_kelvin(temperatura_inicial):
    temperatura = (convertir_farenheit_celcius(temperatura_inicial)) + 273.15
    return temperatura

def solicitar_datos():
    temperatura_usuario = float(input("Ingrese su Temperatura Inicial: "))
    return temperatura_usuario

def programa_principal():
    print()
    print("¡Súper Conversor de Temperatura!")
    print("=================================")
    
    while True: 
        cargar_menu()
        print()
        opcion = input("Seleccione su opción [0-6]:")
        resultado = 0
        temperatura_inicial = 0

        if opcion == "1":
            escala_inicial = "°C"
            escala_final = "K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_celcius_kelvin(temperatura_inicial)
        elif opcion == "2":
            escala_inicial = "°C"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_celcius_farenheit(temperatura_inicial)
        elif opcion == "3":
            escala_inicial = "K"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_kelvin_celcius (temperatura_inicial)
        elif opcion == "4":
            escala_inicial = "°K"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_kelvin_farenheit (temperatura_inicial)
        elif opcion == "5":
            escala_inicial = "°F"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_farenheit_celcius (temperatura_inicial)
        elif opcion == "6":
            escala_inicial = "°F"
            escala_final = "K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_farenheit_kelvin (temperatura_inicial)
        elif opcion == "0":
            print("Adios.")
            break
        else: 
            print("Opción Invalida")
            pass
        print()
        print(f"{temperatura_inicial}{escala_inicial} = {resultado}{escala_final}")
        print()

programa_principal()




