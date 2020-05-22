# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import Callable

import holoviews as hv
import numpy as np
import plotly
from holoviews import opts

hv.extension("bokeh")

def plot_curve(
    func: Callable[[np.ndarray], np.ndarray] = lambda x: 1 + (x - 2) ** 2,
    x_min: int = 0,
    x_max: int = 5,
    renderer: hv.renderer = hv.renderer("bokeh"),
):

    xs = np.linspace(x_min, x_max, 100)
    ys = [func(x) for x in xs]

    curve = hv.Curve((xs, ys), "x", hv.Dimension("f(x)"), label="Graph of f")

    curve.opts(opts.Curve(height=600, width=900, line_width=2.50, tools=["hover"]))

    # Create plot and save it as html file. We create the plot depending on the input
    # parameter renderer either via bokeh or via plotly.
    if renderer == "bokeh":
        renderer = hv.renderer("bokeh")
        # Using renderer save
        renderer.save(curve, "bokeh")
    elif renderer == "plotly":
        renderer = hv.renderer("plotly").get_plot(curve).state
        plotly.offline.plot(renderer, filename="plotly.html")
    elif renderer == "online":
        hv.save(curve, 'browse_me.html', )


# %%
plot_curve(renderer="online")


# %%
plot_curve(renderer="bokeh")


# %%
plot_curve(renderer="plotly")

