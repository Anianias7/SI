import population as pop
from random import random

def calculate_total_inverted_population_cost(evaluated_population):
    return sum(calculate_inverted_population_costs(evaluated_population))


def calculate_inverted_population_costs(evaluated_population):
    return list(map(lambda individual: 1 / individual[1],
                        evaluated_population))


def calculate_rations(evaluated_population):
    total_population_cost = calculate_total_inverted_population_cost(evaluated_population)
    inverted_population_costs = calculate_inverted_population_costs(evaluated_population)
    last_cost = 0
    intervals = []
    for cost in inverted_population_costs:
        ratio = (cost + last_cost)/total_population_cost
        last_cost = cost + last_cost
        intervals.append(ratio)
    return intervals


def roulette(evaluated_population):
    parents = []
    intervals = calculate_rations(evaluated_population)
    for _ in evaluated_population:
        trail_ratio = random()
        i = 0
        while intervals[i] < trail_ratio:
            i += 1
        parents.append(evaluated_population[i])
    return parents









