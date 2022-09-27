import pandas as pd
import emoji
from functools import reduce
from data import dfs



df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Jugadores'],
                                            how='outer'), dfs).fillna(0)

df_goles = df_merged.groupby(['Jugadores'])['Goles_x'].sum() + round(df_merged.groupby(['Jugadores'])['Goles_y'].sum()) +round(df_merged.groupby(['Jugadores'])['Goles'].sum())
df_goles = df_goles.sort_values(ascending = False)
df_goles = df_goles.astype(int)
df_mvps = df_merged.groupby(['Jugadores'])['MVP_x'].sum() + round(df_merged.groupby(['Jugadores'])['MVP_y'].sum()) +round(df_merged.groupby(['Jugadores'])['MVP'].sum())
df_mvps = df_mvps.sort_values(ascending = False)
df_mvps = df_mvps.astype(int)
df_wins = df_merged.groupby(['Jugadores'])['W/L_x'].sum().astype(str) + df_merged.groupby(['Jugadores'])['W/L_y'].sum().astype(str) +df_merged.groupby(['Jugadores'])['W/L'].sum().astype(str)
print(df_goles.values)
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

def emojis(x):
    if x == 'Javi' or x == 'Fran':
        return x + ' ' + emoji.emojize(':fire:')
    elif x == 'Pepe':
        return x + ' ' + emoji.emojize(':droplet:')
    else:
        return x


df_wins2['Jugadores'] = df_wins2['Jugadores'].apply(lambda x: emojis(x))