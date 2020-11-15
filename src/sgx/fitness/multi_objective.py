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

from random import shuffle
from .simple import Vector


class Lexicase(Vector):
    """Pseudo-MO through Lexicase selection (DOI:10.1109/TEVC.2014.2362729)"""

    def is_fitter(self, other: 'Lexicase') -> bool:
        self.check_comparable(other)
        order = list(range(len(self._values)))
        shuffle(order)
        logging.debug(f"{[self._values[i] for i in order]} vs. {[other._values[i] for i in order]}")
        return Vector.compare_vectors([self._values[i] for i in order], [other._values[i] for i in order]) > 0

    def is_dominant(self, other: 'Lexicase') -> bool:
        self.check_comparable(other)
        return all(f1 > f2 for f1, f2 in zip(self._values, other._values))
