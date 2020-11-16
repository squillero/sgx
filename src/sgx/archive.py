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

from collections import namedtuple

from .utils import logging
from .base import Paranoid, Genotype, Tuple
from .fitness.base import Fitness


class Archive(Paranoid):
    """Archive of best solutions so far"""

    Element = namedtuple('Element', 'genotype fitness')

    def __init__(self):
        self._archive = set()

    def add(self, genotype: Genotype, fitness: Fitness) -> bool:
        """Add a new solution to Archive, return True if really added."""
        assert isinstance(genotype, Genotype), f"Only a Genotype can be added to the archive: {type(genotype)}"
        assert isinstance(fitness, Fitness), f"Only a Fitness can be added to the archive: {type(fitness)}"

        new_element = Archive.Element(genotype, fitness)
        if new_element in self._archive or any(ae.fitness >> fitness for ae in self._archive):
            return False
        else:
            new_set = {new_element}
            for old in self._archive:
                if not any(new.fitness >> old.fitness for new in new_set):
                    new_set.add(old)
            self._archive = new_set
            return True

    def items(self):
        return set(self._archive)

    def __len__(self):
        return len(self._archive)

    def __bool__(self):
        return bool(self._archive)

    def __iter__(self):
        return iter([e for e in self._archive])

    def run_paranoia_checks(self) -> bool:
        return True
