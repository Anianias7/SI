import random
import population as pop


def choose_individuals_for_tournament(population, size):
    return random.sample(population, size)


def rate_contestants(population, size, distance_matrix, flow_matrix):
    contestants = choose_individuals_for_tournament(population, size)
    return list(map(lambda x: (x, pop.calculate_individual_cost(x, distance_matrix, flow_matrix)), contestants))


def choose_tournament_winner(population, size, distance_matrix, flow_matrix):
    rated_contestants = rate_contestants(population, size, distance_matrix, flow_matrix)
    best = min(rated_contestants, key=lambda rated_contestant: rated_contestants[1])
    return best[0]


def tournament_selection(population, size, distance_matrix, flow_matrix):
    parents = []
    for i in range(len(population)):
        parents.append(choose_tournament_winner(population, size, distance_matrix, flow_matrix))
    return parents

