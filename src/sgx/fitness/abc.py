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

from typing import Any
from abc import ABC, abstractmethod
from ..utils import logging


class Fitness(ABC):

    @abstractmethod
    def __gt__(self, other: 'Fitness') -> bool:
        pass

    def __ne__(self, other: 'Fitness') -> bool:
        return not self == other

    def __ge__(self, other: 'Fitness') -> bool:
        return self > other or self == other

    def __lt__(self, other: 'Fitness') -> bool:
        return not (self > other or self == other)

    def __le__(self, other: 'Fitness') -> bool:
        return not self > other

    # @abstractmethod
    # def _is_dominated(self, other: Type['Fitness']) -> bool:
    #    pass
