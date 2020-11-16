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

__all__ = ['sg']

from typing import Optional, Callable

from ..utils import logging
from ..archive import Archive
from .. import species


def sg(species: species.Species, max_generation: Optional[int] = None):
    num_generation = 0
    archive = Archive()

    # inject stopping conditions (raw)
    stopping_conditions = list()

    if max_generation:
        stopping_conditions.append(lambda: num_generation > max_generation)  # closure!

    if species.fitness_function.best_fitness:
        stopping_conditions.append(
            lambda: archive and next(iter(archive)).fitness >= species.fitness_function.best_fitness)

    while all(not f() for f in stopping_conditions):
        num_generation += 1
        i1 = species.sample()
        i2 = species.sample()
        f1 = species.evaluate(i1)
        f2 = species.evaluate(i2)

        if f1 > f2:
            species.update(winner=i1, loser=i2)
        elif f2 > f1:
            species.update(winner=i2, loser=i1)

        archive_changed = archive.add(i1, f1) or archive.add(i2, f2)
        if archive_changed:
            logging.info(f"** ARCHIVE AT GENERATION {num_generation}")
            for ae in archive:
                logging.info(f"-] {species.genome.genotype_to_str(ae.genotype)}:{ae.fitness}")
