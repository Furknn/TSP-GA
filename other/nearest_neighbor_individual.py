from TSPMap import TSPMap


def nearest_neighbor_individual(tsp_map: TSPMap, initial: list):
    individual = [initial]
    remaining = list(range(0, tsp_map.size))
    remaining.remove(initial)
    while len(remaining) > 0:
        nearest = remaining[0]
        for city in remaining:
            city_distance = tsp_map.distances[(individual[-1], city)]
            nearest_distance = tsp_map.distances[(individual[-1], nearest)]
            if city_distance < nearest_distance:
                nearest = city
        individual.append(nearest)
        remaining.remove(nearest)
    return individual
