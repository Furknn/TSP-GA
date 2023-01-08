import random
import time

from TSPMap import TSPMap
from TSPGA import TSPGA
from TSPSA import TSPSA

from logs import *


def varying_crossover_mutation_types(tsp_map: TSPMap):
    # First run, Varying the crossover and mutation operators
    case_run_time = 10
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
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
            log_per_combination_k_n_m(best_case_run_time_in_operator_combination, crossover_operator, mutation_operator)

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
    case_run_time = 20
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
    tournament_size = 5
    crossover_operator = best[0]
    mutation_operator = best[1]
    # log at every generation
    log_generations = [1000, 5000, 20000]
    K = [10, 20, 50]
    N = [5, 10, 20]
    M = [1, 3, 5]

    for k in K:
        for n in N:
            for m in M:
                best_run_fitness_in_operator_combination = None
                best_run_individual_in_operator_combination = None
                best_case_run_time_in_operator_combination = None

                for i in range(case_run_time):
                    tsp_ga = TSPGA(tsp_map, population_size, mutation_probability, generations, tournament_size,
                                   crossover_operator, mutation_operator, k, n, m, log_generations)
                    best_individual_of_run = tsp_ga.run()

                    log_varying_values_each_run(k, m, n, best, tsp_ga, best_individual_of_run, i)

                    # check if best fitness of run is better than the best fitness of all runs in operator combination
                    if best_run_fitness_in_operator_combination is None or best_run_fitness_in_operator_combination > tsp_ga.best_fitness:
                        best_run_fitness_in_operator_combination = tsp_ga.best_fitness
                        best_run_individual_in_operator_combination = best_individual_of_run
                        best_case_run_time_in_operator_combination = i

                # write to file
                log_varying_values_each_case(k, m, n, best_run_fitness_in_operator_combination,
                                             best_case_run_time_in_operator_combination)


def improving_performance(map, best: None):
    case_run_time = 100
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
    tournament_size = 5
    crossover_operator = "CSOX"  # best[0]
    mutation_operator = "IVM"  # best[1]
    K = 50
    N = 20
    M = 5

    # log at every 100 generations
    log_generations = [i for i in range(0, generations, 100)]
    best_run = None
    best_fitness_of_case = None
    best_fitness_run_of_case = None

    for j in range(case_run_time):
        case = TSPGA(map, population_size, mutation_probability, generations, tournament_size,
                     crossover_operator,
                     mutation_operator, K, N, M, log_generations, True)
        case_best_individual = case.run()

        if best_fitness_of_case is None or case.best_fitness < best_fitness_of_case:
            best_fitness_of_case = case.best_fitness
            best_fitness_run_of_case = j
            best_run = case

        log_improving_performance_each_run(case, case_best_individual, j)

    log_improving_performance_best_case(best_run, best_fitness_of_case, best_fitness_run_of_case)

    report_best_figure(best_run)


def SAwithDiffrentCoolingSchedules(tsp_map: TSPMap):
    # random initial solution
    initial_solution = [i for i in range(tsp_map.size)]
    random.shuffle(initial_solution)
    # Set the number of runs for each case
    num_runs = 100

    params = [{"cooling_rate": 0.95, "iterations_per_temp": 10, "initial_temp": 10000,
               "stopping_temp": 0.01},
              {"cooling_rate": 0.995, "iterations_per_temp": 2, "initial_temp": 10000,
               "stopping_temp": 0.01}]

    outputs = [
        {"average_fitness": 0.0, "best_solution": [], "fitness_per_run": [], "running_time_per_run": [],
         "best_fitness_index": 0, "best_fitness": 0.0, "complete_time": 0.0, "best_solution_fitnesses": []},
        {"average_fitness": 0.0, "best_solution": [], "fitness_per_run": [], "running_time_per_run": [],
         "best_fitness_index": 0, "best_fitness": 0.0, "complete_time": 0.0, "best_solution_fitnesses": []}
    ]

    # Run the first case num_runs times
    for j in range(len(params)):
        param = params[j]

        for i in range(num_runs):
            start_time = time.time()

            sa = TSPSA(tsp_map=tsp_map, initial_solution=initial_solution, initial_temperature=param["initial_temp"],
                       stopping_temperature=param["stopping_temp"], cooling_rate=param["cooling_rate"],
                       equilibrium_state=param["iterations_per_temp"], preserve_best=True)

            sa.run()

            outputs[j]["fitness_per_run"].append(sa.best_fitness)
            outputs[j]["running_time_per_run"].append(time.time() - start_time)
            if outputs[j]["best_fitness"] == 0 or outputs[j]["best_fitness"] > sa.best_fitness:
                outputs[j]["best_fitness"] = sa.best_fitness
                outputs[j]["best_solution"] = sa.best_solution
                outputs[j]["best_fitness_index"] = i
                outputs[j]["best_solution_fitnesses"] = sa.fitnesses

            log_sa_each_run(sa, i, param["cooling_rate"], param["iterations_per_temp"])

        outputs[j]["average_fitness"] = sum(outputs[j]["fitness_per_run"]) / len(outputs[j]["fitness_per_run"])
        outputs[j]["running_time"] = sum(outputs[j]["running_time_per_run"]) / len(outputs[j]["running_time_per_run"])
        outputs[j]["complete_time"] = sum(outputs[j]["running_time_per_run"])

        log_sa_each_case(outputs[j], param["cooling_rate"], param["iterations_per_temp"])
        report_sa_each_case(outputs[j]["best_solution_fitnesses"], param["cooling_rate"], param["iterations_per_temp"])


def CompareSAwithGA(tsp_map):
    # random initial solution
    initial_solution = [i for i in range(tsp_map.size)]
    random.shuffle(initial_solution)
    # Set the number of runs for each case
    num_runs = 100

    sa_params = {"cooling_rate": 0.9995, "iterations_per_temp": 10, "initial_temp": 100000,
                 "stopping_temp": 0.001}

    sa_outputs = {"average_fitness": 0.0, "best_solution": [], "fitness_per_run": [], "running_time_per_run": [],
                  "best_fitness_index": 0, "best_fitness": 0.0, "complete_time": 0.0, "best_solution_fitnesses": []}

    ga_params = {"population_size": 50, "mutation_probability": 0.3, "generations": 20000, "tournament_size": 5,
                 "crossover_operator": "PMX", "mutation_operator": "SM"}

    ga_outputs = {"average_fitness": 0.0, "best_solution": [], "fitness_per_run": [], "running_time_per_run": [],
                  "best_fitness_index": 0, "best_fitness": 0.0, "complete_time": 0.0, "best_solution_fitnesses": []}

    for i in range(num_runs):
        start_time = time.time()

        sa = TSPSA(tsp_map=tsp_map, initial_solution=initial_solution, initial_temperature=sa_params["initial_temp"],
                   stopping_temperature=sa_params["stopping_temp"], cooling_rate=sa_params["cooling_rate"],
                   equilibrium_state=sa_params["iterations_per_temp"], preserve_best=True)

        sa.run()

        sa_outputs["fitness_per_run"].append(sa.best_fitness)
        sa_outputs["running_time_per_run"].append(time.time() - start_time)
        if sa_outputs["best_fitness"] == 0 or sa_outputs["best_fitness"] > sa.best_fitness:
            sa_outputs["best_fitness"] = sa.best_fitness
            sa_outputs["best_solution"] = sa.best_solution
            sa_outputs["best_fitness_index"] = i
            sa_outputs["best_solution_fitnesses"] = sa.fitnesses

        ga = TSPGA(tsp_map=tsp_map, population_size=ga_params["population_size"],
                   mutation_probability=ga_params["mutation_probability"], generations=ga_params["generations"],
                   tournament_size=ga_params["tournament_size"], crossover_operator=ga_params["crossover_operator"],
                   mutation_operator=ga_params["mutation_operator"],
                   log_generations=[a for a in range(ga_params["generations"])])

        ga.run_time_limit(sa_outputs["running_time_per_run"][-1], True)
        ga_outputs["fitness_per_run"].append(ga.best_fitness)
        ga_outputs["running_time_per_run"].append(time.time() - start_time)
        if ga_outputs["best_fitness"] == 0 or ga_outputs["best_fitness"] > ga.best_fitness:
            ga_outputs["best_fitness"] = ga.best_fitness
            ga_outputs["best_solution"] = ga.best_individual
            ga_outputs["best_fitness_index"] = i
            ga_outputs["best_solution_fitnesses"] = ga.best_fitnesses

        log_sa_vs_ga_each_run(sa, ga, i)

    sa_outputs["average_fitness"] = sum(sa_outputs["fitness_per_run"]) / len(sa_outputs["fitness_per_run"])
    sa_outputs["running_time"] = sum(sa_outputs["running_time_per_run"]) / len(sa_outputs["running_time_per_run"])
    sa_outputs["complete_time"] = sum(sa_outputs["running_time_per_run"])

    ga_outputs["average_fitness"] = sum(ga_outputs["fitness_per_run"]) / len(ga_outputs["fitness_per_run"])
    ga_outputs["running_time"] = sum(ga_outputs["running_time_per_run"]) / len(ga_outputs["running_time_per_run"])
    ga_outputs["complete_time"] = sum(ga_outputs["running_time_per_run"])

    log_sa_vs_ga(sa_outputs, ga_outputs)

    report_sa_vs_ga(sa_outputs["best_solution_fitnesses"], ga_outputs["best_solution_fitnesses"])


if __name__ == '__main__':
    tsp_map = TSPMap()
    tsp_map.read("kroA100.tsp")

    # Project 1
    # best, worst = varying_crossover_mutation_types(tsp_map)
    # performance_of_best_and_worst(tsp_map, best, worst)
    # best = ["OX", "IVM", 21346.283044622232, 0.0, 0.0]
    # varying_values(tsp_map, best)
    # improving_performance(tsp_map, None)

    # Project 2
    SAwithDiffrentCoolingSchedules(tsp_map)
    CompareSAwithGA(tsp_map)

    # percentage of improvement
    # from
    val1 = 21294
    # to
    val2 = 21282

    print((val1 - val2) / val1 * 100)
