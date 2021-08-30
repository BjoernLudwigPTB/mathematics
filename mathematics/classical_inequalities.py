from typing import Callable, Union

import numpy as np
from scipy import stats

__all__ = ["check_jensen_inequality"]


def check_jensen_inequality(
    rand_var: Union[stats.rv_continuous, stats.rv_discrete],
    phi: Callable[[np.float], np.float],
) -> bool:
    r"""Check if Jensen's inequality holds for the given function phi

    Jensen's inequality states: Let :math:`(\Omega, \mathcal A, P)` be a probability
    space, :math:`X` an integrable real-valued random variable and :math:`\varphi` a
    convex function, then

    :math:`\varphi( \mathbb E [X]) \leq \mathbb E [\varphi(X)]`.

    Parameters
    ----------
    rand_var : Union[stats.rv_continuous, stats.rv_discrete]
        the random variable under test
    phi : Callable[[np.float], np.float]the function under test

    Returns
    -------
    True, if Jensen's inequality holds for the given function and random variable
    """
    return np.less_equal(
        phi(rand_var.expect()), rand_var.expect(func=phi)
    ) or np.allclose(phi(rand_var.expect()), rand_var.expect(func=phi), rtol=9e-15)
