import random
#TSP Travelller Salesman Problem

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)): # i = 0,1,2,3 - gradovi
        randomCity = cities[random.randint(0, len(cities) - 1)] #bira slucajan grad (0,1,2,3)
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]] # i - 1 je zadnji element! 0 -1 = -1 -> -1 je zadnji elemnt u listi
    return routeLength

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy() #lista neighbour pravi novu memorijsku lokaciju sa podatcima od souilution
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength

def duzine(n):
    tsp = [[random.randint(1,n)*100 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        tsp[i][i] = 0
    return tsp

def main():
    tsp = duzine(10)
    print("All distances:")
    print(tsp)
    print("------------------")
    sol = randomSolution(tsp)
    print("Random soulution:")
    print(sol)
    print("------------------")
    print("Route length of random soulution:")
    print(routeLength(tsp, sol))
    print("------------------")
    susedi = getNeighbours(sol)
    print("Neighbours:")
    print(susedi)
    print("------------------")
    print("Best neighbour and shortest route lenghts")
    print(getBestNeighbour(tsp, susedi))
    print("------------------")
    print("Hill Climbing:")
    print(hillClimbing(tsp))


if __name__ == "__main__":
    main()