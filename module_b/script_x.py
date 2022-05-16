from module_a.script_y import double
from module_a.script_z import halve


def weird_function(x: int | float, y: int | float) -> int | float:
    result = double(x) + halve(y)
    return result
