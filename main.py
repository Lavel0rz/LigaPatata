import streamlit as st
from funcs import df_wins2, df_goles, df_mvps
from data import dfs

st.set_page_config(page_title="LigaPatata", page_icon="soccer", initial_sidebar_state='expanded')
st.title('Liga Patata')
st.sidebar.image(r"patata.jpg", use_column_width=True)

with st.sidebar:
        st.subheader('Welcome to La Liga Patata')

option = st.sidebar.selectbox('Home',
                                      ['HOME','Partidos','Estadisticas'])


if option == 'HOME':
    st.metric(label='Pichichi', value=(df_goles.index[0]+ ' '+str(round(df_goles.values[0]))), delta=3, delta_color="normal")
    st.metric(label='Maximo MVP', value=(df_mvps.index[0]+' '+ str(round(df_mvps.values[0]))),
              delta=1, delta_color="normal")
    st.metric(label='El Victorioso', value=(df_wins2.sort_values(by=['Win%','TotalWL'],ascending=False)[:1]['Jugadores'].values[0]+' '+df_wins2.sort_values(by=['Win%','TotalWL'],ascending=False)[:1]['TotalWL'].values[0]),
              delta=1, delta_color="normal")

if option == 'Partidos':
    option2 = st.sidebar.selectbox('Partidos',
                                   ['Jornada1', 'Jornada2','Jornada3','Jornada4'])
    if option2 == 'Jornada1':
        st.table(dfs[3])
    elif option2 == 'Jornada2':
        st.table(dfs[2])

    elif option2 == 'Jornada3':
        st.table(dfs[1])

    elif option2 == 'Jornada4':
        st.table(dfs[0])

if option == 'Estadisticas':
    option3 = st.sidebar.selectbox('Estadisticas Agregadas',
                                   ['Pichichi', 'MVPs','W/L'])
    if option3 == 'Pichichi':
        st.title('Maximo Goleador')
        st.table(df_goles)
    elif option3 == 'MVPs':
        st.title('Clasificacion MVP')
        st.table(df_mvps)
    elif option3 == 'W/L':
        st.title('Winrate')
        st.subheader('Minimo 3 Partidos Jugados')
        st.table(df_wins2)

