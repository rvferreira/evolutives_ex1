from random import seed, randrange
from math import cos, exp, sqrt, pi

MIN_X_RANGE = 0.0
MAX_X_RANGE = 1.0
C3 = 2*pi
C2 = 0.2
C1 = 20

def population_evolve(population_vector, population_size, crossover_method):
	print "evolve"


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