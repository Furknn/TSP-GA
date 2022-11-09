from random import sample


def order_crossover(mating_pool: list):
    # compare the length of the parents
    parent1 = mating_pool[0]
    parent2 = mating_pool[1]

    size = len(parent1)
    # randomly select a crossover point
    point1, point2 = sorted(sample(range(0, size), 2))
    while parent2[point1:point2] == parent1[point1:point2]:
        point1, point2 = sorted(sample(range(0, size), 2))

    # create the offspring1
    offspring1 = [-1] * size
    offspring1[point1:point2] = parent1[point1:point2]

    # remaining genes in parent2
    remaining_genes = parent2[point2:size]
    remaining_genes.extend(parent2[0:point2])

    # add genes to offspring1 cyclically starting from point2
    i = point2
    while remaining_genes != [] and -1 in offspring1:
        gene = remaining_genes.pop(0)
        if gene not in offspring1:
            offspring1[i] = gene
            i = (i + 1) % size

    # create the offspring2
    offspring2 = [-1] * size
    offspring2[point1:point2] = parent2[point1:point2]

    # remaining genes in parent1
    remaining_genes = parent1[point2:size]
    remaining_genes.extend(parent1[0:point2])

    # add genes to offspring2 cyclically starting from point2
    i = point2
    while remaining_genes != [] and -1 in offspring2:
        gene = remaining_genes.pop(0)
        if gene not in offspring2:
            offspring2[i] = gene
            i = (i + 1) % size

    # give warning if one of the offsprings is the same as one of the parents
    if offspring1 == parent1 or offspring1 == parent2 or offspring2 == parent1 or offspring2 == parent2:
        print("Warning: one of the offsprings is the same as one of the parents")

    return [offspring1, offspring2]
