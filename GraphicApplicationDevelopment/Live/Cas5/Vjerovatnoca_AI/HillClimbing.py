import random


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
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
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


def main():
    tsp = [
        [0, 400, 500, 300, 200, 600, 700, 800, 900, 100],
        [400, 0, 300, 500, 600, 200, 300, 400, 500, 600],
        [500, 300, 0, 400, 500, 100, 200, 300, 400, 500],
        [300, 500, 400, 0, 100, 700, 800, 900, 1000, 1100],
        [200, 600, 500, 100, 0, 600, 700, 800, 900, 1000],
        [600, 200, 100, 700, 600, 0, 100, 200, 300, 400],
        [700, 300, 200, 800, 700, 100, 0, 100, 200, 300],
        [800, 400, 300, 900, 800, 200, 100, 0, 100, 200],
        [900, 500, 400, 1000, 900, 300, 200, 100, 0, 100],
        [100, 600, 500, 1100, 1000, 400, 300, 200, 100, 0]
    ]

    print(hillClimbing(tsp))


if __name__ == "__main__":
    main()
