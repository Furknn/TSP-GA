from random import randint, shuffle, sample

from TSPMap import TSPMap


def steady_state_survivor_selection(tsp_map: TSPMap, parents: list, offsprings: list):
    # shuffle offsprings
    shuffle(offsprings)

    # select random individual from offsprings and replace the worst individual from parents with it unless it exists
    # in parents
    # if offsprings[0] not in parents:
    parents[-1] = offsprings[0]

    # for rest of the offsprings
    indices = sample(range(0, len(parents) - 1), len(offsprings) - 1)
    for i in range(1, len(offsprings)):
        parents[indices[i - 1]] = offsprings[i]

    return parents
