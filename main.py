import sys

REPRESENTATION = 'REAL'
CROSSOVER = 'MEAN'
MUTATION_RATE = 0.1
MUTATION_EFFECT = 0.01
PARENTS_SELECTION = 'ROULETTE'
INITIAL_POPULATION_SIZE = 1
INITIAL_POPULATION_MODE = 'RANDOM'
LAST_GENERATION = 15

population = []
fitness = []

def population_init(population_vector, fitness_vector, initial_size):
	for i in range(INITIAL_POPULATION_SIZE):
		population_vector.append([1.0, 1.1, 1.2])
		fitness_vector.append(1.0)

def ackley_fitness(population_vector, individual_index):
	return round(1.0, 4)

def test_fitness(population_vector, fitness_vector, fitness_function, population_size):
	for i in range(population_size):
		fitness_vector[i] = fitness_function(population_vector, i)
		if fitness_vector[i] == 0.0:
			return i

	return -1

	

def main():
	population_init(population, fitness, INITIAL_POPULATION_SIZE)
	
	for i in range(LAST_GENERATION):

		print 'GENERATION:', i
		zero_fitness_element = test_fitness(population, fitness, ackley_fitness, INITIAL_POPULATION_SIZE)
		if zero_fitness_element != -1:
			print "\nOptimal fitness was found at element", zero_fitness_element
			print population[zero_fitness_element]
			break


		print '\n'

	if zero_fitness_element == -1:
		best_fitness_element = fitness.index(min(fitness))
		print "Best fitness was found to be", fitness[best_fitness_element], "at the element", best_fitness_element
		print population[best_fitness_element]


if __name__ == '__main__': main()