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

from typing import final
from abc import abstractmethod
from ..base import Pedantic, Paranoid

class Fitness(Pedantic, Paranoid):
    """Fitness of a phenotype, handle multiple formats (eg. scalar, tuple). The class also redefines the relational
    operator in order to handle different types of optimization (eg. maximization, minimization) and to provide limited
    support to more complex scenarios (eg. multi-objective optimization)

    One-character operators represent approximate (uncertain) relationships: is_better (`x > y`), is_worse (`x < y`)

    Two-character operators represent exact relationships: is_equal (`x == y`), is_different (`x != y`),
    dominates (`x >> y`), and is_dominated (`x << y`),

    Note: Two-character operators denoting weak inequalities should not be used: `x <= y` and `x >= y`

    When subclassing, one may only redefine is_better (`x > y`), dominates (`x >> y`), and is_equal (`x == y`)
    """

    # NON-EXACT

    @abstractmethod
    def __gt__(self, other: 'Fitness') -> bool:
        """f1 is better than f2 (may be approximate or accidental)"""
        logging.debug("__gt__")
        return super().__gt__(other)

    @final
    def __lt__(self, other: 'Fitness') -> bool:
        """f1 is worse than f2 (may be approximate or accidental)"""
        logging.debug("__lt__")
        return not (self > other or self == other)

    # EXACT

    @abstractmethod
    def __eq__(self, other: 'Fitness') -> bool:
        """f1 is equal to f2"""
        logging.debug("__eq__")
        return super().__eq__(other)

    @final
    def __ne__(self, other: 'Fitness') -> bool:
        """f1 is different from f2"""
        logging.debug("__ne__")
        return not self == other

    def __rshift__(self, other: 'Fitness') -> bool:
        """f1 domintes f2"""
        return self > other

    def __lshift__(self, other: 'Fitness') -> bool:
        """f1 is dominated by f2"""
        return self < other

    # NOT TO BE USE

    @final
    def __ge__(self, other: 'Fitness') -> None:
        """Weak inequalities between fitness values should not be used"""
        #warnings.warn("Functions is going to be removed", DeprecationWarning, stacklevel=2)
        logging.debug("__ge__")
        raise NotImplementedError

    @final
    def __le__(self, other: 'Fitness') -> None:
        """Weak inequalities between fitness values should not be used"""
        #warnings.warn("Functions is going to be removed", DeprecationWarning, stacklevel=2)
        logging.debug("__le__")
        raise NotImplementedError

    def run_paranoia_checks(self) -> bool:
        return super().run_paranoia_checks()

    # SPARE CUSTOMIZATION
    def __str__(self):
        return f"<f:{super().__str__()}>"


def reversed(fitness_class: 'Fitness') -> 'Fitness':
    """Reverse fitness class turning a maximization problem into a minimization one"""
    assert isinstance(fitness_class, type), f"Only <class 'sgx.t.Fitness'> can be reversed. Found an object of type {type(fitness_class)}."
    assert issubclass(fitness_class, Fitness), f"Only <class 'sgx.t.Fitness'> can be reversed. Found {fitness_class}."
    class r(fitness_class):
        def __gt__(self, other: 'Fitness') -> bool:
            return fitness_class(self) < fitness_class(other)
        def __rshift__(self, other: 'Fitness') -> bool:
            return fitness_class(self) << fitness_class(other)
        def __lshift__(self, other: 'Fitness') -> bool:
            return fitness_class(self) >> fitness_class(other)
    return r
