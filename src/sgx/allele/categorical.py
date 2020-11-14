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

from ..utils import logging
from ..utils.random import SGxRandom

from .base import Allele


class Boolean(Allele):
    DEFAULT_SCALE = .001

    def __init__(self, scale: float = DEFAULT_SCALE):
        assert 0 <= scale < 1, "Illegal scale"
        self._loc = .5
        self._scale = scale

    @property
    def loc(self) -> float:
        return self._loc

    @property
    def scale(self) -> float:
        return self._scale

    @property
    def mode(self) -> bool:
        return self._loc < .5

    def sample(self, mutation_rate: float) -> bool:
        if SGxRandom.random() < mutation_rate:
            return SGxRandom.choice([True, False])
        else:
            return SGxRandom.random() < self.loc

    def update(self, winner: bool, loser: bool) -> None:
        if winner is True and loser is False:
            self._loc += self._scale
        elif winner is False and loser is True:
            self._loc -= self._scale

        self._loc = max(0, self._loc)
        self._loc = min(1, self._loc)
