import math
import time
from random import random, randrange, sample

from TSPMap import TSPMap


class TSPSA:
    def __init__(self, tsp_map: TSPMap, initial_solution: list[int], initial_temperature: float, cooling_rate: float,
                 stopping_temperature: float, equilibrium_state: int, preserve_best: bool):
        # Initialize instance variables
        self.tsp_map = tsp_map
        self.initial_solution = initial_solution
        self.initial_temperature = initial_temperature
        self.stopping_temperature = stopping_temperature
        self.cooling_rate = cooling_rate
        self.equilibrium_state = equilibrium_state
        self.preserve_best = preserve_best
        self.current_temperature = self.initial_temperature
        self.best_fitness = None
        self.best_solution = None
        self.fitnesses = []
        self.running_time = None

    def run(self):
        # Initialize variables
        current_solution = self.initial_solution
        current_fitness = self.tsp_map.fitness(current_solution)
        self.best_fitness = current_fitness
        self.best_solution = current_solution
        start_time = time.time()

        # Run simulated annealing loop
        while self.current_temperature > self.stopping_temperature:
            for i in range(self.equilibrium_state):
                # Generate a new solution by perturbing the current solution
                new_solution = self.perturb(current_solution)
                new_fitness = self.tsp_map.fitness(new_solution)

                # Calculate the difference in fitness between the new and current solutions
                delta = new_fitness - current_fitness

                # If the new solution is better than the current solution, accept it
                if delta < 0:
                    current_solution = new_solution
                    current_fitness = new_fitness
                    self.fitnesses.append(current_fitness)
                    # If the new solution is the best solution overall, keep track of it
                    if self.preserve_best and current_fitness < self.best_fitness:
                        self.best_fitness = current_fitness
                        self.best_solution = current_solution


                # If the new solution is not better than the current solution, accept it with a probability
                # based on the current temperature and the difference in fitness
                else:
                    acceptance_probability = math.exp(-delta / self.current_temperature)
                    if acceptance_probability > random():
                        current_solution = new_solution
                        current_fitness = new_fitness

            print(f"Temperature: {self.current_temperature:.2f}, Fitness: {current_fitness:.2f}")
            # Decrease the temperature according to the cooling schedule
            self.current_temperature *= self.cooling_rate

        self.running_time = time.time() - start_time

        # Return the best solution found
        return self.best_fitness

    def perturb(self, current_solution):
        # Select two random indices in the solution
        i, j = sample(range(len(current_solution)), 2)

        # Swap the cities at the selected indices
        new_solution = current_solution.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        return new_solution
