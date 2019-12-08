import psycopg2
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as of
conn = psycopg2.connect("dbname=chess19 user=tmaranzatto")
cur = conn.cursor()
#json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
dataq = 'select victory_status, black_rating, white_rating from rawdata;'

cur.execute(dataq)
data = cur.fetchall()

#Convert data to numpy array
newdata = np.array(data)

diff = []
for list in newdata:
#    print(list[2], list[1])
    difference =int(list[2]) - int(list[1])
    x = abs(difference)
    diff.append(x)

status = []
for list in newdata:
    x = list[0]
    status.append(x)

test1 = pd.DataFrame(diff)
test2 = pd.DataFrame(status)

df = pd.concat([test1.reset_index(drop=True),test2], axis=1)
df.columns = ['difference', 'status']

#make bins for difference
df['diff_bins'] = pd.cut(x=df['difference'], bins=[0,401,802,1204,1605])

#df.groupby(['status'])

fig = go.Figure(data=go.Heatmap(z=[df.groupby(['status'])], x=df['status'], y=df['diff_bins']))
fig.update_layout(xaxis_title= "Victory Status", yaxis_title= "Difference in rating between players")

#fig.write_image("/var/www/Chess/databasesProject/chess/static/heat.png")
of.plot(fig, filename = "/var/www/Chess/databasesProject/chess/templates/heat.html", auto_open=False)
