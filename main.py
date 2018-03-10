import matplotlib.pyplot as plt
import numpy as np

import file
import half_and_fill_crossover as haf
import population as pop
import tournament_selection as tournament
from soulution import best_solution
from swap_two_mutation import mutate


file_name = "had20.txt"
pop_size = 100
gen = 50
Px = 70
Pm = 0.1
Tour = 5
amount_of_experiments = 4
num_of_individual_genes = file.get_number_of_cols(file_name)
distance = file.get_distance_matrix(file_name)
flow = file.get_flow_matrix(file_name)
result_matrix = np.zeros((gen, 4))
experiment_best = np.zeros((gen, amount_of_experiments))

##BASE GENERATION
population = pop.create_population(pop_size, num_of_individual_genes)
eval_individuals = pop.evaluate_individuals_in_population(population, distance, flow)
best_in_generation = pop.best_in_nth_generation(eval_individuals), 0
evaluated_generation = pop.evaluate_generation(eval_individuals, 0).append(best_in_generation)
solution = best_in_generation
result_matrix[0] = evaluated_generation


for nth_gen in range(1, gen):
    parent_population = tournament.tournament_selection(population, Tour, distance, flow)
    parent_population = haf.crossover(parent_population, Px)
    parent_population = mutate(parent_population, Pm)
    evaluated_new_population = pop.evaluate_individuals_in_population(parent_population, distance, flow)
    evaluated_generation = pop.evaluate_generation(evaluated_new_population, nth_gen)
    result_matrix[nth_gen] = evaluated_generation
    best_in_generation = pop.best_in_nth_generation(evaluated_new_population)
    print(best_in_generation)

    solution = best_solution(best_in_generation, solution, nth_gen)

    print(solution)

    population = parent_population

plt.xlabel('Generations')
plt.ylabel('Costs')
plt_best = plt.plot(np.arange(gen), result_matrix[:, 1], label="Best")
# plt_avg = plt.plot(np.arange(gen), result_matrix[:, 2], label="Avg")
# plt_worst = plt.plot(np.arange(gen), result_matrix[:, 3], label="Worst")
# plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)
plt.show()
