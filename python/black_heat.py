# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:15:43 2019

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

bz1a = data_b.bp.str.contains(r'1|a').sum()
bz2a = data_b.bp.str.contains(r'2|a').sum() 
bz3a = data_b.bp.str.contains(r'3|a').sum()
bz4a = data_b.bp.str.contains(r'4|a').sum()
bz5a = data_b.bp.str.contains(r'5|a').sum()
bz6a = data_b.bp.str.contains(r'6|a').sum() 
bz7a = data_b.bp.str.contains(r'7|a').sum() 
bz8a = data_b.bp.str.contains(r'8|a').sum() 
bza = [bz1a,bz2a,bz3a,bz4a,bz5a,bz6a,bz7a,bz8a]

bz1b = data_b.bp.str.contains(r'1|b').sum() 
bz2b = data_b.bp.str.contains(r'2|b').sum()
bz3b = data_b.bp.str.contains(r'3|b').sum() 
bz4b = data_b.bp.str.contains(r'4|b').sum() 
bz5b = data_b.bp.str.contains(r'5|b').sum() 
bz6b = data_b.bp.str.contains(r'6|b').sum() 
bz7b = data_b.bp.str.contains(r'7|b').sum() 
bz8b = data_b.bp.str.contains(r'8|b').sum() 
bzb = [bz1b,bz2b,bz3b,bz4b,bz5b,bz6b,bz7b,bz8b]

bz1c = data_b.bp.str.contains(r'1|c').sum() 
bz2c = data_b.bp.str.contains(r'2|c').sum() 
bz3c = data_b.bp.str.contains(r'3|c').sum() 
bz4c = data_b.bp.str.contains(r'4|c').sum() 
bz5c = data_b.bp.str.contains(r'5|c').sum() 
bz6c = data_b.bp.str.contains(r'6|c').sum() 
bz7c = data_b.bp.str.contains(r'7|c').sum() 
bz8c = data_b.bp.str.contains(r'8|c').sum() 
bzc = [bz1c,bz2c,bz3c,bz4c,bz5c,bz6c,bz7c,bz8c]

bz1d = data_b.bp.str.contains(r'1|d').sum()
bz2d = data_b.bp.str.contains(r'2|d').sum()
bz3d = data_b.bp.str.contains(r'3|d').sum()
bz4d = data_b.bp.str.contains(r'4|d').sum() 
bz5d = data_b.bp.str.contains(r'5|d').sum()
bz6d = data_b.bp.str.contains(r'6|d').sum() 
bz7d = data_b.bp.str.contains(r'7|d').sum() 
bz8d = data_b.bp.str.contains(r'8|d').sum() 
bzd = [bz1d,bz2d,bz3d,bz4d,bz5d,bz6d,bz7d,bz8d]


bz1e = data_b.bp.str.contains(r'1|e').sum()
bz2e = data_b.bp.str.contains(r'2|e').sum()
bz3e = data_b.bp.str.contains(r'3|e').sum() 
bz4e = data_b.bp.str.contains(r'4|e').sum() 
bz5e = data_b.bp.str.contains(r'5|e').sum() 
bz6e = data_b.bp.str.contains(r'6|e').sum()
bz7e = data_b.bp.str.contains(r'7|e').sum()
bz8e = data_b.bp.str.contains(r'8|e').sum()
bze = [bz1e,bz2e,bz3e,bz4e,bz5e,bz6e,bz7e,bz8e]


bz1f = data_b.bp.str.contains(r'1|f').sum() 
bz2f = data_b.bp.str.contains(r'2|f').sum() 
bz3f = data_b.bp.str.contains(r'3|f').sum()
bz4f = data_b.bp.str.contains(r'4|f').sum() 
bz5f = data_b.bp.str.contains(r'5|f').sum()
bz6f = data_b.bp.str.contains(r'6|f').sum() 
bz7f = data_b.bp.str.contains(r'7|f').sum() 
bz8f = data_b.bp.str.contains(r'8|f').sum() 
bzf = [bz1f,bz2f,bz3f,bz4f,bz5f,bz6f,bz7f,bz8f]


bz1g = data_b.bp.str.contains(r'1|g').sum() 
bz2g = data_b.bp.str.contains(r'2|g').sum() 
bz3g = data_b.bp.str.contains(r'3|g').sum() 
bz4g = data_b.bp.str.contains(r'4|g').sum() 
bz5g = data_b.bp.str.contains(r'5|g').sum() 
bz6g = data_b.bp.str.contains(r'6|g').sum() 
bz7g = data_b.bp.str.contains(r'7|g').sum() 
bz8g = data_b.bp.str.contains(r'8|g').sum() 
bzg = [bz1g,bz2g,bz3g,bz4g,bz5g,bz6g,bz7g,bz8g]


bz1h = data_b.bp.str.contains(r'1|h').sum() 
bz2h = data_b.bp.str.contains(r'2|h').sum() 
bz3h = data_b.bp.str.contains(r'3|h').sum() 
bz4h = data_b.bp.str.contains(r'4|h').sum() 
bz5h = data_b.bp.str.contains(r'5|h').sum()
bz6h = data_b.bp.str.contains(r'6|h').sum() 
bz7h = data_b.bp.str.contains(r'7|h').sum() 
bz8h = data_b.bp.str.contains(r'8|h').sum() 
bzh = [bz1h,bz2h,bz3h,bz4h,bz5h,bz6h,bz7h,bz8h]


fig = go.Figure(data=go.Heatmap(z=[bza,bzb,bzc,bzd,bze,bzf,bzg,bzh],x=letters, y=numbers))

fig.update_layout(title="Use of Board: Player with Black Pieces")

of.plot(fig, filename="/var/www/Chess/databasesProject/bmov.html", auto_open=False)
# of.plot(fig, filename = "/usr/share/databases/abrockway/wmov.html", auto_open=False)

fig.show()