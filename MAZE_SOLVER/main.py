import os
from menus import Menu
from save_files import Save
from grid import Grid
from wilson import Wilson
from json import load
from solveproblem import solution


def mainMenu():
    salir = False
    while not(salir):
        Menu.showMenu()
        option_m = Menu.chooseOption('en el rango [1-5]:')
        if option_m == 1:
            print("Generando laberinto...")
            n_rows, n_columns = Menu.giveDimension()
            g = Grid(n_columns, n_rows)
            Wilson.create(g)
            Save.save_json(g)
            
            print("")

        elif option_m == 2:
            print("1.Cargar puzzle")
            print("2.Cargar problema")
            option_l = Menu.chooseOption('en el rango[1-2]')
            if option_l == 1:
                print("Cargando laberinto...")
                os.chdir('puzzles')
                correct = False
                while(correct == False):
                    try:
                        file = str(input('Introduzca ruta laberinto.json:'))
                        g = Grid(0, 0, file)
                        correct = True
                    except FileNotFoundError:
                        print("Archivo no encontrado")
                Save.save_json(g)
                print('Pintando laberinto...')
                print('Laberinto cargado, Imagen guardada en el directorio actual.')
                os.chdir('..')
            elif option_l == 2:
                correct = False
                while(correct == False):
                    try:
                        filename = str(input('Introduzca ruta laberinto.json:'))
                        os.chdir('problemas')
                        with open(filename) as fdata:
                            jsondata = load(fdata)
                        a = str(jsondata['INITIAL'])
                        initial = Grid.parse_tuple(jsondata['INITIAL'])
                        end = Grid.parse_tuple(jsondata['OBJETIVE'])
                        maze_filename = jsondata['MAZE']
                        g = Grid(0, 0, maze_filename)
                        correct = True
                    except FileNotFoundError:
                        os.chdir('..')
                        print("Archivo no encontrado")
                Save.save_json_problem(g)
                print('Pintando laberinto...')
                print('Laberinto cargado, Imagen guardada en el directorio actual.')
                os.chdir('..')
            else:
                print("Opción incorrecta")

        elif option_m == 3:
            print("Creando problema en laberinto")
            correct = False
            while(correct == False):
                try:
                    filename = str(input('Introduzca ruta del fichero:'))
                    g = Grid(0, 0, filename)
                    correct = True
                except FileNotFoundError:
                    print("Archivo no encontrado")
            Save.save_json_problem(g)
            print('Problema generado, json guardada en el directorio actual.')

        elif option_m == 4:
            print("Resolviendo laberinto...")
            os.chdir('problemas')
            correct = False
            while(correct == False):
                try:
                    filename = str(input('Introduzca ruta del fichero:'))
                    list_solution, w, h, strategy = solution(filename)
                    correct = True
                except FileNotFoundError:
                    print("Archivo no encontrado")
            for l in list_solution:
                print(l)
            list_strategy = ["", "BREADTH", "DEPTH", "UNIFORM", "GREEDY", "A"]
            output = f"sol_{w}x{h}_{list_strategy[strategy]}.txt"
            
            with open(output, 'wt') as fp:
                fp.write("[id][cost,state,father_id,action,depth,h,value]\n")
                for l in list_solution:
                    fp.write(f"{l}\n")

            os.chdir('..')

        elif option_m == 5:
            print("Saliendo...")
            salir = True
            print("Has salido de programa con éxito")
        else:
            print("Opción incorrecta")

if __name__ == '__main__':
    mainMenu()
    

    
    