#!/usr/bin/python3

"Tests the accuracy of our general quadratic solver."

from random import SystemRandom
from genquad import general_quadratic


def test_accuracy():
    "Generates 10,000 random quadratics and solves them."
    rng = SystemRandom()
    for index in range(10000):
        root_1 = rng.uniform(0.0, 1e6)
        root_2 = rng.uniform(0.0, 1e6)
        if root_2 < root_1:
            root_1, root_2 = root_2, root_1
        sum_term = root_1 + root_2
        prod_term = root_1 * root_2
        (sol_1, sol_2) = general_quadratic(1.0, -sum_term, prod_term)
        assert(abs(root_1 - sol_1) < .001)
        assert(abs(root_2 - sol_2) < .001)