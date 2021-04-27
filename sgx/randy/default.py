# -*- coding: utf-8 -*-
# ______________   ______   __
# |____/|____|| \  ||   \\_/
# |R  \_|A   ||N \_||D__/ |Y
#
#    @..@    古池や
#   (----)    蛙飛び込む
#  ( >__< )    水の音
#
# ( ! ) 2021 Giovanni Squillero. Public Domain.
# Project page: https://github.com/squillero/randy

__all__ = [
    'boolean', 'choice', 'randint', 'random', 'shuffle', 'shuffled', 'sigma_choice', 'sigma_random', 'weighted_choice'
]

import logging
from typing import Optional, Any
import numpy as np

from .core import Randy

try:
    # Ok, I may admit it's a little bit paranoid...
    _default_generator
    assert False, f"Panic: The default random generator has already be initialized: {_default_generator!r}"
except NameError:
    _default_generator = Randy(None, croak=False)  # None, but w/o warning
    logging.debug(f"Initialized Randy: {_default_generator!r}")


def seed(new_seed: Optional[Any] = None) -> None:
    global _default_generator
    _default_generator = np.random.default_rng(new_seed)


def boolean(*args, **kwargs):
    """Call boolean with the default random generator."""
    return _default_generator.boolean(*args, **kwargs)


def random(*args, **kwargs):
    """Call random with the default random generator."""
    return _default_generator.random(*args, **kwargs)


def sigma_random(*args, **kwargs):
    """Call sigma_random with the default random generator."""
    return _default_generator.sigma_random(*args, **kwargs)


def weighted_choice(*args, **kwargs):
    """Call weighted_choice with the default random generator."""
    return _default_generator.weighted_choice(*args, **kwargs)


def sigma_choice(*args, **kwargs):
    """Call sigma_choice with the default random generator."""
    return _default_generator.sigma_choice(*args, **kwargs)


def choice(*args, **kwargs):
    """Call choice with the default random generator."""
    return _default_generator.choice(*args, **kwargs)


def randint(*args, **kwargs):
    """Call randint with the default random generator."""
    return _default_generator.randint(*args, **kwargs)


def shuffle(*args, **kwargs):
    """Call shuffle with the default random generator."""
    return _default_generator.shuffle(*args, **kwargs)


def shuffled(*args, **kwargs):
    """Call shuffled with the default random generator."""
    return _default_generator.shuffled(*args, **kwargs)
