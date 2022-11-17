import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def log_per_combination(best_case_run_time_in_operator_combination, crossover_operator, mutation_operator):
    if not os.path.exists("first_run/" + crossover_operator + "_" + mutation_operator):
        os.makedirs("first_run/" + crossover_operator + "_" + mutation_operator)
    with open("first_run/" + crossover_operator + "_" + mutation_operator + "/results.txt", "w") as f:
        f.write(
            "Best result path: first_run/" + crossover_operator + "_" + mutation_operator + "/results_" + str(
                best_case_run_time_in_operator_combination) + ".txt\n")


def log_per_run(best_individual_of_run, crossover_operator, i, mutation_operator, tsp_ga):
    # write to file
    if not os.path.exists("first_run/" + crossover_operator + "_" + mutation_operator):
        os.makedirs("first_run/" + crossover_operator + "_" + mutation_operator)
    with open("first_run/" + crossover_operator + "_" + mutation_operator + "/results_" + str(i) + ".txt",
              "w") as f:

        for j in range(len(tsp_ga.best_fitnesses)):
            f.write("Generation: " + str(j) + " Best fitness: " + str(
                tsp_ga.best_fitnesses[j]) + " Avarage fitness: " + str(
                tsp_ga.avarage_fitnesses[j]) + " Standard deviation: " + str(
                tsp_ga.standard_deviations[j]) + "\n")

        f.write("Best individual: " + str(best_individual_of_run) + "\n")
        f.write("Best fitness: " + str(tsp_ga.best_fitness) + "\n")
        f.write("Running time: " + str(tsp_ga.running_time) + "\n")
        f.write("Case run: " + str(i) + "\n")


def report_figure(best_case, gen, worst_case):
    # Report results as a figure
    # best
    best_data = pd.DataFrame({'Best fitness': best_case.best_fitnesses, 'Mean fitness': best_case.avarage_fitnesses})
    # best_standart_deviation = pd.DataFrame({'Standard deviation': best_case.standard_deviations})
    p = sns.lineplot(data=best_data)
    # p.fill_between([i for i in range(0, generations)],
    #                y1=best_data['Mean fitness'] - best_standart_deviation['Standard deviation'],
    #                y2=best_data['Mean fitness'] + best_standart_deviation['Standard deviation'], alpha=.5)
    p.set_xlabel("Generation")
    p.set_ylabel("Fitness")
    p.set_ylim(20000, 30000)

    # increase resolution
    fig = p.get_figure()
    fig.savefig("second_run/best_case/best_case.png", dpi=300)

    plt.show()

    # worst
    worst_data = pd.DataFrame({'Best fitness': worst_case.best_fitnesses, 'Mean fitness': worst_case.avarage_fitnesses})
    # worst_standart_deviation = pd.DataFrame({'Standard deviation': worst_case.standard_deviations})
    p = sns.lineplot(data=worst_data)
    # p.fill_between([i for i in range(0, generations)],
    #               y1=worst_data['Mean fitness'] - worst_standart_deviation['Standard deviation'],
    #               y2=worst_data['Mean fitness'] + worst_standart_deviation['Standard deviation'], alpha=.5)
    p.set_xlabel("Generation")
    p.set_ylabel("Fitness")
    # set y axis limit
    p.set_ylim(21200, 30000)

    # increase resolution to 4096x2160
    fig = p.get_figure()
    fig.savefig("second_run/worst_case/worst_case.png", dpi=300)

    plt.show()


def log_performance_of_worst(worst_case, worst_individual):
    # write to file
    if not os.path.exists("second_run/worst_case"):
        os.makedirs("second_run/worst_case")
    with open("second_run/worst_case/results.txt", "w") as f:

        for i in range(len(worst_case.best_fitnesses)):
            f.write("Generation: " + str(i) + " Best fitness: " + str(
                worst_case.best_fitnesses[i]) + " Avarage fitness: " + str(
                worst_case.avarage_fitnesses[i]) + " Standard deviation: " + str(
                worst_case.standard_deviations[i]) + "\n")

        f.write("Best individual: " + str(worst_individual) + "\n")
        f.write("Best fitness: " + str(worst_case.best_fitness) + "\n")
        f.write("Running time: " + str(worst_case.running_time) + "\n")


def log_performance_of_best(best_case, best_individual):
    # write to file
    if not os.path.exists("second_run/best_case"):
        os.makedirs("second_run/best_case")
    with open("second_run/best_case/results.txt", "w") as f:

        for i in range(len(best_case.best_fitnesses)):
            f.write("Generation: " + str(i) + " Best fitness: " + str(
                best_case.best_fitnesses[i]) + " Avarage fitness: " + str(
                best_case.avarage_fitnesses[i]) + " Standard deviation: " + str(
                best_case.standard_deviations[i]) + "\n")

        f.write("Best individual: " + str(best_individual) + "\n")
        f.write("Best fitness: " + str(best_case.best_fitness) + "\n")
        f.write("Running time: " + str(best_case.running_time) + "\n")


def log_varying_values_each_case(K, M, N, best_fitness_of_case, best_fitness_run_of_case):
    # write to file
    if not os.path.exists("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M)):
        os.makedirs("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M))
    with open("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M) + "/best_result.txt",
              "w") as f:
        f.write("Best fitness of case: " + str(best_fitness_of_case) + "\n")
        f.write(
            "Best run path: third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M) + "/result_" + str(
                best_fitness_run_of_case) + ".txt\n")


def log_varying_values_each_run(K, M, N, best, case, case_best_individual, j):
    # write to file
    if not os.path.exists("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M)):
        os.makedirs("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M))
    with open("third_run/varying_values_K" + str(K) + "_N" + str(N) + "_M" + str(M) + "/result_" + str(
            j) + ".txt",
              "w") as f:

        for i in range(len(case.best_fitnesses)):
            f.write("Generation: " + str(i) + " Best fitness: " + str(
                case.best_fitnesses[i]) + " Avarage fitness: " + str(
                case.avarage_fitnesses[i]) + " Standard deviation: " + str(
                case.standard_deviations[i]) + "\n")

        f.write("Best individual: " + str(case_best_individual) + "\n")
        f.write("Best fitness: " + str(case.best_fitness) + "\n")
        f.write("Running time: " + str(case.running_time) + "\n")
        f.write("Percentage of improvement over the best case: " + str(
            (case.best_fitness - best[2]) / best[2] * -100) + "%\n")


def log_best_and_worst(best_case_run_time, best_crossover_operator, best_mutation_operator, best_run_fitness,
                       best_run_individual, worst_case_run_time, worst_crossover_operator, worst_mutation_operator,
                       worst_run_fitness, worst_run_individual):
    # write to file
    with open("first_run/results.txt", "w") as f:
        f.write("Best crossover operator: " + str(best_crossover_operator) + "\n")
        f.write("Best mutation operator: " + str(best_mutation_operator) + "\n")
        f.write("Best run fitness: " + str(best_run_fitness) + "\n")
        f.write("Best run individual: " + str(best_run_individual) + "\n")
        f.write("Best case run time: " + str(best_case_run_time) + "\n")
        f.write(
            "Best result path: first_run/" + best_crossover_operator + "_" + best_mutation_operator + "/results_" + str(
                best_case_run_time) + ".txt\n")
        f.write("Worst crossover operator: " + str(worst_crossover_operator) + "\n")
        f.write("Worst mutation operator: " + str(worst_mutation_operator) + "\n")
        f.write("Worst run fitness: " + str(worst_run_fitness) + "\n")
        f.write("Worst run individual: " + str(worst_run_individual) + "\n")
        f.write("Worst case run time: " + str(worst_case_run_time) + "\n")
        f.write(
            "Worst result path: first_run/" + worst_crossover_operator + "_" + worst_mutation_operator + "/results_" + str(
                worst_case_run_time) + ".txt\n")


def log_improving_performance_each_run( case, case_best_individual, j):
    # write to file
    if not os.path.exists("fourth_run/"):
        os.makedirs("fourth_run/")
    with open("fourth_run/result_" + str(j) + ".txt",
              "w") as f:

        for i in range(len(case.best_fitnesses)):
            f.write("Generation: " + str(i) + " Best fitness: " + str(
                case.best_fitnesses[i]) + " Avarage fitness: " + str(
                case.avarage_fitnesses[i]) + " Standard deviation: " + str(
                case.standard_deviations[i]) + "\n")

        f.write("Best individual: " + str(case_best_individual) + "\n")
        f.write("Best fitness: " + str(case.best_fitness) + "\n")
        f.write("Running time: " + str(case.running_time) + "\n")


def log_improving_performance_best_case(case, best_fitness_of_case, best_fitness_run_of_case):
    # write to file
    if not os.path.exists("fourth_run/"):
        os.makedirs("fourth_run/")
    with open("fourth_run/best_result.txt",
              "w") as f:
        f.write("Best fitness of case: " + str(best_fitness_of_case) + "\n")
        f.write(
            "Best run path: fourth_run/result_" + str(
                best_fitness_run_of_case) + ".txt\n")


def report_best_figure(best_run):
    data = pd.DataFrame({"Best fitness": best_run.best_fitnesses, "Mean fitness": best_run.avarage_fitnesses})
    p = sns.lineplot(data=data)
    p.set_xlabel("Generation")
    p.set_ylabel("Fitness")
    p.set_ylim(20000, 25000)

    # increase resolution
    fig = p.get_figure()
    fig.savefig("fourth_run/best_case.png", dpi=300)

    plt.show()
