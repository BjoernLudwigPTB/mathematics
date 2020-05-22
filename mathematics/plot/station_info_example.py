# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# %load  station_info_example.py
import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts

hv.extension("plotly")

station_info = pd.read_csv('../holoviews-examples/assets/station_info.csv')
station_info.head()


# %%
scatter = hv.Scatter(station_info, 'services', 'ridership')
scatter


# %%
layout = scatter + hv.Histogram(np.histogram(station_info['opened'], bins=24), kdims=['opened'])
layout


# %%
taxi_dropoffs = {hour:arr for hour, arr in np.load('../holoviews-examples/assets/hourly_taxi_data.npz').items()}
print('Hours: {hours}'.format(hours=', '.join(taxi_dropoffs.keys())))
print('Taxi data contains {num} arrays (one per hour).\nDescription of the first array:\n'.format(num=len(taxi_dropoffs)))
np.info(taxi_dropoffs['0'])


# %%
bounds = (-74.05, 40.70, -73.90, 40.80)
image = hv.Image(taxi_dropoffs['0'], ['lon','lat'], bounds=bounds)
image


# %%
points = hv.Points(station_info, ['lon','lat'])
image + image * points


# %%


