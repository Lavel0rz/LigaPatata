
import pandas as pd
from data import dfs

merged_df = pd.concat(dfs)

df_goles = merged_df.groupby(['Jugadores'])['Goles'].sum().sort_values(ascending=False)
df_mvps = merged_df.groupby(['Jugadores'])['MVP'].sum().sort_values(ascending=False)
df_wins = merged_df.groupby(['Jugadores'])['WL'].sum().sort_values(ascending=False)

winloss = []
perc = []
for i in df_wins.values:
    winloss.append(str(i.count('W'))+'-'+str(i.count('L')))
    perc.append(round(i.count('W') / (i.count('W') + i.count('L')) * 100))
jogadores = (list(df_wins.index))

df_wins2 = pd.DataFrame({'Jugadores':jogadores,
                         'TotalWL':winloss,
                         'Win%':perc})
df_wins2.sort_values(by='TotalWL',ascending = False,inplace = True)
df_wins2.reset_index(inplace = True)
df_wins2.drop('index',axis=1,inplace = True)
df_wins2 = df_wins2.sort_values(by=['Win%','TotalWL'],ascending=False)
df_wins2.index = pd.RangeIndex(1,len(df_wins2)+1)


def minimo(x):
    if x == '0-1' or x == '1-0' or x == '1-1' or x == '2-0' or x == '0-2':
        return 0
    else:
        return x
df_wins2['TotalWL'].apply(lambda x: minimo(x))
df_wins2['TotalWL'] = df_wins2['TotalWL'].apply(lambda x: minimo(x))
df_wins2 = df_wins2[df_wins2['TotalWL'] != 0]

def emojis(x):
    if x == 'Javi' or x == 'Hugo':
        return x + ' ' + '\N{fire}'
    elif x == 'Pepe':
        return x + ' ' + '\N{droplet}'
    else:
        return x


df_wins2['Jugadores'] = df_wins2['Jugadores'].apply(lambda x: emojis(x) if x == 'Javi' or x == 'Hugo' or x == 'Pepe' else x)