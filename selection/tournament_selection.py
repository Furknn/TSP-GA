from random import sample, randint

from TSPMap import TSPMap


def tournament_selection(tsp_map: TSPMap, population: list, tournament_size: int):
    # select tournament_size individuals from population randomly without duplicates
    population_set = set(tuple(individual) for individual in population)

    tournament = []
    if len(population_set) < tournament_size:
        tournament = list(population_set).copy()
        while not len(tournament) == tournament_size:
            tournament.append(tournament[randint(0, len(tournament) - 1)])
    else:
        tournament = sample(population_set, tournament_size)

    # sort tournament
    tournament.sort(key=lambda x: tsp_map.fitness(x))
    # return the best two unique individuals from tournament
    return [list(tournament[0]), list(tournament[1])]
