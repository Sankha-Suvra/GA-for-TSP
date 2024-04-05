import random
import math
import matplotlib.pyplot as plt
import numpy as np

parent1 = [1,2,3,4,5,6,7,8,9,10]
parent2 = [11,12,13,14,15,16,17,18,19,20]


# def crossover(parent1, parent2):
#     start = random.randint(0, len(parent1) - 2)
#     end = random.randint(start + 1, len(parent1) - 1)

#     child1 = parent1[:]
#     child2 = parent2[:]

#     # Swap genes in mapping section between parents
#     for i in range(start, end):
#         child1[i], child2[i] = child2[i], child1[i]

#     return child1, child2

def crossover(parent1, parent2):
    crossover_point1 = random.randint(1, len(parent1) - 2)
    crossover_point2 = random.randint(1, len(parent1) - 2)

    while crossover_point1 == crossover_point2:
        crossover_point2 = random.randint(1, len(parent1) - 2)

    start_point = min(crossover_point1, crossover_point2)
    end_point = max(crossover_point1, crossover_point2)

    child1 = parent1[:start_point] + parent2[start_point:end_point] + parent1[end_point:]
    child2 = parent2[:start_point] + parent1[start_point:end_point] + parent2[end_point:]

    return child1, child2

print(crossover(parent1,parent2))