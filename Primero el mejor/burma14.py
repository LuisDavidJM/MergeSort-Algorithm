import math
import matplotlib.pyplot as plt

#Calcula la distancia entre los dos puntos de las ciudades
def euclideanDistance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def totalDistance(route, coord):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclideanDistance(coord[route[i]], coord[route[i + 1]])
    # Agrega la distancia de regreso a la ciudad de inicio
    total_distance += euclideanDistance(coord[route[-1]], coord[route[0]])
    return total_distance

def firstBestAlgorithm(coord):
    num_cities = len(coord)
    # Inicializa la ruta con la primera ciudad
    current = 1
    route = [current]
    # Inicializa la lista de ciudades no visitadas
    unvisited = set(range(1, num_cities + 1))
    unvisited.remove(current)

    while unvisited:
        # Calcula las distancias a las ciudades no visitadas
        distances = [euclideanDistance(coord[current], coord[city]) for city in unvisited]
        # Selecciona la ciudad más cercana en distancia
        next = min(unvisited, key=lambda city: euclideanDistance(coord[current], coord[city]))
        route.append(next)
        unvisited.remove(next)
        current = next

    return route

def plotRoute(coord, route):
    x = [coord[city][0] for city in route]
    y = [coord[city][1] for city in route]

    x.append(x[0])
    y.append(y[0])

    plt.scatter(x, y, c='blue', marker='o')
    plt.plot(x, y, linestyle='-', linewidth=1, color='red')

    for i, city in enumerate(route):
        plt.text(x[i], y[i], str(city), fontsize=12, ha='right')

    plt.title("Primero el mejor (burma14.tsp)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

#Lee el archivo para obtener los datos
#file = "berlin52.tsp"
file = "burma14.tsp"
coord = {}

with open(file, 'r') as file:
    node_coord_section = False
    for line in file:
        if line.startswith("NODE_COORD_SECTION"):
            node_coord_section = True
            continue
        elif line.startswith("EOF"):
            break
        elif node_coord_section and line.strip():
            parts = line.split()
            node = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            coord[node] = (x, y)

# Aplica el algoritmo primero el mejor
best_route = firstBestAlgorithm(coord)
print("Mejor ruta:", best_route)

# Calcula la distancia total de la ruta encontrada
total_distance = totalDistance(best_route, coord)
print("Distancia total:", total_distance)

# Grafica la ruta
plotRoute(coord, best_route)
