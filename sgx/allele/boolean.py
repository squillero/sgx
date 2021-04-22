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

from typing import Optional, Sequence, Hashable, Union, Dict, Tuple
from math import isclose, exp

from ..utils import logging
from ..utils.random import SGxRandom

from .base import Allele

DEFAULT_LEARNING_RATE = .001


class Boolean(Allele):

    @staticmethod
    def sigmoid(x: float, k: Optional[float] = 1) -> float:
        """Logistic function with given logistic growth (`k`). See https://en.wikipedia.org/wiki/Logistic_function"""
        return 1 / (1 + exp(-k * x))

    def __init__(self, learning_rate: float = DEFAULT_LEARNING_RATE):
        self._x = 0
        self._k = 1
        self._learning_rate = learning_rate

    def sample(self, sample_type: Optional[str] = Allele.DEFAULT_SAMPLE_TYPE) -> Hashable:
        if sample_type == Allele.SAMPLE_TYPE__SAMPLE:
            return SGxRandom.random() < Boolean.sigmoid(self._x, self._k)
        elif sample_type == Allele.SAMPLE_TYPE__UNIFORM:
            return SGxRandom.random() < .5
        elif sample_type == Allele.SAMPLE_TYPE__MODE:
            self._x > 0
        else:
            assert sample_type in Allele.VALID_SAMPLE_TYPES, f"Unknown sample type: {sample_type!r} vs. {Allele.VALID_SAMPLE_TYPES}"

    def update(self, winner: Hashable, loser: Hashable) -> None:
        if winner and not loser:
            self._x += self._learning_rate
        elif not winner and loser:
            self._x -= self._learning_rate
        assert self.run_paranoia_checks()

    def describe(self) -> str:
        return f'{self._x:.e}>{Boolean.sigmoid(self._x, self._k):.2}'

    def is_valid(self, value: Hashable) -> bool:
        return value in [True, False]

    def run_paranoia_checks(self) -> bool:
        return super().run_paranoia_checks()
