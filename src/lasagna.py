"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function


def bake_time_remaining(time):
    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(layer):
    return layer * PREPARATION_TIME

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here


# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(layer, time):
    total = preparation_time_in_minutes(layer)+time
    return total
