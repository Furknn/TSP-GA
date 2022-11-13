from random import sample, random


def swap_mutation(offsprings: list, mutation_probability: float):
    mutated_offsprings = []
    for offspring in offsprings:
        if int(random() * 100) < int(mutation_probability * 100):
            # randomly select a mutation points
            point1, point2 = sorted(sample(range(len(offspring)), 2))
            # swap the genes
            offspring[point1], offspring[point2] = offspring[point2], offspring[point1]
        mutated_offsprings.append(offspring)
    return mutated_offsprings
