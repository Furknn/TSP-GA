from random import sample


def order_crossover(mating_pool: list):
    # compare the length of the parents
    parent1 = mating_pool[0]
    parent2 = mating_pool[1]

    size = len(parent1)
    # randomly select a crossover point
    point1, point2 = sorted(sample(range(0, size), 2))

    if parent1 == parent2:
        return [parent1, parent2]

    while parent1 != parent2 and parent2[point1:point2] == parent1[point1:point2]:
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


def order_crossover_alt(mating_pool: list):
    ind1 = mating_pool[0]
    ind2 = mating_pool[1]

    size = min(len(ind1), len(ind2))
    a, b = sample(range(size), 2)
    if a > b:
        a, b = b, a

    holes1, holes2 = [True] * size, [True] * size
    for i in range(size):
        if i < a or i > b:
            holes1[ind2[i]] = False
            holes2[ind1[i]] = False

    # We must keep the original values somewhere before scrambling everything
    temp1, temp2 = ind1, ind2
    k1, k2 = b + 1, b + 1
    for i in range(size):
        if not holes1[temp1[(i + b + 1) % size]]:
            ind1[k1 % size] = temp1[(i + b + 1) % size]
            k1 += 1

        if not holes2[temp2[(i + b + 1) % size]]:
            ind2[k2 % size] = temp2[(i + b + 1) % size]
            k2 += 1

    # Swap the content between a and b (included)
    for i in range(a, b + 1):
        ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2
