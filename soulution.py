from population import best_in_nth_generation


def best_solution(best_in_generation, solution, gen):
    best = best_in_generation
    if best[1] < solution[0][1]:
        return best, gen
    else:
        return solution



def display(lista):
    for p in lista: print(p)
