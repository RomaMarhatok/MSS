from typing import Callable


class Mapper:
    def mapping(self, function_map: dict[tuple, Callable], kwargs):
        keys = tuple(kwargs.keys())
        values = tuple(kwargs.values())
        return function_map.get(keys, None)(*values)
