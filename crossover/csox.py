from random import sample


def complete_subtour_order_crossover(mating_pool: list):
    P1, P2 = mating_pool
    r1, r2 = sample(range(1, len(P1) - 2), 2)

    O = [[-1 for _ in range(len(P1))] for _ in range(6)]
    pos1, pos2 = 0, 0
    for i in range(3):
        if i == 0:
            pos1 = r1
            pos2 = r2
        elif i == 1:
            pos1 = 0
            pos2 = r1
        elif i == 2:
            pos1 = r2
            pos2 = len(P1)

        # generate offsprings
        O[2 * i][pos1:pos2] = P1[pos1:pos2]
        O[2 * i + 1][pos1:pos2] = P2[pos1:pos2]

        # remaining genes in parent1
        remaining_genes1 = P2[pos2:len(P1)]
        remaining_genes1.extend(P2[0:pos2])

        # remaining genes in parent2
        remaining_genes2 = P1[pos2:len(P1)]
        remaining_genes2.extend(P1[0:pos2])

        # add genes to offspring1 cyclically starting from point2
        j = pos2
        while remaining_genes1 != [] and -1 in O[2 * i]:
            gene = remaining_genes1.pop(0)
            if j == len(P1):
                j = j % len(P1)

            if gene not in O[2 * i]:
                O[2 * i][j] = gene
                j = (j + 1) % len(P1)

        # add genes to offspring2 cyclically starting from point2
        j = pos2
        while remaining_genes2 != [] and -1 in O[2 * i + 1]:
            gene = remaining_genes2.pop(0)
            if j == len(P1):
                j = j % len(P1)
            if gene not in O[2 * i + 1]:
                O[2 * i + 1][j] = gene
                if pos2 == len(P1) - 1:
                    j = j % len(P1)
                else:
                    j = (j + 1) % len(P1)

    # return the offsprings
    return O
