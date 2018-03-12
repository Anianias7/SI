import matplotlib.pyplot as plt
import numpy as np

import file
import population as pop

file_name = "had12.dat.txt"
num_of_individual_genes = file.get_number_of_cols(file_name)
distance = file.get_distance_matrix(file_name)
flow = file.get_flow_matrix(file_name)


def find_random_individual(num_of_genes):
    return pop.create_individual(num_of_genes)


def calculate_random_individual_cost(individual, distance_matrix, flow_matrix):
    return pop.calculate_individual_cost(individual, distance_matrix, flow_matrix)


def random_individual(num_of_genes, distance_matrix, flow_matrix):
    individual = find_random_individual(num_of_genes)
    cost = calculate_random_individual_cost(individual, distance_matrix, flow_matrix)
    return individual, cost


def random_search(num_of_genes, distance_matrix, flow_matrix, gen):
    bests = []
    best = random_individual(num_of_genes, distance_matrix, flow_matrix)
    bests.append(best[1])
    for i in range(gen - 1):
        candidate = random_individual(num_of_genes, distance_matrix, flow_matrix)
        if candidate[1] < best[1]:
            best = candidate
        bests.append(best[1])

    return best, bests


r = random_search(num_of_individual_genes, distance, flow, 100)
print(r[1])
#
plt.plot(np.arange(100), r[1], label="Best")
plt.show()
