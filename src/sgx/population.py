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
from .allele.abc import Allele


class Population:
    def __init__(self, genome: Sequence[Allele], fitness_function: Optional[Callable[[Sequence[Allele]], Any]] = None,
                 compare_function: Optional[Callable[[Sequence[Allele],Sequence[Allele]], bool]] = None) -> None:
        assert not ( fitness_function and compare_function), "Can't specify both fitness and compare functions"
        assert fitness_function or compare_function, "Either fitness or compare function must be specified"

        self._genome = tuple(genome)
        self._compare_function = None
        self._fitness_function = None
        if fitness_function:
            self._fitness_function = fitness_function
        else:
            self._compare_function = compare_function


    @property
    def mode(self) -> Tuple[Any]:
        return tuple(a.mode for a in self._genome)

    def sample(self, mutation_rate: Optional[float]) -> Tuple[Any]:
        return tuple(a.sample(mutation_rate) for a in self._genome)

    def compare(self, ind1: Sequence[Allele], ind2: Sequence[Allele]):
        if self._compare_function:
            return self._compare_function(ind1, ind2)
        else:
            return self._fitness_function(ind1) > self._fitness_function(ind2)