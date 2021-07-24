#!/usr/bin/env python3

import pytest

from genquad import general_quadratic, NotQuadratic

def test_not_quadratic():
    with pytest.raises(NotQuadratic):
        # x = 0 is not a quadratic equation.
        general_quadratic(0.0, 1.0, 0.0)
