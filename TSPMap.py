import math


class TSPMap:
    def __init__(self):
        self.cities = {}
        self.distances = {}
        self.size = 0

    def read(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        # Read city coordinates
        for line in lines:
            if line.startswith("EOF"):
                break

            if line.startswith("NODE_COORD_SECTION") or line.startswith("NAME") or line.startswith(
                    "COMMENT") or line.startswith("TYPE") or line.startswith("DIMENSION") or line.startswith(
                "EDGE_WEIGHT_TYPE"):
                continue

            line = line.split()

            self.cities[int(line[0])] = {"x": int(line[1]), "y": int(line[2])}
            self.size += 1

        # Fill the distances list
        for i in range(1, self.size + 1):
            for j in range(i + 1, self.size + 1):
                city1 = self.cities[i]
                city2 = self.cities[j]
                self.distances[(i, j)] = self.distance(city1, city2)
                self.distances[(j, i)] = self.distances[(i, j)]

    def distance(self, city1, city2):
        return math.sqrt((city1["x"] - city2["x"]) ** 2 + (city1["y"] - city2["y"]) ** 2)

    def fitness(self, individual: list):
        fit = sum([self.distances[(individual[i], individual[i + 1])] for i in range(len(individual) - 1)]) + \
              self.distances[(individual[-1], individual[0])]
        return fit
