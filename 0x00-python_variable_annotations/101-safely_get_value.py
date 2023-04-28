#!/usr/bin/env python3
""" Annotates function params and return values """

from typing import Dict, TypeVar, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Dict[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """ Duck-typing """
    if key in dct:
        return dct[key]
    else:
        return default
