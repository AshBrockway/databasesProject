#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:34:59 2019

@author: oliviaroberts
"""

import pandas as pd
import plotly.express as px

data = pd.read_csv("times_graph.csv")
data = data.drop(['Unnamed: 0', 'X', 'index'], axis = 1)
data.columns = ['rated', 'opening_play', 'increment_code', 'variable','rating', 'rating_grouping']

fig = px.violin(data, y= "opening_play", x = "rating_grouping", color = "increment_code", facet_col = "rated", box = True, points = "all", hover_data=["opening_play", "increment_code", "rating"])
fig.update_layout(title="Effect of Rating on Opening Play", xaxis_title="Rating", yaxis_title="Opening Play")
fig['layout']['xaxis2']['title']['text']= 'Rating'
fig.show()
