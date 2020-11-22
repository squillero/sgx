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

# Copyright 2020 Giovanni Squillero
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

PROBLEM_SIZE = 100

from random import shuffle
import sgx

genome = sgx.t.Genome([sgx.allele.Categorical("01") for _ in range(PROBLEM_SIZE)])
fitness_function = sgx.fitness.FitnessFunction(lambda i: i.count('1'),
                                               best_fitness=len(genome),
                                               type_=sgx.fitness.Scalar)
species = sgx.t.Species(genome=genome, fitness_function=fitness_function)
sgx.algorithms.sg(species, max_generation=1000)

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
