import streamlit as st
import pandas as pd
from funcs import df_goles,df_mvps,df_wins
df1 = pd.read_csv('Partido1.csv')
df2 = pd.read_csv('Partido2.csv')
st.title('Liga Patata')

option = st.sidebar.selectbox('Home',
                                      ['HOME','Partidos','Estadisticas'])
if option == 'HOME':
    st.metric(label='Pichichi', value=(df_goles[:1]['Jugadores'][0]+' ' +str(df_goles[:1]['GolesTotales'][0])), delta=3, delta_color="normal", help=None)
    st.metric(label='Maximo MVP', value=(df_mvps[:1]['Jugadores'][0]+' '+ str(df_mvps[:1]['MVPTotales'][0])),
              delta=0, delta_color="normal", help=None)
    st.metric(label='El Victorioso', value=(df_wins.sort_values(by='TotalWL',ascending=False)[:1]['Jugadores'].values[0]+' '+df_wins.sort_values(by='TotalWL',ascending=False)[:1]['TotalWL'].values[0]),
              delta=1, delta_color="normal", help=None)

if option == 'Partidos':
    option2 = st.sidebar.selectbox('Partidos',
                                   ['Jornada1', 'Jornada2'])
    if option2 == 'Jornada1':
        st.dataframe(df1)
    elif option2 == 'Jornada2':
        st.dataframe(df2)

if option == 'Estadisticas':
    option3 = st.sidebar.selectbox('Estadisticas Agregadas',
                                   ['Pichichi', 'MVPs','W/L'])
    if option3 == 'Pichichi':
        st.title('Maximo Goleador')
        st.dataframe(df_goles)
    elif option3 == 'MVPs':
        st.title('Clasificacion MVP')
        st.dataframe(df_mvps)
    elif option3 == 'W/L':
        st.title('Winrate')
        st.dataframe(df_wins)
        