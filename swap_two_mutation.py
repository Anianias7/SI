from random import randint, choice


def __should_mutate(percentage):
    return True if randint(1, 100) <= percentage else False


def swap_two_mutation(individual):
    return __swap(individual)


def __swap(individual):
    index_1 = randint(0, len(individual) - 1)
    index_2 = randint(0, len(individual) - 1)
    individual[index_1], individual[index_2] = individual[index_2], individual[index_1]
    return individual


def mutate(population, percentage):
    children = []
    for i in range(len(population)):
        if __should_mutate(percentage):
            children.append(swap_two_mutation(population[i]))
        else:
            children.append(population[i])
    return children




