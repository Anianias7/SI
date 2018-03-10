from math import ceil
import random


def cross(fst_individual, snd_individual):
    return __take_half(fst_individual, __find_half_length(fst_individual)) + \
           __take_fill(fst_individual, snd_individual)


def __find_half_length(fst_individual):
    return ceil(len(fst_individual) / 2)


def __take_half(fst_individual, half_length):
    return fst_individual[:half_length]


def __take_fill(fst_individual, snd_individual):
    half = __take_half(fst_individual, __find_half_length(fst_individual))
    return [a for a in snd_individual if a not in half]


def __should_crossover(percentage):
    return True if random.randint(1, 100) <= percentage else False


def __find_random_individual(population):
    return random.choice(population)


def crossover(population, percentage):
    children = []
    for i in range(len(population)):
        if __should_crossover(percentage):
            children.append(cross(population[i], __find_random_individual(population)))
        else:
            children.append(population[i])
    return children



