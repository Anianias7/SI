from random import randint, choice
import population as pop


def __should_mutate(percentage):
    return True if randint(1, 100) <= percentage else False


def swap_two_mutation(rated_individual, distance_matrix, flow_matrix):
    return __swap(rated_individual, distance_matrix, flow_matrix)


def __swap(rated_individual, distance_matrix, flow_matrix):
    index_1 = randint(0, len(rated_individual[0]) - 1)
    index_2 = randint(0, len(rated_individual[0]) - 1)
    rated_individual[0][index_1], rated_individual[0][index_2] = rated_individual[0][index_2], rated_individual[0][index_1]
    rated_individual = __update_individual_cost(rated_individual, distance_matrix, flow_matrix)
    return rated_individual


def __update_individual_cost(rated_individual, distance_matrix, flow_matrix):
    individual_cost = pop.calculate_individual_cost(rated_individual[0], distance_matrix, flow_matrix)
    return rated_individual[0], individual_cost


def mutate(population, percentage, distance_matrix, flow_matrix):
    children = []
    for i in range(len(population)):
        if __should_mutate(percentage):
            children.append(swap_two_mutation(population[i], distance_matrix, flow_matrix))
        else:
            children.append(population[i])
    return children




