# juego.py
import entrada.menu
import random

def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

def obtener_ayuda(minimo, maximo):
    return f"El número está entre {minimo} y {maximo}."

def jugar():
    minimo, maximo = entrada.menu.seleccionar_nivel()
    numero_secreto = generar_numero_secreto(minimo, maximo)
    
    ayuda = input("¿Desea recibir ayuda? (s/n): ").lower()
    
    if ayuda == 's':
        print(obtener_ayuda(minimo, maximo))
    
    intentos = 0
    while True:
        intento = int(input("Ingrese un número: "))
        intentos += 1
        
        if intento == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        else:
            print("Demasiado alto. Intenta nuevamente.")

if __name__ == "__main__":
    jugar()
