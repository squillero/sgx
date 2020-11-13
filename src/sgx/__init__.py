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

"""The Extended Selfish Gene optimization library (SGX)

A quick 'n dirty versatile population-less evolutionary optimizer loosely
inspired by a cool interpretation of the Darwinian theory.

Copyright © 2019 Giovanni Squillero and Alberto Tonda
The SGX is licensed under the Apache License, Version 2.0.
For more information see <https://github.com/squillero/sgx>
"""

import sys
import warnings

from .utils import logging
from . import allele
from . import fitness
from .population import Population

if sys.flags.optimize == 0:
    warnings.warn("Debug checks are active, performances are SIGNIFICANTLY impaired.", RuntimeWarning, stacklevel=2)

if sys.version_info < (3,):
    warnings.warn("The code is probably not compatible with Python v2", Warning, stacklevel=2)
elif sys.version_info < (3, 7):
    warnings.warn("The code has only been tested with Python v3.7+", Warning, stacklevel=2)

sys.stderr.flush()
sys.stdout.flush()
