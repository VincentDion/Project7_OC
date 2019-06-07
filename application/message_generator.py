# -*- coding: Utf-8 -*

from random import randint


def random_msgs(msgs_array):
    """Function to find a random item on an array"""
    index = randint(1, len(msgs_array))
    return msgs_array[index - 1]
