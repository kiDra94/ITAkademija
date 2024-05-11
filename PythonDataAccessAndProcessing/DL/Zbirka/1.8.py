'''Zadatak 1.8. Preko ovog linka https://www.kaggle.com/shivamb/netflix-shows preuzeti bazu netflix_titles.csv.
Uz pomoć biblioteke pandas ispisati broj redova I kolona, zameniti vrednosti Nan kolona sa Unknown I izdvojiti kolone title
 I type za koje type ima vrednost Movie.'''


import pandas as pd

titles = pd.read_csv('netflix_titles.csv', index_col=0)
titles.shape
titles.fillna(value='Unknown', inplace=True) 
titles=titles[(titles['type']=='Movie')]
df = titles[['title','type']]
df
