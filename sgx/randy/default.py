# -*- coding: utf-8 -*-
# ______________   ______   __
# |____/|____|| \  ||   \\_/
# |R  \_|A   ||N \_||D__/ |Y
#
#    @..@    古池や
#   (----)    蛙飛び込む
#  ( >__< )    水の音
#
# ( ! ) 2021 Giovanni Squillero. CC0 Public Domain.
# Project page: https://github.com/squillero/randy

__all__ = ['boolean', 'choice', 'random', 'sigma_choice', 'sigma_random', 'randint', 'shuffle']

import logging
from .core import Randy

try:
    # Ok, I may admit it's a little bit paranoid...
    __the_ram
    assert False, f"Panik: Randy the Ram has already be initialized: {__the_ram!r}"
except NameError:
    __the_ram = Randy('None')   # 'None' is like None, but w/o warning
    logging.debug(f"Initialized Randy the Ram: {__the_ram!r}")


def boolean(*args, **kwargs):
    """Call boolean with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.boolean(*args, **kwargs)


def random(*args, **kwargs):
    """Call random with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.random(*args, **kwargs)


def sigma_random(*args, **kwargs):
    """Call sigma_random with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.sigma_random(*args, **kwargs)


def choice(*args, **kwargs):
    """Call choice with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.choice(*args, **kwargs)


def sigma_choice(*args, **kwargs):
    """Call sigma_choice with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.sigma_choice(*args, **kwargs)


def randint(*args, **kwargs):
    """Call randint with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.randint(*args, **kwargs)


def shuffle(*args, **kwargs):
    """Call shuffle with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.shuffle(*args, **kwargs)


def shuffled(*args, **kwargs):
    """Call shuffled with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.shuffled(*args, **kwargs)
