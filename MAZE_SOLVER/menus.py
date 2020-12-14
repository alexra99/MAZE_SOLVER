class Menu:
    def chooseOption(option):
        correct = False
        num = 0
        while (not correct):
            try:
                num = int(input("Introduzca opción "+option+"\n"))
                correct = True
            except ValueError:
                print('Error, introduce un numero entero')

        return num


    def showMenu():
        print("-----MAZE-SOLVER-----")
        print("1. Generar laberinto")
        print("2. Cargar laberinto")
        print("3. Generar Problema ")
        print("4. Resolver Problema")
        print("5. Salir")
    

    def giveDimension():
        correct = False
        while (correct == False):
            try:
                n_rows = int(input('Introduzca el número de filas: '))
                n_columns = int(input('Introduzca el número de columnas: '))
                

                return n_rows, n_columns
                correct = True
            except ValueError as error:
                print('valor de entrada no válido')

    def showStrategies():
        print("\nESTRATEGIAS DISPONIBLES PARA RESOLVER LABERINTO:")
        print("1. Anchura")
        print("2. Profundidad")
        print("3. Coste uniforme")
        print("4. Voraz")
        print("5. A estrella")