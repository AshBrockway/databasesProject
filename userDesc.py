#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:48:03 2019

@author: oliviaroberts
"""

import psycopg2
conn = psycopg2.connect("dbname = chess19 user = oroberts")
cur = conn.cursor()
cur.execute("select r.opening_name, g.winner from game_info g, rawdata r where g.id = r.id;")
table = cur.fetchall()

def userDesc():
    description = input("Choose your opening move here: ")
    count = 0
    for i in range(len(table)):
        if table[i][0] == description and table[i][1] == "white":
            count = count + 1
    white_wins = count
    
    count1 = 0
    for j in range(len(table)):
        if table[j][0] == description:
            count1 = count1 + 1
    len_open_move = count1
    
    return(white_wins, len_open_move)
            
            
            
        
    
    
    
