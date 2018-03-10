import random

import cost


def create_individual(number_of_genes):
    genes = list(range(number_of_genes))
    random.shuffle(genes)
    return genes


def create_population(size_of_population, individuals_number_of_genes):
    population = []
    for i in range(size_of_population):
        population.append(create_individual(individuals_number_of_genes))
    return population


def calculate_individual_cost(individual, distance_matrix, flow_matrix):
    connections = cost.__create_connections_list(individual)
    return sum(list(map(lambda x: cost.__calculate_single_flow(x, flow_matrix) *
                                  cost.__calculate_single_distance(x, individual, distance_matrix)
                        , connections)))


def calculate_population_cost(population, distance_matrix, flow_matrix):
    return sum(list(map(lambda individual: calculate_individual_cost(individual, distance_matrix, flow_matrix),
                        population)))


def evaluate_individuals_in_population(population, distance_matrix, flow_matrix):
    return list(
        map(lambda individual: (individual, calculate_individual_cost(individual, distance_matrix, flow_matrix)),
            population))


def best_in_nth_generation(evaluated_population):
    best = min(evaluated_population, key=lambda evaluated_individual: evaluated_individual[1])
    return [best[0], best[1]]


def worst_in_nth_generation(evaluated_population):
    best = max(evaluated_population, key=lambda evaluated_individual: evaluated_individual[1])
    return [best[0], best[1]]


def avg_in_nth_generation(evaluated_population):
    avg = sum(i for _, i in evaluated_population) / float(len(evaluated_population))
    return avg


def evaluate_generation(population, gen):
    return [gen, best_in_nth_generation(population)[1], avg_in_nth_generation(population),
            worst_in_nth_generation(population)[1]]
