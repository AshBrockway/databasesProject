import plotly.express as px
import psycopg2
import numpy as np
conn = psycopg2.connect("dbname=chess19 user=tmaranzatto")
cur = conn.cursor()
ratingsq = "select black_rating,white_rating from black_players b join white_players w on b.id = w.id;"
cur.execute(ratingsq)
ratingsd = cur.fetchall()
ratingsd = np.array(ratingsd)
black_rating = []
white_rating = []
for pair in ratingsd:
    black_rating.append(pair[0])
    white_rating.append(pair[1])
black_rating = np.array(black_rating)
white_rating = np.array(white_rating)
deltaratings = abs(black_rating - white_rating)
movesq = "select turns from game_info;"
cur.execute(movesq)
movesd = cur.fetchall()
movesd = np.array(movesd)
fig = px.scatter(x=deltaratings, y=movesd)
fig.write_image("/var/www/Chess/databasesProject/chess/static/fig.png")
#fig.show()
