from random import seed, randrange
from math import cos, exp, sqrt, pi, fsum

MIN_X_RANGE = 0.0
MAX_X_RANGE = 1.0
C3 = 2*pi
C2 = 0.2
C1 = 20

def parents_select(population_vector, fitness_vector, population_size):

	#roll that prioritizes best parents
	first_parent_roll = 0.8 ** (randrange(0, 100)/(-5.077) - 1) - 1.2
	second_parent_roll = 0.8 ** (randrange(0, 100)/(-5.077) - 1) - 1.2

	#normalizing for population size
	first_parent_roll = int((first_parent_roll / 100.0) * population_size)
	second_parent_roll = int((second_parent_roll / 100.0) * population_size)

	ordered_fitness_vector = sorted(fitness_vector)

	first_parent = population_vector[fitness_vector.index(ordered_fitness_vector[first_parent_roll])]
	second_parent = population_vector[fitness_vector.index(ordered_fitness_vector[second_parent_roll])]

	return [first_parent, second_parent]


def crossover(parents_vector, pc, crossover_method):
	parents_merge_vector = []
	if crossover_method == 'MEAN':
		for i in range(len(parents_vector[0])):
			parents_merge_vector.append(round(fsum([parents_vector[0][i], parents_vector[1][i]])/len(parents_vector), 4))

	child = parents_vector[0][0:pc] + parents_merge_vector[pc:len(parents_merge_vector)]
	return child


def population_evolve(population_vector, fitness_vector, population_size, crossover_method):
	new_generation = []

	for i in range(population_size):
		selected_parents = parents_select(population_vector, fitness_vector, population_size)
		new_generation.append(crossover(selected_parents, randrange(0,len(population_vector[0])), crossover_method))

	return new_generation


def population_mutate(population_vector, population_size, mutation_rate, mutation_mode, mutation_intensity):
	print "mutate"


def population_init(population_vector, fitness_vector, population_size, individual_dimensions_count):
	seed()

	for i in range(population_size):

		individual_dimensions = []
		for j in range(individual_dimensions_count):
			individual_dimensions.append(randrange(MIN_X_RANGE*100, MAX_X_RANGE*100) / 100.0)

		population_vector.append(individual_dimensions)
		fitness_vector.append(100.0)


def ackley_fitness(population_vector, index, individual_dimensions_count):

	s1 = 0
	s2 = 0
	for j in range (individual_dimensions_count):
		s1 = s1 + (population_vector[index][j] * population_vector[index][j])
		s2 = s2 + (cos(C3*population_vector[index][j]))

	return round(-C1*exp(-C2*sqrt((1.0/individual_dimensions_count)*s1)-exp((1.0/individual_dimensions_count)*s2))+C1+1, 6)


if __name__ == '__main__': population_init(3, population, 2) #ackley_fitness(population, 2, 100, fitness)