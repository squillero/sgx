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

"""The eXtended Selfish Gene algorithm (SGX):
A population-less EA loosely inspired by a cool interpretation of the Darwinian theory.
See: https://github.com/squillero/sgx

Copyright © 2021 Giovanni Squillero. Licensed under the EUPL 1.2.
"""

__name__ = "sgx"
__version__ = "0.2.dev5"
__author__ = "Giovanni Squillero"
__copyright__ = "Copyright (c) 2021 Giovanni Squillero. Licensed under the EUPL 1.2."

import sys
import warnings

from .utils import logging
from . import allele
from . import fitness
from . import algorithms
from . import t

from .species import Species

sys.stderr.flush()
sys.stdout.flush()

if sys.flags.optimize == 0:
    warnings.warn("All debug checks are active, performances are significantly impaired.", RuntimeWarning, stacklevel=2)

if sys.version_info < (3,):
    sys.exit(
        f"{__name__} v{__version__} is not compatible with Python {sys.version_info.major}.{sys.version_info.minor}")

if sys.version_info < (3, 6):
    warnings.warn(
        f"Python version 3.6 or later is required " +
        "({__name__} v{__version__} has not been tested with Python {sys.version_info.major}.{sys.version_info.minor})",
        Warning,
        stacklevel=2)

sys.stderr.flush()
sys.stdout.flush()
