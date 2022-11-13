from random import randint, shuffle

from TSPMap import TSPMap


def steady_state_survivor_selection(tsp_map: TSPMap, parents: list, offsprings: list):
    # shuffle offsprings
    shuffle(offsprings)

    # select random individual from offsprings and replace the worst individual from parents with it unless it exists
    # in parents
    # if offsprings[0] not in parents:
    parents[-1] = offsprings[0]

    # select random individual from offsprings and replace random individual from parents with it
    # if offsprings[1] not in parents:
    parents[randint(0, len(parents) - 1)] = offsprings[1]
    return parents
