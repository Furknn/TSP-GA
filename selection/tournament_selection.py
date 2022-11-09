from random import sample

from TSPMap import TSPMap


def tournament_selection(tsp_map: TSPMap, population: list, tournament_size: int):
    # select tournament_size individuals from population randomly without duplicates
    tournament = sample(set(tuple(individual) for individual in population), tournament_size)
    # sort tournament
    tournament.sort(key=lambda x: tsp_map.fitness(x))
    # return the best two unique individuals from tournament
    return [list(tournament[0]), list(tournament[1])]
