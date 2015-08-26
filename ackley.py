from random import seed, randrange
from math import cos, exp, sqrt, pi

population = []
MIN_X_RANGE = 0.0
MAX_X_RANGE = 1.0
INDIVIDUAL_DIMENSIONS_COUNT = 2
POPULATION_SIZE = 100
C3 = 2*pi
C2 = 0.2
C1 = 20

def population_init(population_size, population_vector, individual_dimensions_count):
	seed()

	for i in range(population_size):

		individual_dimensions = []
		for j in range(individual_dimensions_count):
			individual_dimensions.append(randrange(MIN_X_RANGE*100, MAX_X_RANGE*100) / 100.0)

		population_vector.append(individual_dimensions)
		print population_vector[-1]
	fitness = []
	ackley_fitness(population_vector, individual_dimensions_count, population_size, fitness)



def ackley_fitness(population_vector, individual_dimensions_count, index):

	s1 = 0
	s2 = 0
	for j in range (individual_dimensions_count):
		s1 = s1 + (population_vector[i][j] * population_vector[i][j])
		s2 = s2 + (cos(C3*population_vector[i][j]))

	return (-C1*exp(-C2*sqrt((1.0/individual_dimensions_count)*s1)-exp((1.0/individual_dimensions_count)*s2))+C1+1)


if __name__ == '__main__': population_init(3, population, 2) #ackley_fitness(population, 2, 100, fitness)