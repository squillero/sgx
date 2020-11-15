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

import sgx


f1 = sgx.fitness.Lexicase([10,  2, 30,  4, 50,  6], fitness_type=sgx.fitness.Approximate, abs_tol=.1)
f2 = sgx.fitness.Lexicase([ 1, 20,  3, 40,  5, 60], fitness_type=sgx.fitness.Approximate, abs_tol=.1)

print(f"{f1} vs. {f2}")
print("==\t", f1 == f2)
print("!=\t", f1 != f2)
print(">>\t", f1 >> f2)

for _ in range (10):
    print(">\t", f1 > f2)

f1 = sgx.fitness.Lexicase2([10,  2, 30,  4, 50,  6], fitness_type=sgx.fitness.Approximate, abs_tol=.1)
