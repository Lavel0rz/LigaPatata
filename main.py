import streamlit as st
from funcs import *
from data import dfs
import pandas as pd

st.set_page_config(page_title="LigaPatata", page_icon="soccer", initial_sidebar_state='expanded',layout="wide")
st.title('Liga Patata')
st.sidebar.image(r"patata.jpg", use_column_width=True)

with st.sidebar:
        st.subheader('Welcome to La Liga Patata')

option = st.sidebar.radio('Menu',
                                      ['HOME','Partidos','Estadisticas'])


if option == 'HOME':
    col1, col2,col3 = st.columns(3)
    with col1:
        st.metric(label='Pichichi', value=(df_goles.index[0]+ ' '+str(round(df_goles.values[0]))), delta=3, delta_color="normal")
    with col2:
        st.metric(label='Maximo MVP', value=(df_mvps.index[0]+' '+ str(round(df_mvps.values[0]))),
                  delta=1, delta_color="normal")
    with col3:
        st.metric(label='El Victorioso', value=(df_wins2.sort_values(by=['Win%','TotalWL'],ascending=False)[:1]['Jugadores'].values[0]+' '+df_wins2.sort_values(by=['Win%','TotalWL'],ascending=False)[:1]['TotalWL'].values[0]),
                  delta=1, delta_color="normal")
    col4,col5 = st.columns(2)
    with col4:
        st.plotly_chart(figure_or_data=fig)
    with col5:
        st.plotly_chart(figure_or_data=fig2)
    df = pd.DataFrame(dict(
        value=[6, 4, 8, 10, 10,
               9, 10, 6, 9, 10],
        variable=['Gol', 'Porteria', 'Magia', 'Tercer Tiempo', 'Espiritu',
                  'Gol', 'Porteria', 'Magia', 'Tercer Tiempo', 'Espiritu'],
        jugadores=['Pepe', 'Pepe', 'Pepe', 'Pepe', 'Pepe',
                   'Hugo', 'Hugo', 'Hugo', 'Hugo', 'Hugo']))

    fig = px.line_polar(df, r='value', theta='variable', line_close=True,
                        color='jugadores', color_discrete_map={'A': 'blue', 'B': 'red'})
    fig.update_traces(fill='toself')

    #st.pyplot(fig3)


    st.markdown("<h1 style='text-align: center; color: blue;'>Performance</h1>", unsafe_allow_html=True)
    st.plotly_chart(figure_or_data=fig)

if option == 'Partidos':
    option2 = st.radio('Partidos',
                                   ['Jornada1', 'Jornada2','Jornada3','Jornada4','Jornada5'])
    if option2 == 'Jornada1':
        st.table(dfs[0])
    elif option2 == 'Jornada2':
        st.table(dfs[1])

    elif option2 == 'Jornada3':
        st.table(dfs[2])

    elif option2 == 'Jornada4':
        st.table(dfs[3])
                                    
    elif option2 == 'Jornada5':
        st.table(dfs[4])                               

if option == 'Estadisticas':
    option3 = st.radio('Estadisticas Agregadas',
                                   ['Pichichi', 'MVPs','W/L','MejoresCompis'])
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
    elif option3 == 'MejoresCompis':
        dict = gen_wins_dict()
        col1, col2 = st.columns(2)
        with col1:
            mejores = st.checkbox('Con que Jugador gano mas')


        if mejores:
            compi = st.selectbox(options = dict.keys(),label = 'Jugador')
            value = []
            names = []
            for k,v in dict[compi].items():
                names.append(k)
                value.append(v)
            df = pd.DataFrame({'Companeros': names, 'Partidos Ganados': value})
            df.sort_values(by='Partidos Ganados', ascending=False, inplace=True)
            df = df[:3].reset_index().set_index(pd.RangeIndex(1, len(df[:3]) + 1))
            df.drop('index', axis=1, inplace=True)
            st.table(df)
