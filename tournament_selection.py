import random
import population as pop


def choose_individuals_for_tournament(evaluated_population, size):
    return random.sample(evaluated_population, size)


def choose_tournament_winner(evaluated_population, size):
    rated_contestants = choose_individuals_for_tournament(evaluated_population, size)
    best = min(rated_contestants, key=lambda rated_contestant: rated_contestant[1])
    return best


def tournament_selection(evaluated_population, size):
    parents = []
    for i in range(len(evaluated_population)):
        parents.append(choose_tournament_winner(evaluated_population, size))
    return parents

