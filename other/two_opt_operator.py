from random import sample, randint

from TSPMap import TSPMap


def two_opt_operator(tsp_map: TSPMap, population: list, m: int, n: int):
    # m: number of individuals to be selected from the population
    # n: number of times the operator is applied to each individual
    # returns: a list of individuals after the operator is applied

    # select m individuals from the population and add them to the selected individuals
    indexes = sample(range(1, len(population)), m)
    indexes.append(0)

    for i in indexes:
        individual = population[i]
        fitness = tsp_map.fitness(individual)
        for j in range(n):
            individual_copy = individual.copy()
            # randomly select two nodes, sorted
            node1, node2 = sorted(sample(range(tsp_map.size), 2))
            # swap the nodes
            new_individual = two_opt_swap(individual_copy, node1, node2)
            # if the new individual is better than the old one, replace the old one with the new one
            if tsp_map.fitness(new_individual) < fitness:
                individual = new_individual
                fitness = tsp_map.fitness(individual)

        population[i] = individual

    return population


def two_opt_swap(individual: list, node1: int, node2: int):
    new_individual = []
    # take the nodes between node1 and node2 and add them
    new_individual.extend(individual[0:node1])
    # take the nodes between node2 and node1 and add them in reverse order
    new_individual.extend(reversed(individual[node1:node2]))
    # take the nodes before node1 and add them
    new_individual.extend(individual[node2:])

    return new_individual
