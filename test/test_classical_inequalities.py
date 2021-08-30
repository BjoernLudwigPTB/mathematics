import numpy as np
from hypothesis import given, strategies as st
from hypothesis.strategies import composite
from hypothesis.extra import numpy as hnp
from numpy.testing import raises
from pytest import fixture
from scipy import stats

from mathematics.classical_inequalities import check_jensen_inequality



@composite
def convex_function(draw):
    """Affine and thus convex one dimensional function"""
    strategy = draw(
        st.one_of(st.floats(allow_nan=False, allow_infinity=False)),
        hnp.arrays(np.float64, shape=hnp.array_shapes(min_side=1, max_side=2)),
    )
    a = strategy
    b = strategy

    return lambda x: a * x + b


@composite
def not_convex_function(draw):
    """Function which is not convex"""
    return lambda x: -(x ** 2)


@given(convex_function())
def test_minimal_call_jensen_inequality(phi):
    assert check_jensen_inequality(stats.uniform, phi)

@given(not_convex_function())
def test_minimal_call_jensen_inequality_fails(phi):
    print("Hello World!")
    assert not check_jensen_inequality(stats.uniform, phi)
    
