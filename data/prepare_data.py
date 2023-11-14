#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:27:37 2023

@author: doan
"""

import pandas as pd
import xarray as xr
ds = xr.open_dataset('input_data/AM_t_1950_y.nc')
df = pd.DataFrame(ds.idata.values, columns=ds.year.values, index=ds.sts.values)
df.to_csv('warming_70years_japan.csv')
da = pd.read_csv('../download_JMA_AMeDAS_data/Amedas_list.csv', index_col=1)

x = da.loc[ds.sts.values]
y = x[ [ 'station_name', 'station_name_kana', 'fuken_id',  'latitude', 'longitude', 'height','station_name_roman'] ]
y.to_csv('AMeDAS_stations.csv')


