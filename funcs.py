import pandas as pd
import numpy as np


jugadores = []
gol = []
df1 = pd.read_csv('Partido1.csv')
df2 = pd.read_csv('Partido2.csv')
Todos = list(set(list(df1['Jugadores']) + list(df2['Jugadores'])))
for jugador in Todos:
    if jugador in list(df1['Jugadores']) and jugador in list(df2['Jugadores']):
        gol.append(df1.groupby(['Jugadores'])['Goles'].sum()[jugador] + df2.groupby(['Jugadores'])['Goles'].sum()[
            jugador]), jugadores.append(jugador)
    elif jugador in list(df1['Jugadores']) and jugador not in list(df2['Jugadores']):
        gol.append(df1.groupby(['Jugadores'])['Goles'].sum()[jugador]), jugadores.append(jugador)
    else:
        gol.append(df2.groupby(['Jugadores'])['Goles'].sum()[jugador]), jugadores.append(jugador)

df_goles = pd.DataFrame({'Jugadores': jugadores,
                         'GolesTotales': gol})
df_goles.sort_values(by='GolesTotales', ascending=False, inplace=True)
df_goles.reset_index(inplace=True)
df_goles.drop('index', axis=1, inplace=True)

mvps = []
jogadores = []
for jugador in Todos:
    if jugador in list(df1['Jugadores']) and jugador in list(df2['Jugadores']):
        mvps.append(df1.groupby(['Jugadores'])['MVP'].sum()[jugador] + df2.groupby(['Jugadores'])['MVP'].sum()[
            jugador]), jogadores.append(jugador)
    elif jugador in list(df1['Jugadores']) and jugador not in list(df2['Jugadores']):
        mvps.append(df1.groupby(['Jugadores'])['MVP'].sum()[jugador]), jogadores.append(jugador)
    else:
        mvps.append(df2.groupby(['Jugadores'])['MVP'].sum()[jugador]), jogadores.append(jugador)

df_mvps = pd.DataFrame({'Jugadores': jogadores,
                        'MVPTotales': mvps})
df_mvps.sort_values(by='MVPTotales', ascending=False, inplace=True)
df_mvps.reset_index(inplace=True)
df_mvps.drop('index', axis=1, inplace=True)

wins = []
jogadores = []
winloss = []
perc = []
for jugador in Todos:
    if jugador in list(df1['Jugadores']) and jugador in list(df2['Jugadores']):
        wins.append(df1.groupby(['Jugadores'])['W/L'].sum()[jugador] + df2.groupby(['Jugadores'])['W/L'].sum()[jugador]),jogadores.append(jugador)
    elif jugador in list(df1['Jugadores']) and jugador not in list(df2['Jugadores']):
        wins.append(df1.groupby(['Jugadores'])['W/L'].sum()[jugador]),jogadores.append(jugador)
    else:
        wins.append(df2.groupby(['Jugadores'])['W/L'].sum()[jugador]),jogadores.append(jugador)
for i in wins:
    try:
        winloss.append(str(i.count('W'))+'-'+str(i.count('L')))
        perc.append(round(i.count('W')/(i.count('W')+i.count('L'))*100))

    except:
        print(0)
df_wins = pd.DataFrame({'Jugadores':jogadores,
                         'TotalWL':winloss,
                         'Win%':perc})
df_wins.sort_values(by='Win%',ascending = False,inplace = True)
df_wins.reset_index(inplace = True)
df_wins.drop('index',axis=1,inplace = True)