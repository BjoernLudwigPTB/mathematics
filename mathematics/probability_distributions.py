# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import Optional

import holoviews as hv
import numpy as np
from scipy import stats


def visualize_dist_by_samples(
    size: Optional[int] = 1000,
    dist: Optional[stats.rv_continuous] = stats.norm(),
    upper_bound: Optional[float] = np.inf,
    lower_bound: Optional[float] = -np.inf,
    bins: Optional[int] = None,
):
    """Draw the histogram for a number of samples from the given distribution

    Visualize a probability distribution by drawing random samples and creating the
    histogram from these samples. It is guaranteed that the specified amount of
    samples fall between the specified bounds.

    Parameters
    ----------

        size : int, optional
            number of samples to draw from the distribution, defaults to 1000
        dist : stats.rv_continuous, optional
            distribution to draw from, defaults to standard normal distribution
        lower_bound : float, optional
            the lower bound to truncate the underlying distribution at
        upper_bound : float, optional
            the upper bound to truncate the underlying distribution at
        bins : int, optional
            number of bins for the histogram which should be around one percent
            of the number of samples, which is the default

    Returns
    -------

        hist : hv.Histogram
            the holoviews histogram of the samples
    """
    # We create a histogram based on Bokeh, but could exchange that simply by
    # "matplotlib".
    hv.extension("bokeh")

    if bins is None:
        bins = int(size / 100)

    # Draw the first set of samples.
    realizations = dist.rvs(size=size)
    # Now as long as there are samples outside the desired range, redraw and fill up
    # the sample size with valid samples.
    while np.count_nonzero(
        mask := (realizations < lower_bound) | (realizations > upper_bound)
    ):
        realizations[mask] = dist.rvs(size=np.count_nonzero(mask))

    # Produce the input format for the holoview histogram using the according numpy
    # routine.
    return hv.Histogram(np.histogram(realizations, bins))
