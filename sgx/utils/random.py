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

from typing import Sequence, Any, Optional, Tuple
import random


class Random:

    def __init__(self, seed: Optional = None, state: Optional[Tuple] = None):
        assert not (seed and state), "Can't set both seed and state"
        self._random = random.Random()
        if state:
            self._random.setstate(state)
        else:
            self._random.seed(seed)

    def random(self) -> float:
        """Return a random value in the interval [0, 1)."""
        return self._random.random()

    def choice(self, population: Sequence[Any], weights: Optional[Sequence[float]] = None) -> Any:
        """Return a random element from a non-empty population with optional relative weights."""
        return self._random.choices(population, weights=weights, k=1)[0]

    def shuffled(self, population: Sequence[Any]) -> Sequence[Any]:
        """Return a new list containing all items from the iterable in random order."""
        return self._random.sample(population, len(population))


SGxRandom = Random()
