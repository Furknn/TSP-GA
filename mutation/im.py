from random import sample, random


def insertion_mutation(offsprings: list, mutation_probability: float):
    mutated_offsprings = []
    for offspring in offsprings:
        if int(random() * 100) < int(mutation_probability * 100):
            # randomly select a mutation points
            point1, point2 = sorted(sample(range(len(offspring)), 2))
            # move point2 to next to point1
            gene2 = offspring.pop(point2)
            offspring.insert(point1 + 1, gene2)
        mutated_offsprings.append(offspring)
    return mutated_offsprings
