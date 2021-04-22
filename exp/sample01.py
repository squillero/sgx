# -*- coding: utf-8 -*-
#############################################################################
#   _________ ____________  ___                                             #
#  /   _____//  _____/\   \/  /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  \_____  \/   \  ___ \     /   THE E(X)TENDED (S)ELFISH (G)ENE ALGORITHM  #
#  /        \    \_\  \/     \   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
# /_________/\________/___/\  \  https://github.com/squillero/sgx           #
#                           \_/                                             #
#                                                                           #
# A quick 'n dirty versatile population-less evolutionary optimizer loosely #
# inspired by a cool interpretation of the Darwinian theory.                #
#                                                                           #
#############################################################################
# Copyright © 2021 Giovanni Squillero. Licensed under the EUPL 1.2.
#############################################################################

PROBLEM_SIZE = 100

from random import shuffle
import sgx

genome = sgx.t.Genome([sgx.allele.Categorical("01") for _ in range(PROBLEM_SIZE)])
genome = sgx.t.Genome([sgx.allele.Boolean() for _ in range(PROBLEM_SIZE)])
fitness_function = sgx.fitness.FitnessFunction(lambda i: sum(i),
                                               best_fitness=len(genome),
                                               type_=sgx.fitness.Scalar)
species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
archive = sgx.algorithms.sg(species, max_generation=100_000)
print(list(archive))

# print("\n\nmulti-values all X's")
# tmp = [sgx.allele.Categorical("abcX") for _ in range(PROBLEM_SIZE)
#       ] + [sgx.allele.Categorical("01X") for _ in range(PROBLEM_SIZE)]
# shuffle(tmp)
# genome = sgx.t.Genome(tmp)
# fitness_function = sgx.fitness.FitnessFunction(lambda i: i.count('X'),
#                                                best_fitness=len(genome),
#                                                type_=sgx.fitness.Scalar)
# species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
#sgx.algorithms.sg(species)

# print("\n\nclassical 2-max")
# genome = sgx.t.Genome([sgx.allele.Categorical(['0', '1']) for _ in range(PROBLEM_SIZE)])
# fitness_function = sgx.fitness.FitnessFunction(lambda i: max(i.count('1'), i.count('0')),
#                                                best_fitness=len(genome),
#                                                type_=sgx.fitness.Scalar)
# species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
#sgx.algorithms.sg(species)

# print("\n\nreversed 1-max (minimization)")
# genome = sgx.t.Genome([sgx.allele.Categorical("01") for _ in range(PROBLEM_SIZE)])
# fitness_function = sgx.fitness.FitnessFunction(lambda i: i.count('1'),
#                                                best_fitness=0,
#                                                type_=sgx.fitness.reversed(sgx.fitness.Scalar))
# species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
#sgx.algorithms.sg(species)

# print("\n\nMO 2-max")
# genome = sgx.t.Genome([sgx.allele.Categorical(['0', '1']) for _ in range(PROBLEM_SIZE)])
# fitness_function = sgx.fitness.FitnessFunction(lambda i: [i.count('1'), i.count('0')],
#                                                best_fitness=[len(genome), len(genome)],
#                                                type_=sgx.fitness.Lexicase)
# species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
#sgx.algorithms.sg(species)
