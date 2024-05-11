'''Zadatak 1.8. Preko ovog linka https://www.kaggle.com/shivamb/netflix-shows preuzeti bazu netflix_titles.csv.
Uz pomoć biblioteke pandas ispisati broj redova I kolona, zameniti vrednosti Nan kolona sa Unknown I izdvojiti kolone title
 I type za koje type ima vrednost Movie.'''


#import modula
import pandas as pd

#uploudovanje baze netflix_titles u Jupiter Notebook
#index_col=0 znaci da po difoltu prva kolona bude indeks
titles = pd.read_csv('netflix_titles.csv', index_col=0)

#dobijamo broj redova i kolona u vidu n-torke
titles.shape

#zamena nepoznatih vrednosti sa Unknown, ako je inplace True izvrsice se trajna promena
titles.fillna(value='Unknown', inplace=True) 

#izdvajaju se filmovi koji u koloni type imaju vrednost Movie
titles=titles[(titles['type']=='Movie')]

#izdvaja se tabela koja sadrzi samo ove dve kolone
df = titles[['title','type']]

#ispis tabele
df
