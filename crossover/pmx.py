from random import sample


def partially_mapped_crossover(mating_pool: list):
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
    # get genes from parent2
    for i in range(point1, point2):
        gene = parent2[i]
        if gene not in offspring1:
            offspring1[get_new_gene_index(gene, parent1, parent2, offspring1)] = gene

    # iterate over elements in offspring1 with -1
    for i in range(size):
        if offspring1[i] == -1:
            offspring1[i] = parent2[i]

    # create the offspring2
    offspring2 = [-1] * size
    offspring2[point1:point2] = parent2[point1:point2]
    # get genes from parent1
    for i in range(point1, point2):
        gene = parent1[i]
        if gene not in offspring2:
            offspring2[get_new_gene_index(gene, parent2, parent1, offspring2)] = gene

    # iterate over elements in offspring2 with -1
    for i in range(size):
        if offspring2[i] == -1:
            offspring2[i] = parent1[i]

    # give warning if one of the offsprings is the same as one of the parents
    if offspring1 == parent1 or offspring1 == parent2 or offspring2 == parent1 or offspring2 == parent2:
        print("Warning: one of the offsprings is the same as one of the parents")

    return [offspring1, offspring2]


def get_new_gene_index(gene, source_parent, target_parent, offspring):
    # source_parent: parent that already has genes inserted into offspring
    # target_parent: parent that has the gene to be inserted

    # get the index of the gene in the target_parent
    new_index = target_parent.index(source_parent[target_parent.index(gene)])
    if offspring[new_index] == -1:
        return new_index
    else:
        # if the new_index is already occupied, get the new index
        new_gene = target_parent[new_index]
        return get_new_gene_index(new_gene, source_parent, target_parent, offspring)
