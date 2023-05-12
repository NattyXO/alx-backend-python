#!/usr/bin/env python3
""" Takes list input of floats and ints, returns sum """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums list, returns float """
    total: float = 0
    for x in mxd_lst:
        total += x
    return total
