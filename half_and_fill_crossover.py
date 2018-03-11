from math import ceil
import random
import population as pop


def cross_individual(fst_individual, snd_individual):
    return __take_half(fst_individual[0], __find_half_length(fst_individual[0])) + \
           __take_fill(fst_individual[0], snd_individual[0])


def crossed_individual(fst_individual, evaluated_population, distance_matrix, flow_matrix):
    snd_individual = __find_random_individual(evaluated_population)
    indiv = cross_individual(fst_individual, snd_individual)
    return indiv, __update_individual_cost(indiv, distance_matrix, flow_matrix)


def __update_individual_cost(individual, distance_matrix, flow_matrix):
    individual_cost = pop.calculate_individual_cost(individual, distance_matrix, flow_matrix)
    return individual_cost


def __find_half_length(fst_individual):
    """
    :param fst_individual: [indicidual]
    :return: int
    """
    return ceil(len(fst_individual) / 2)


def __take_half(fst_individual, half_length):
    """
    :param fst_individual: [individual]
    :param half_length: int
    :return: [individual]
    """
    return fst_individual[:half_length]


def __take_fill(fst_individual, snd_individual):
    half = __take_half(fst_individual, __find_half_length(fst_individual))
    return [a for a in snd_individual if a not in half]


def __should_crossover(percentage):
    return True if random.randint(1, 100) <= percentage else False


def __find_random_individual(evaluated_population):
    """
    :param evaluated_population: [([individual], cost), ([individual], cost)]
    :return: ([individual], cost)
    """
    return random.choice(evaluated_population)


def crossover(evaluated_population, percentage, distance_matrix, flow_matrix):
    children = []
    for i in range(len(evaluated_population)):
        if __should_crossover(percentage):
            children.append(crossed_individual(evaluated_population[i], evaluated_population, distance_matrix, flow_matrix))
        else:
            children.append(evaluated_population[i])
    return children



