from typing import Callable, Union

import numpy as np
from scipy import stats

__all__ = ["jensen_inequality"]


def jensen_inequality(
    rand_var: Union[stats.rv_continuous, stats.rv_discrete],
    phi: Callable[[np.float], np.float],
) -> bool:
    """Check if Jensen's inequality holds for the given function phi

    Jensen's inequality states: Let :math:`(\Omega, \mathcal A, P)` be a probability
    space, :math:`X` an integrable real-valued random variable and :math:`\varphi` a
    convex function, then

    :math:`\varphi( \mathbb E [X]) \leq \mathbb E [\varphi(X)]`.

    Parameters
    ----------

        rand_var :
            the random variable under test
        phi : the function under test

    Returns
    -------
    :return: if Jensen's inequality holds for the given function and random variable
    """
    return np.less_equal(
        phi(rand_var.expect()), rand_var.expect(func=phi)
    ) or np.allclose(phi(rand_var.expect()), rand_var.expect(func=phi), rtol=9e-15)
