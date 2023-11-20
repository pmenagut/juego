def seleccionar_nivel():
    print("Seleccione un nivel de dificultad:")
    print("1. Nivel Simple (entre 0 y 100)")
    print("2. Nivel Intermedio (entre 0 y 1,000)")
    print("3. Nivel Avanzado (entre 0 y 1,000,000)")
    print("4. Nivel Experto (entre 0 y 1,000,000,000,000)")
    opcion = int(input("Ingrese el número correspondiente al nivel: "))
    
    if opcion == 1:
        return 0, 100
    elif opcion == 2:
        return 0, 1000
    elif opcion == 3:
        return 0, 1000000
    elif opcion == 4:
        return 0, 1000000000000
    else:
        print("Opción no válida. Seleccionando nivel Simple por defecto.")
        print("Vuelva a intentarlo")