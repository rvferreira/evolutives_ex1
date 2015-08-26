import sys
import matplotlib.pyplot as plt

from ackley import population_evolve, population_mutate, population_init, ackley_fitness


#simulation parameters
REPRESENTATION = 'REAL'
CROSSOVER = 'MEAN'
MUTATION_RATE = 0.1
MUTATION_EFFECT_MODE = 'PLUS_MINUS'
MUTATION_EFFECT_INTENSITY = 0.01
PARENTS_SELECTION = 'ROULETTE'
INITIAL_POPULATION_SIZE = 500
INITIAL_POPULATION_MODE = 'RANDOM'
INDIVIDUAL_DIMENSIONS_COUNT = 4
LAST_GENERATION = 30

def test_fitness(population_vector, fitness_vector, fitness_function, population_size, individual_dimensions):
	for i in range(population_size):
		fitness_vector[i] = fitness_function(population_vector, i, individual_dimensions)
		if fitness_vector[i] == 0.0:
			return i

	return -1


def main():
	population = []
	fitness = []
	results_by_generation = []

	population_init(population, fitness, INITIAL_POPULATION_SIZE, INDIVIDUAL_DIMENSIONS_COUNT)
	
	for i in range(LAST_GENERATION):

		print 'GENERATION:', i
		zero_fitness_element = test_fitness(population, fitness, ackley_fitness, INITIAL_POPULATION_SIZE, INDIVIDUAL_DIMENSIONS_COUNT)
		if zero_fitness_element != -1:
			print "\nOptimal fitness was found at element", zero_fitness_element
			print population[zero_fitness_element]
			break

		best_fitness_element = fitness.index(min(fitness))
		print "Best fitness for this generation was found to be", fitness[best_fitness_element], "at the element", best_fitness_element
		print population[best_fitness_element]
		print '\n'

		results_by_generation.append(fitness[best_fitness_element])

		population = population_evolve(population, fitness, INITIAL_POPULATION_SIZE, CROSSOVER)
		population_mutate(population, MUTATION_RATE, MUTATION_EFFECT_MODE, MUTATION_EFFECT_INTENSITY)


	if zero_fitness_element == -1:
		best_fitness_element = fitness.index(min(fitness))
		print "Best fitness was found to be", fitness[best_fitness_element], "at the element", best_fitness_element
		print population[best_fitness_element]

	plt.plot(results_by_generation)
	plt.ylabel('Best Fitness')
	plt.xlabel('Generation')
	plt.show()


if __name__ == '__main__': main()