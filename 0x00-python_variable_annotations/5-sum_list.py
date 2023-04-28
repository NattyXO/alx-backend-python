#!/usr/bin/env python3
""" Takes list input of floats, returns sum """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums list of floats """
    total: float = 0
    for x in input_list:
        total += x
    return total
