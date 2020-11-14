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

from typing import Tuple, Sequence, Any, Callable, Optional
from .utils import logging
from .base import Genome, Genotype
from .allele.base import Allele


class Species:
    def __init__(self, genome: Sequence[Any], fitness_function: Optional[Callable[[Sequence[Allele]], Any]] = None,
                 compare_function: Optional[Callable[[Sequence[Allele],Sequence[Allele]], bool]] = None) -> None:
        assert not ( fitness_function and compare_function), "Can't specify both fitness and compare functions"
        assert fitness_function or compare_function, "Either fitness or compare function must be specified"

        self._genome = Genome(genome)
        if compare_function:
            self._compare_function = compare_function
        else:
            self._compare_function = lambda i1, i2: fitness_function(i1) > fitness_function(i2)

    @property
    def mode(self) -> Genotype:
        return Genotype(a.mode for a in self._genome)

    @property
    def genome(self) -> Genome:
        return Genome(self._genome)

    def sample(self, mutation_rate: Optional[float]) -> Genotype:
        return Genotype(a.sample(mutation_rate) for a in self._genome)

    def compare(self, ind1: Genotype, ind2: Genotype):
        return self._compare_function(ind1, ind2)
