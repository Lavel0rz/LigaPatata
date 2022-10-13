
import pandas as pd
from data import dfs
import itertools
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

def gen_wins_dict():


    teamed = []
    x = 0
    for i in range(0, len(merged_df), 5):
        x += 5
        teamed.append((merged_df[['Jugadores', 'WL']][i:x]))

    winners = []
    for i in teamed:
        if 'W' in i['WL'].values:
            winners.append(list(i['Jugadores']))

    tots = (list(itertools.chain.from_iterable(winners)))
    unicos = list(set(tots))

    parejas = {}
    for i in unicos:
        for jugadores in winners:
            if i in jugadores:
                parejas.setdefault(i, []).append(list((set(jugadores) - set([i]))))
    dictglobal = {}
    for dicts in parejas:
        for i in (parejas[dicts]):
            for j in i:
                dictglobal.setdefault(j, []).append(dicts)
    final_dict = {}
    megadict = {}
    for i in dictglobal:
        unique_list = list(set((dictglobal[i])))
        # print(dictglobal[i])
        for j in unique_list:
            # print(dictglobal[i].count(j),j)
            megadict.setdefault(j, []).append((i, dictglobal[i].count(j)))
    real_final_dict = {}
    for i in megadict:
        # print(dict(megadict[i]),i)
        real_final_dict[i] = dict(megadict[i])
    return real_final_dict


def minimo(x):
    if x == '0-1' or x == '1-0' or x == '1-1' or x == '2-0' or x == '0-2':
        return 0
    else:
        return x

def get_lost_dict():
    teamed2 = []
    x = 0
    for i in range(0, len(merged_df), 5):
        x += 5
        teamed2.append((merged_df[['Jugadores', 'WL']][i:x]))

    winners2 = []
    for i in teamed2:
        if 'L' in i['WL'].values:
            winners2.append(list(i['Jugadores']))

    tots2 = (list(itertools.chain.from_iterable(winners2)))
    unicos2 = list(set(tots2))

    parejas2 = {}
    for i in unicos2:
        for jugadores2 in winners2:
            if i in jugadores2:
                parejas2.setdefault(i, []).append(list((set(jugadores2) - set([i]))))
    dictglobal2 = {}
    for dicts2 in parejas2:
        for i in (parejas2[dicts2]):
            for j in i:
                dictglobal2.setdefault(j, []).append(dicts2)
    final_dict2 = {}
    megadict2 = {}
    for i in dictglobal2:
        unique_list2 = list(set((dictglobal2[i])))
        # print(dictglobal[i])
        for j in unique_list2:
            # print(dictglobal[i].count(j),j)
            megadict2.setdefault(j, []).append((i, dictglobal2[i].count(j)))
    real_final_dict2 = {}
    for i in megadict2:
        # print(dict(megadict[i]),i)
        real_final_dict2[i] = dict(megadict2[i])
    return real_final_dict2
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


df_wins2['Jugadores'] = df_wins2['Jugadores'].apply(lambda x: emojis(x) if x == 'Javi' or x == 'Hugo' or x == 'Pepe' else x
