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

# Copyright 2021 Giovanni Squillero
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random


def test_consistency():
    randy._random.seed(42)
    r0 = list()
    r1 = list()
    for _ in range(100):
        r0.append(randy.random())
        r1.append(random.random())
    assert r1 == r1

    randy._random.seed(42)
    r2 = [randy.random() for _ in range(100)]
    assert r0 == r2

    randy._random.seed(42)
    state = randy._random.getstate()
    r3 = [randy.random() for _ in range(100)]
    assert state != randy._random.getstate()
    randy._random.seed(42)
    assert state == randy._random.getstate()
    state_std = random.getstate()
    random.shuffle(r1)
    assert state_std != random.getstate()
    assert state == randy._random.getstate()
    r4 = [randy.random() for _ in range(100)]
    assert r3 == r4


def test_choice():
    for _ in range(1000):
        assert randy.choice([0, 1, 2, 3, 4], weights=[1, 0, 0, 0, 0]) == 0
        assert randy.choice([0, 1, 2, 3, 4], weights=[0, .25, .25, .25, .25]) != 0


def test_shuffled():
    assert list(range(1000)) == sorted(randy.shuffled(list(range(1000))))
