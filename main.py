from TSPMap import TSPMap
from TSPGA import TSPGA

if __name__ == '__main__':
    map = TSPMap()
    map.read("kroA100.tsp")

    case_run_time = 100
    population_size = 50
    mutation_probability = 0.1
    generations = 20000
    tournament_size = 5
    crossover_operators = ["PMX", "OX"]
    mutation_operators = ["SM", "IM", "IVM"]
    K = 20
    N = 5
    M = 1
    log_generations = [1000, 5000, 20000]

    best_crossover_and_mutation = []
    best_crossover_and_mutation_fitness = 0

    for crossover_operator in crossover_operators:
        for mutation_operator in mutation_operators:
            for i in range(case_run_time):
                ga = TSPGA(map, population_size, mutation_probability, generations, tournament_size, crossover_operator,
                           mutation_operator, K, N, M, log_generations)
                ga.run()
                if ga.best_fitness > best_crossover_and_mutation_fitness:
                    best_crossover_and_mutation_fitness = ga.best_fitness
                    best_crossover_and_mutation = [crossover_operator, mutation_operator]

    print("Best crossover operator: " + best_crossover_and_mutation[0])
    print("Best mutation operator: " + best_crossover_and_mutation[1])
    print("------------------------")
