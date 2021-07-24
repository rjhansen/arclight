#!/usr/bin/python3

"Computes the general quadratic equation in a relatively sane way."

from math import sqrt


class NotQuadratic(Exception):
    "Thrown when general_quadratic is given a non-quadratic equation."

class ImaginaryResult(Exception):
    "Thrown if imaginary solutions would be returned."

def general_quadratic(a: float, b: float, c: float) -> (float, float):
    "Computes the general quadratic equation."

    if not (isinstance(a, (int, float)) and
        isinstance(b, (int, float)) and
        isinstance(c, (int, float))):
        raise ValueError("passed non-floats")

    a = float(a)
    b = float(b)
    c = float(c)

    if abs(a) < 0.001:
        raise NotQuadratic()
    
    try:
        if (4 * a * c) > (b**2):
            raise ImaginaryResult()
        discriminant = sqrt(b**2 - (4 * a * c))
        numerator_1 = (-1 * b) - discriminant
        numerator_2 = (-1 * b) + discriminant
        denominator = 2 * a
        return (numerator_1 / denominator, numerator_2 / denominator)
    
    except OverflowError:
        raise ValueError("numeric crash")
