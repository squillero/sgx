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


def sg(species: species.Species, format_function: Optional[Callable] = None):
    if format_function is None:
        format_function = lambda x: f'{x}'

    num_generation = 0
    archive = Archive()

    stopping_conditions = list()
    stopping_conditions.append(lambda: num_generation > 2500)    # closure!

    while all(not f() for f in stopping_conditions):
        num_generation += 1
        i1 = species.sample()
        i2 = species.sample()
        f1 = species.evaluate(i1)
        f2 = species.evaluate(i2)

        archive.add(i1, f1)
        archive.add(i2, f2)

        if f1 > f2:
            species.update(winner=i1, loser=i2)
        elif f2 > f1:
            species.update(winner=i2, loser=i1)
