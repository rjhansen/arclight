#!/usr/bin/env python3

"Ensures we throw an exception if called with invalid parameters."

import pytest
from genquad import general_quadratic


def test_not_floats():
    with pytest.raises(ValueError):
        general_quadratic("these are", "bad", "parameters")
