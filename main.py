import streamlit as st
from funcs import dfs, df_wins2, df_goles, df_mvps

st.set_page_config(page_title="LigaPatata", page_icon="soccer", initial_sidebar_state='expanded')
st.title('Liga Patata')
st.sidebar.image(r"patata.jpg", use_column_width=True)
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('patataimagen.png')
with st.sidebar:
        st.subheader('Welcome to La Liga Patata')

option = st.sidebar.selectbox('Home',
                                      ['HOME','Partidos','Estadisticas'])


if option == 'HOME':
    st.metric(label='Pichichi', value=(df_goles.index[0]+ ' '+str(round(df_goles.values[0]))), delta=3, delta_color="normal", help=None)
    st.metric(label='Maximo MVP', value=(df_mvps.index[0]+' '+ str(round(df_mvps.values[0]))),
              delta=1, delta_color="normal", help=None)
    st.metric(label='El Victorioso', value=(df_wins2.sort_values(by='TotalWL',ascending=False)[:1]['Jugadores'].values[0]+' '+df_wins2.sort_values(by='TotalWL',ascending=False)[:1]['TotalWL'].values[0]),
              delta=1, delta_color="normal", help=None)

if option == 'Partidos':
    option2 = st.sidebar.selectbox('Partidos',
                                   ['Jornada1', 'Jornada2','Jornada3'])
    if option2 == 'Jornada1':
        st.table(dfs[0])
    elif option2 == 'Jornada2':
        st.table(dfs[1])

    elif option2 == 'Jornada3':
        st.table(dfs[2])

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
        st.table(df_wins2)
        