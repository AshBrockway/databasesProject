# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:27:31 2019

@author: ashle_000
"""

import plotly.graph_objects as go
import psycopg2 as psy
import pandas as pd
import plotly.express as plt
import plotly.offline as of
import numpy as np
from plotly.subplots import make_subplots
from plotly.graph_objs import *
import chart_studio.plotly as py


conn = psy.connect("dbname=chess19 user=abrockway")

cur = conn.cursor()

query_id = "select id from moves_info;" 
cur.execute(query_id)
ids = cur.fetchall()

query_moves = "select moves from moves_info;" 
cur.execute(query_moves)
moves = cur.fetchall()

count_moves = "select count(id) from moves_info group by id;"
cur.execute(count_moves)
counts = cur.fetchall() 


temp = "create temp table turns as (select turns from game_info);" 
cur.execute(temp)

query_turns = "select turns from turns;"
cur.execute(query_turns)
turns = cur.fetchall()

query_distinct_moves = "select distinct moves from moves_info;" 
cur.execute(query_distinct_moves)
distinct_moves =  cur.fetchall() 

# conn.close()
# secur.close() 




# plotting 
x = np.array(ids)
y = np.array(moves)

data = np.column_stack([x,y])
df = pd.DataFrame(data=data, columns=['id','move'])
'''
cols = ['ind', 'id', 'move']
df.columns(['id', 'move'])
'''
dicti = {k: g["move"].tolist() for k,g in df.groupby("id")}

# df.groupby('id').apply(copyStuff) 

white_move = []
black_move = []
count_list = []
pastval = 0


for key in dicti.keys():
    n = len(dicti[key])
    liz = list(dicti[key])
    count = 0
    for i in range(n):
        count = count + 1
        if count%2==0:
            white_move.append(liz[i-1])
        else:
            black_move.append(liz[i-1])
        count_list.append(count)
    

liw = []
lib = []
cou = []

for i in white_move:
    liw.append(i)

for j in black_move:
    lib.append(j)

for c in count_list:
    cou.append(c)

white_move = np.array(liw)
black_move = np.array(lib)
counts = np.array(cou)

# data = np.column_stack([white_move, black_move])    

data_w = pd.DataFrame(data=white_move, columns=['wp'])    
data_b = pd.DataFrame(data=black_move, columns=['bp'])

letters = ['a','b','c','d','e','f','g','h']
numbers = ['1','2','3','4','5','6','7','8']

z1a = data_w.wp.str.contains(r'1|a').sum() 
z2a = data_w.wp.str.contains(r'2|a').sum() 
z3a = data_w.wp.str.contains(r'3|a').sum() 
z4a = data_w.wp.str.contains(r'4|a').sum() 
z5a = data_w.wp.str.contains(r'5|a').sum() 
z6a = data_w.wp.str.contains(r'6|a').sum() 
z7a = data_w.wp.str.contains(r'7|a').sum() 
z8a = data_w.wp.str.contains(r'8|a').sum() 
za = [z1a,z2a,z3a,z4a,z5a,z6a,z7a,z8a]

z1b = data_w.wp.str.contains(r'1|b').sum() 
z2b = data_w.wp.str.contains(r'2|b').sum() 
z3b = data_w.wp.str.contains(r'3|b').sum() 
z4b = data_w.wp.str.contains(r'4|b').sum() 
z5b = data_w.wp.str.contains(r'5|b').sum() 
z6b = data_w.wp.str.contains(r'6|b').sum() 
z7b = data_w.wp.str.contains(r'7|b').sum() 
z8b = data_w.wp.str.contains(r'8|b').sum() 
zb = [z1b,z2b,z3b,z4b,z5b,z6b,z7b,z8b]

z1c = data_w.wp.str.contains(r'1|c').sum() 
z2c = data_w.wp.str.contains(r'2|c').sum()
z3c = data_w.wp.str.contains(r'3|c').sum() 
z4c = data_w.wp.str.contains(r'4|c').sum() 
z5c = data_w.wp.str.contains(r'5|c').sum() 
z6c = data_w.wp.str.contains(r'6|c').sum() 
z7c = data_w.wp.str.contains(r'7|c').sum() 
z8c = data_w.wp.str.contains(r'8|c').sum() 
zc = [z1c,z2c,z3c,z4c,z5c,z6c,z7c,z8c]

z1d = data_w.wp.str.contains(r'1|d').sum()
z2d = data_w.wp.str.contains(r'2|d').sum()
z3d = data_w.wp.str.contains(r'3|d').sum()
z4d = data_w.wp.str.contains(r'4|d').sum() 
z5d = data_w.wp.str.contains(r'5|d').sum()
z6d = data_w.wp.str.contains(r'6|d').sum() 
z7d = data_w.wp.str.contains(r'7|d').sum()
z8d = data_w.wp.str.contains(r'8|d').sum()
zd = [z1d,z2d,z3d,z4d,z5d,z6d,z7d,z8d]

z1e = data_w.wp.str.contains(r'1|e').sum() 
z2e = data_w.wp.str.contains(r'2|e').sum() 
z3e = data_w.wp.str.contains(r'3|e').sum() 
z4e = data_w.wp.str.contains(r'4|e').sum() 
z5e = data_w.wp.str.contains(r'5|e').sum() 
z6e = data_w.wp.str.contains(r'6|e').sum() 
z7e = data_w.wp.str.contains(r'7|e').sum() 
z8e = data_w.wp.str.contains(r'8|e').sum()
ze = [z1e,z2e,z3e,z4e,z5e,z6e,z7e,z8e]

z1f = data_w.wp.str.contains(r'1|f').sum() 
z2f = data_w.wp.str.contains(r'2|f').sum() 
z3f = data_w.wp.str.contains(r'3|f').sum()
z4f = data_w.wp.str.contains(r'4|f').sum() 
z5f = data_w.wp.str.contains(r'5|f').sum() 
z6f = data_w.wp.str.contains(r'6|f').sum() 
z7f = data_w.wp.str.contains(r'7|f').sum() 
z8f = data_w.wp.str.contains(r'8|f').sum()
zf = [z1f,z2f,z3f,z4f,z5f,z6f,z7f,z8f]

z1g = data_w.wp.str.contains(r'1|g').sum() 
z2g = data_w.wp.str.contains(r'2|g').sum()
z3g = data_w.wp.str.contains(r'3|g').sum() 
z4g = data_w.wp.str.contains(r'4|g').sum() 
z5g = data_w.wp.str.contains(r'5|g').sum() 
z6g = data_w.wp.str.contains(r'6|g').sum() 
z7g = data_w.wp.str.contains(r'7|g').sum()
z8g = data_w.wp.str.contains(r'8|g').sum()
zg = [z1g,z2g,z3g,z4g,z5g,z6g,z7g,z8g]


z1h = data_w.wp.str.contains(r'1|h').sum() 
z2h = data_w.wp.str.contains(r'2|h').sum()
z3h = data_w.wp.str.contains(r'3|h').sum()
z4h = data_w.wp.str.contains(r'4|h').sum() 
z5h = data_w.wp.str.contains(r'5|h').sum()
z6h = data_w.wp.str.contains(r'6|h').sum()
z7h = data_w.wp.str.contains(r'7|h').sum() 
z8h = data_w.wp.str.contains(r'8|h').sum() 
zh = [z1h,z2h,z3h,z4h,z5h,z6h,z7h,z8h]

fig = go.Figure(data=go.Heatmap(z=[za,zb,zc,zd,ze,zf,zg,zh],x=letters, y=numbers))

fig.update_layout(title="Use of Board: Player with White Pieces")

of.plot(fig, filename="/var/www/Chess/databasesProject/wmov.html", auto_open=False)

# of.plot(fig, filename = "/usr/share/databases/abrockway/wmov.html", auto_open=False)
fig.show()