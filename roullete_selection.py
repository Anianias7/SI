import population as pop


def __calculate_population_cost(population, distance_matrix, flow_matrix):
    return sum(list(map(lambda individual: 1 / pop.calculate_individual_cost(individual, distance_matrix, flow_matrix),
                        population)))

