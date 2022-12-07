#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
