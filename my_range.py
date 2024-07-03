"""
Instructions
Define and test a function `myRange` in the file named testmyrange.py.
This function should behave like Python’s standard `range` function, 
with the required and optional arguments, but it should return a `list`. 
Do not use the `range` function in your implementation! 
(Hints: Study Python’s help on `range` to determine the names, positions, 
and what to do with your function’s parameters (See item 2 below). 
Use a default value of `None` for the two optional parameters. 
If these parameters both equal `None`, then the function has been called 
with just the stop value. If just the third parameter equals `None`, then 
the function has been called with a start value as well. Thus, the first 
part of the function’s code establishes what the values of the parameters 
are or should be. The rest of the code uses those values to build a list by 
counting up or down.)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 3, 5, 7, 9]
"""

class MyRangeError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        if errors:
            print(errors)


def my_range(stop: int, start: int=None, step: int=1) -> list:
    num_list: list = []
    # if statements on the start parameter
    # if statements on the step parameter
    # fill num_list with the numbers within the range given
    return num_list