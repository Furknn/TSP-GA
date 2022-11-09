import time
from random import *
from statistics import stdev

from crossover.ox import order_crossover
from crossover.pmx import partially_mapped_crossover
from TSPMap import TSPMap
from mutation.im import insertion_mutation
from mutation.ivm import inversion_mutation
from mutation.sm import swap_mutation
from other.two_opt_operator import two_opt_operator
from selection.steady_state_survivor_selection import steady_state_survivor_selection
from selection.tournament_selection import tournament_selection


class TSPGA:
    def __init__(self, tsp_map: TSPMap, population_size: int, mutation_probability: float, generations: int,
                 tournament_size: int,
                 crossover_operator: str, mutation_operator: str, K: int, N: int, M: int, log_generations: list[int]):
        self.map = tsp_map
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.generations = generations
        self.tournament_size = tournament_size
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator
        self.log_generations = log_generations
        self.K = K  # frequency of 2-opt
        self.N = N  # number of cities to be swapped in two-opt
        self.M = M  # number of individuals to be swapped in two-opt

        self.best_fitness = None
        self.best_individual = None
        self.best_fitnesses = []
        self.avarage_fitnesses = []
        self.standard_deviations = []

        self.start_time = None
        self.end_time = None
        self.running_time = None

    def initialization(self):
        population = []
        # Create %80 of the population randomly
        p80 = int(self.population_size * 0.8)
        while len(population) < p80:
            individual = list(range(1, self.map.size + 1))
            shuffle(individual)
            if individual not in population:
                population.append(individual)

        # Create %20 of the population using nearest neighbor algorithm
        p20 = int(self.population_size * 0.2)
        initial_cities = sample(range(1, self.map.size + 1), p20)
        for city in initial_cities:
            population.append(self.nearest_neighbor_individual(city))
        return population

    def nearest_neighbor_individual(self, initial):
        individual = [initial]
        remaining = list(range(1, self.map.size + 1))
        remaining.remove(initial)
        while len(remaining) > 0:
            nearest = remaining[0]
            for city in remaining:
                city_distance = self.map.distances[(individual[-1], city)]
                nearest_distance = self.map.distances[(individual[-1], nearest)]
                if city_distance < nearest_distance:
                    nearest = city
            individual.append(nearest)
            remaining.remove(nearest)
        return individual

    def crossover(self, mating_pool):
        if self.crossover_operator == "OX":
            offsprings = order_crossover(mating_pool)
        elif self.crossover_operator == "PMX":
            offsprings = partially_mapped_crossover(mating_pool)
        else:
            raise Exception("Unknown crossover operator")
        return offsprings

    def mutation(self, offsprings):
        if self.mutation_operator == "SM":
            mutated_offsprings = swap_mutation(offsprings, self.mutation_probability)
        elif self.mutation_operator == "IM":
            mutated_offsprings = insertion_mutation(offsprings, self.mutation_probability)
        elif self.mutation_operator == "IVM":
            mutated_offsprings = inversion_mutation(offsprings, self.mutation_probability)
        else:
            raise Exception("Unknown mutation operator")
        return mutated_offsprings

    def run(self):
        population = self.initialization()
        self.start_time = time.time()
        for i in range(self.generations+1):
            mating_pool = tournament_selection(self.map, population, self.tournament_size)
            offsprings = self.crossover(mating_pool)
            mutated_offsprings = self.mutation(offsprings)
            population = steady_state_survivor_selection(self.map, population, mutated_offsprings)

            # sort the population according to their fitness

            population.sort(key=lambda x: self.map.fitness(x))
            if i % self.K == 0:
                population = two_opt_operator(self.map, population, self.M, self.N)
                population.sort(key=lambda x: self.map.fitness(x))

            self.best_fitness = self.map.fitness(population[0])
            avarage_fitness = sum([self.map.fitness(individual) for individual in population]) / len(population)
            standard_deviation = stdev([self.map.fitness(individual) for individual in population])
            print(f"Generation: {i} Best fitness: {self.best_fitness} Avarage fitness: {avarage_fitness} Standard deviation: {standard_deviation}")

            if i in self.log_generations:
                self.best_fitnesses.append(self.best_fitness)
                self.avarage_fitnesses.append(avarage_fitness)
                self.standard_deviations.append(standard_deviation)

            if self.best_fitness is None or self.map.fitness(population[0]) < self.best_fitness:
                self.best_fitness = self.map.fitness(population[0])
                self.best_individual = population[0]

        self.end_time = time.time()
        self.running_time = self.end_time - self.start_time

        return population[0]
