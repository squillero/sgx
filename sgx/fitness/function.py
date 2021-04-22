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

from typing import Callable, Any, Optional, Type
from collections import abc
import warnings

from .base import Fitness
from .simple import Scalar
from ..base import Genotype
from ..utils import logging


class FitnessFunction(abc.Callable):
    #    def __init__(self, fitness_function: Callable[[Genotype], Fitness], type_: Optional[Fitness.__class__] = Scalar.__class__, best_fitness: Optional[Fitness] = None):
    def __init__(self,
                 fitness_function: Callable[[Genotype], Any],
                 type_: Optional[Type[Fitness]] = Type[Scalar],
                 best_fitness: Optional[Fitness] = None):
        self._fitness_function = fitness_function
        self._fitness_type = type_
        self._best_fitness = type_(best_fitness)

    def __call__(self, genotype: Genotype) -> Fitness:
        return self._fitness_type(self._fitness_function(genotype))

    @property
    def fitness_type(self):
        return self._fitness_type

    @property
    def best_fitness(self):
        return self._best_fitness
