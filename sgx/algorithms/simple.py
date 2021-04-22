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

__all__ = ['sg']

from typing import Optional, Callable, Union
try:
    from tqdm import tqdm
except:
    tqdm = None
try:
    # could fail with -O...
    from tqdm.notebook import tqdm as tqdm_notebook
except:
    tqdm_notebook = tqdm

from ..utils import logging, jupyter_support
from ..archive import Archive
from .. import species as species_

TQDM_DEFAULT_OPTIONS = {
    'bar_format': '{n:,} generations in {elapsed} (speed: {rate_fmt})',
    'unit': 'gen',
    'unit_scale': True,
    'leave': False,
    'dynamic_ncols': True
}


def sg(species: species_.Species,
       max_generation: Optional[int] = None,
       progress_bar: Optional[Union[str, bool]] = True):
    """A vanilla optimizer

    The algorithm is described in the paper *A new evolutionary algorithm inspired by the selfish gene theory*
    (DOI: 10.1109/ICEC.1998.700092)
    """

    tqdm_options = TQDM_DEFAULT_OPTIONS
    num_generation = 0
    archive = Archive()

    # inject stopping conditions (raw)
    stopping_conditions = list()

    if max_generation:
        stopping_conditions.append(lambda: num_generation >= max_generation)  # closure!
        tqdm_options['bar_format'] = '{percentage:.0f}%|{bar}|{remaining} ({rate_fmt})'

    if species.fitness_function.best_fitness:
        stopping_conditions.append(
            lambda: archive and next(iter(archive)).fitness >= species.fitness_function.best_fitness)

    if tqdm is None or not progress_bar:
        bar = None
    elif progress_bar == 'tqdm' or (progress_bar is True and not jupyter_support.is_notebook()):
        bar = tqdm(total=max_generation, **tqdm_options)
    elif progress_bar == 'notebooks' or (progress_bar is True and jupyter_support.is_notebook()):
        bar = tqdm_notebook(total=max_generation, **tqdm_options)
    else:
        assert False, "D'ho!?"

    while all(not f() for f in stopping_conditions):
        if bar is not None:
            bar.update(1)
        num_generation += 1

        i1 = species.sample()
        i2 = species.sample()
        f1 = species.evaluate(i1)
        f2 = species.evaluate(i2)

        if f1 > f2:
            species.update(winner=i1, loser=i2)
        elif f2 > f1:
            species.update(winner=i2, loser=i1)

        archive_changed = archive.add_generation([[i1, f1], [i2, f2]])
        if archive_changed:
            logging.debug(f"** ARCHIVE AT GENERATION {num_generation} -- SIZE: {len(archive):,}")
            for ae in archive:
                logging.debug(f"-] {species.genome.format_genotype(ae.genotype)}:{ae.fitness}")

    if bar is not None:
        bar.close()
    return archive
