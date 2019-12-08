#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:52:45 2019

@author: oliviaroberts
"""
import pandas as pd
import plotly.express as px
import plotly.offline as of
data = pd.read_csv("moves_graph.csv")
data = data.drop(['Unnamed: 0'], axis = 1)
data.columns = ['increment_codes', 'turns', 'count', 'turns_range']
data = data.sort_values(by='increment_codes', ascending=False)

fig = px.histogram(data, x="turns", color="increment_codes", marginal="box", hover_data=data.columns)
fig.update_layout(title="Effect of Time Controls on Number of Turns in a Game", xaxis_title="Number of Turns", yaxis_title="Frequency")
#fig.show()
of.plot(fig, filename='/var/www/Chess/databasesProject/chess/templates/movevtime.html', auto_open=False)




