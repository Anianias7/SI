import matplotlib.pyplot as plt
import numpy as np

import file
import half_and_fill_crossover as haf
import population as pop
import tournament_selection as tournament
from soulution import best_solution
from swap_two_mutation import mutate
from roullete_selection import roulette


file_name = "had16.txt"
pop_size = 300
gen = 100
Px = 70
Pm = 1
Tour = 5
amount_of_experiments = 5
num_of_individual_genes = file.get_number_of_cols(file_name)
distance = file.get_distance_matrix(file_name)
flow = file.get_flow_matrix(file_name)
result_matrix = np.zeros((4, gen, amount_of_experiments))


for i in range(amount_of_experiments):
    population = pop.create_population(pop_size, num_of_individual_genes)
    evaluated_population = pop.evaluate_individuals_in_population(population, distance, flow)
    best_in_generation = pop.best_in_nth_generation(evaluated_population), 0
    evaluated_generation = pop.evaluate_generation(evaluated_population, 0)
    solution = best_in_generation
    result_matrix[:, 0, i] = evaluated_generation

    for nth_gen in range(1, gen):
        parent_population = roulette(evaluated_population)
        parent_population = tournament.tournament_selection(evaluated_population, Tour)
        parent_population = haf.crossover(parent_population, Px, distance, flow)
        parent_population = mutate(parent_population, Pm, distance, flow)
        evaluated_generation = pop.evaluate_generation(parent_population, nth_gen)
        best_in_generation = pop.best_in_nth_generation(parent_population)
        solution = best_solution(best_in_generation, solution, nth_gen)
        evaluated_population = parent_population
        result_matrix[:, nth_gen, i] = evaluated_generation


plt.xlabel('Generations')
plt.ylabel('Costs')
# plt.errorbar(np.arange(gen), np.average(result_matrix[1, :, :], axis=1), np.std(result_matrix[1, :, :], axis=1), label="Best")
# plt.errorbar(np.arange(gen), np.average(result_matrix[2, :, :], axis=1), np.std(result_matrix[2, :, :], axis=1), label="Avg")
# plt.errorbar(np.arange(gen), np.average(result_matrix[3, :, :], axis=1), np.std(result_matrix[3, :, :], axis=1),  label="Worst")

plt.plot(np.arange(gen), np.average(result_matrix[1, :, :], axis=1), label="Best")
plt.plot(np.arange(gen), np.average(result_matrix[2, :, :], axis=1), label="Avg")
plt.plot(np.arange(gen), np.average(result_matrix[3, :, :], axis=1), label="Worst")
plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)
plt.show()
