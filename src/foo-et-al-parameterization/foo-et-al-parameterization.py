# Author: Aidan Goldstein

import math


def sphere_volume(radius):
    """ sphere_volume takes a given numerical value radius as a parameter of a sphere
    and returnsback the total volume of the sphere. """

    volume = 4.0 / 3.0 * math.pi * (radius ** 3)
    return volume

