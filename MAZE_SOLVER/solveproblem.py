from frontier import Frontier
from node import Node
from json import load
from grid import Grid
from menus import Menu
from decimal import Decimal


def load_problem(filename):
    with open(filename) as fdata:
        jsondata = load(fdata)
    a = str(jsondata['INITIAL'])
    initial = Grid.parse_tuple(jsondata['INITIAL'])
    end = Grid.parse_tuple(jsondata['OBJETIVE'])
    maze_filename = jsondata['MAZE']
    g = Grid(0, 0, maze_filename)
    return initial, end, g

def successor(cell):
    list_successor = list()
    return list_successor


def get_sucessor_nodes(current_node, g, list_sucessors, all_succesor, strategy, end):
    list_nodes = []
    value = 0
    for sucessor in list_sucessors:
        all_succesor.append(sucessor)
        ID = len(all_succesor)
        cost = current_node.cost + g[sucessor[1].get_tuple()].value + 1
        state = sucessor[1]
        father_id = current_node.ID 
        depth = current_node.depth + 1
        action = sucessor[0]
        h = abs(sucessor[1].row - end[0]) + abs(sucessor[1].column - end[1])
        node = Node(ID, cost, state, father_id, action, depth, h, value)
        if strategy == 1:
            value = depth
        elif strategy == 2:
                value = 1.0/(depth+1)
        elif strategy == 3:
            value = cost 
        elif strategy == 4:
            value = abs(sucessor[1].row - end[0]) + abs(sucessor[1].column - end[1])
        elif strategy == 5:
            value = cost + h
        else:
           print("opcion fuera de rango")
        node.value = value
        list_nodes.append(node)
    return list_nodes


def expandir(current_node, g, visited, expanded, frontier, all_succesor, strategy, end):
    list_sucesores = get_sucessor_nodes(current_node, g, current_node.state.neighbors_format(), all_succesor, strategy, end)
    if strategy == 2:
        for sucesor in list_sucesores:
            if not visited[f"{sucesor.state}"]:
                push_frontier(frontier, sucesor)
                visited[f"{sucesor.state}"] = True
            elif not expanded[f'{sucesor.state}']:
                frontier.remove_by_pos(sucesor.state.get_tuple())
                push_frontier(frontier, sucesor)
                visited[f"{sucesor.state}"] = True
    else:
        for sucesor in list_sucesores:
            if not visited[f"{sucesor.state}"]:
                push_frontier(frontier, sucesor)
                visited[f"{sucesor.state}"] = True

     
def get_node_by_id(id, path):
    for state in path:
        if state.ID == id:
            return state
    return None

def push_frontier(frontier, node):
    if (frontier.is_empty()):
        frontier.push(node)
    else:
        x = frontier.get_size() - 1
        pos = frontier.items[x].state.get_tuple()[0]
        while x >= 0:
            if ((frontier.get_value(x) < node.value)):
                frontier.insert(x+1,node)
                break
            elif(frontier.get_value(x) == node.value):
                if(frontier.items[x].state.get_tuple()[0] < node.state.get_tuple()[0]):
                    frontier.insert(x+1,node)
                    break
                else:
                    if(frontier.items[x].state.get_tuple()[0] == node.state.get_tuple()[0]):
                        if(frontier.items[x].state.get_tuple()[1] < node.state.get_tuple()[1] ):
                            frontier.insert(x+1,node)
                            break
                        elif(frontier.items[x].state.get_tuple()[1] == node.state.get_tuple()[1] ):
                            if (frontier.items(x).state.ID < node.ID):
                                frontier.insert(x+1,node)
                                break
            if (x==0):
                frontier.insert(0,node)
            x= x-1

def solution(filename):
    initial, end, g = load_problem(filename)
    w, height = g.dimensions()
    all_succesor = []
    Menu.showStrategies()
    strategy = Menu.chooseOption('en el rango [1-5]')
    while strategy < 0 or strategy > 5:
        print("Estrategia no valida")
        strategy = Menu.chooseOption('en el rango [1-5]')

    str_solution = []
    visited = dict()
    expanded = dict()
    frontier = Frontier()
    for cell in g.each_cell():
        visited[cell.__str__()] = False
        expanded[cell.__str__()] = False
    path = []
    found = False
    h = abs(end[1] - initial[1]) + abs(end[0] - initial[0])
    if strategy >= 4:
        first_node = Node(0,0,g[initial],-1, "None",0, h,h)
    else:
        first_node = Node(0,0,g[initial],-1, "None",0, h,0)

    current_node = first_node
    frontier.push(current_node)
    visited[f'{first_node.state}'] = True
    
    while not frontier.is_empty() and not found:
        current_node = frontier.pop_order()
        expanded[f'{current_node.state}'] = True
        path.append(current_node)
        if current_node.depth==1000000:
            print("SE HA ALCANZADO LA PROFUNIDAD MAXIMA")
            break
        if current_node.state.get_tuple() == end:
            found = True
            break
        else:
            expandir(current_node, g,visited, expanded, frontier, all_succesor, strategy, end)
    print("[id][cost,state,father_id,action,depth,h,value]") 
    list_solution = []
    current_node = path[-1]
    if current_node.father_id == -1:
        output = f'[{current_node.ID}]({current_node.cost},{current_node.state},None,{current_node.action},{current_node.depth},{current_node.h},{Decimal(current_node.value)})'
    else:
        output = f'[{current_node.ID}]({current_node.cost},{current_node.state},{current_node.father_id},{current_node.action},{current_node.depth},{current_node.h},{Decimal(current_node.value)})'
    list_solution.append(output)
    father_id = current_node.father_id

    while father_id >= 0:
        current_node = get_node_by_id(father_id, path)
        if current_node is None:
            break
        if current_node.father_id == -1:
            output = f'[{current_node.ID}]({current_node.cost},{current_node.state},None,{current_node.action},{current_node.depth},{current_node.h},{Decimal(current_node.value)})'
        else:
            output = f'[{current_node.ID}]({current_node.cost},{current_node.state},{current_node.father_id},{current_node.action},{current_node.depth},{current_node.h},{Decimal(current_node.value)})'
        list_solution.append(output)
        father_id = current_node.father_id
        if father_id is None:
            break
    list_solution.reverse()
    return list_solution, w, height, strategy

# main


