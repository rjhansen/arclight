#!/usr/bin/env python3

"Ensures we don't return imaginary results."

import pytest
from genquad import general_quadratic, ImaginaryResult


def test_not_real():
    with pytest.raises(ImaginaryResult):
        # x**2 + 1 = 0 is not a real quadratic equation.
        general_quadratic(1.0, 0.0, 1.0)
