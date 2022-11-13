from TSPMap import TSPMap
from TSPGA import TSPGA

from logs import *


def varying_crossover_mutation_types(tsp_map: TSPMap):
    # First run, Varying the crossover and mutation operators
    case_run_time = 1
    population_size = 50
    mutation_probability = 0.1
    generations = 100
    tournament_size = 5
    crossover_operators = ["PMX", "OX"]
    mutation_operators = ["SM", "IM", "IVM"]
    K = 20
    N = 5
    M = 1
    # log at every generation
    log_generations = [1000, 5000, 20000]

    best_crossover_operator = None
    best_run_fitness = None
    best_run_individual = None
    best_mutation_operator = None
    best_case_run_time = None

    worst_crossover_operator = None
    worst_run_fitness = None
    worst_run_individual = None
    worst_mutation_operator = None
    worst_case_run_time = None

    for crossover_operator in crossover_operators:
        for mutation_operator in mutation_operators:

            best_run_fitness_in_operator_combination = None
            best_run_individual_in_operator_combination = None
            best_case_run_time_in_operator_combination = None

            for i in range(case_run_time):
                tsp_ga = TSPGA(tsp_map, population_size, mutation_probability, generations, tournament_size,
                               crossover_operator, mutation_operator, K, N, M, log_generations)
                best_individual_of_run = tsp_ga.run()

                log_per_run(best_individual_of_run, crossover_operator, i, mutation_operator, tsp_ga)

                # check if best fitness of run is better than the best fitness of all runs
                if best_run_fitness is None or best_run_fitness > tsp_ga.best_fitness:
                    best_run_fitness = tsp_ga.best_fitness
                    best_run_individual = best_individual_of_run
                    best_crossover_operator = crossover_operator
                    best_mutation_operator = mutation_operator
                    best_case_run_time = i

                # check if worst fitness of run is worse than the worst fitness of all runs
                if worst_run_fitness is None or worst_run_fitness < tsp_ga.best_fitness:
                    worst_run_fitness = tsp_ga.best_fitness
                    worst_run_individual = best_individual_of_run
                    worst_crossover_operator = crossover_operator
                    worst_mutation_operator = mutation_operator
                    worst_case_run_time = i

                # check if best fitness of run is better than the best fitness of all runs in operator combination
                if best_run_fitness_in_operator_combination is None or best_run_fitness_in_operator_combination > tsp_ga.best_fitness:
                    best_run_fitness_in_operator_combination = tsp_ga.best_fitness
                    best_run_individual_in_operator_combination = best_individual_of_run
                    best_case_run_time_in_operator_combination = i

            # write to file
            log_per_combination(best_case_run_time_in_operator_combination, crossover_operator, mutation_operator)

    log_best_and_worst(best_case_run_time, best_crossover_operator, best_mutation_operator, best_run_fitness,
                       best_run_individual, worst_case_run_time, worst_crossover_operator, worst_mutation_operator,
                       worst_run_fitness, worst_run_individual)

    return [best_crossover_operator, best_mutation_operator, best_run_fitness, best_run_individual,
            best_case_run_time], [worst_crossover_operator, worst_mutation_operator, worst_run_fitness,
                                  worst_run_individual, worst_case_run_time]


def performance_of_best_and_worst(tsp_map: TSPMap, best: list, worst: list):
    # best
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
    tournament_size = 5
    crossover_operator = best[0]
    mutation_operator = best[1]
    K = 20
    N = 5
    M = 1
    log_generations = [i for i in range(0, generations)]
    best_case = TSPGA(tsp_map, population_size, mutation_probability, generations, tournament_size, crossover_operator,
                      mutation_operator, K, N, M, log_generations)
    best_individual = best_case.run()
    log_performance_of_best(best_case, best_individual)

    # worst
    crossover_operator = worst[0]
    mutation_operator = worst[1]
    worst_case = TSPGA(tsp_map, population_size, mutation_probability, generations, tournament_size, crossover_operator,
                       mutation_operator, K, N, M, log_generations)
    worst_individual = worst_case.run()
    log_performance_of_worst(worst_case, worst_individual)

    report_figure(best_case, generations, worst_case)


def varying_values(tsp_map: TSPMap, best: list):
    # First run, Varying the crossover and mutation operators
    case_run_time = 1
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
    tournament_size = 5
    crossover_operator = best[0]
    mutation_operator = best[1]
    # log at every generation
    log_generations = [1000, 5000, 20000]
    cases = [{"K": 10, "N": 5, "M": 1}, {"K": 20, "N": 10, "M": 3}, {"K": 50, "N": 20, "M": 5}]

    for case in cases:
        K = case["K"]
        N = case["N"]
        M = case["M"]
        best_fitness_of_case = None
        best_fitness_run_of_case = None
        for j in range(case_run_time):
            case = TSPGA(tsp_map, population_size, mutation_probability, generations, tournament_size,
                         crossover_operator,
                         mutation_operator, K, N, M, log_generations)
            case_best_individual = case.run()

            if best_fitness_of_case is None or case.best_fitness < best_fitness_of_case:
                best_fitness_of_case = case.best_fitness
                best_fitness_run_of_case = j

            log_varying_values_each_run(K, M, N, best, case, case_best_individual, j)

        log_varying_values_each_case(K, M, N, best_fitness_of_case, best_fitness_run_of_case)


if __name__ == '__main__':
    map = TSPMap()
    map.read("kroA100.tsp")

    best, worst = varying_crossover_mutation_types(map)
    performance_of_best_and_worst(map, best, worst)
    varying_values(map, best)
