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
from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_notebook

from ..utils import logging, jupyter_support
from ..archive import Archive
from .. import species


def sg(species: species.Species, max_generation: Optional[int] = None, progress: Optional[str] = None):
    num_generation = 0
    archive = Archive()

    # inject stopping conditions (raw)
    stopping_conditions = list()

    if max_generation:
        stopping_conditions.append(lambda: num_generation >= max_generation)  # closure!

    if species.fitness_function.best_fitness:
        stopping_conditions.append(
            lambda: archive and next(iter(archive)).fitness >= species.fitness_function.best_fitness)

    if progress is None and not jupyter_support.is_notebook():
        pbar = tqdm(total=max_generation)
    elif progress is None and jupyter_support.is_notebook():
        pbar = tqdm_notebook(total=max_generation)
    else:
        pbar = None

    while all(not f() for f in stopping_conditions):
        if pbar: pbar.update(1)
        num_generation += 1

        i1 = species.sample()
        i2 = species.sample()
        f1 = species.evaluate(i1)
        f2 = species.evaluate(i2)

        if f1 > f2:
            species.update(winner=i1, loser=i2)
        elif f2 > f1:
            species.update(winner=i2, loser=i1)

        archive_changed = archive.add_generation([[i1, f1], [i2, f2]])
        if archive_changed:
            logging.debug(f"** ARCHIVE AT GENERATION {num_generation} -- SIZE: {len(archive):,}")
            for ae in archive:
                logging.debug(f"-] {species.genome.format_genotype(ae.genotype)}:{ae.fitness}")

    if pbar: pbar.close()
    return archive
