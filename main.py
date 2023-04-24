import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("# NBA Fantasy ")
st.sidebar.markdown("# NBA data for seasons 1996-2021")


st.subheader('Content')
st.text(' In recent years the NBA has seen an explosive growth in popularity.\n Along with the growth in popularity of the NBA, NBA fantasy has becoming more and more popular. \n NBA Fantasy is a game where fans can create their own league with friends and then draft their own fantasy teams with players of NBA Players. \n The fans then earn points each week for how each of their players perform week. \n They compete against each other in weekly matchups to see who created the best fantasy team.')

st.subheader('Recent Year Stats')
games, playerstats, salarydata = st.tabs(
    ['Games', 'Player stats', 'Salary data'])


with games:
    games = pd.read_csv("data\games.csv")
    st.write('## Games Data')
    st.write(games)
    Bargames = alt.Chart(games).mark_bar().encode(
        x='awayTeam',
        y=alt.Y('pointsAway', sort='-x'),
        color='awayTeam',
        tooltip=['pointsAway'],
    )
    st.altair_chart(Bargames, use_container_width=True)
with playerstats:
    playerstats = pd.read_csv("data\player_info.csv")
    st.write('## Players Data')
    st.write(playerstats)
    top20playerstats = playerstats.head(20)
    st.write(top20playerstats)
    Bartop20playerstats = alt.Chart(top20playerstats).mark_bar().encode(
        x='playerName',
        y=alt.Y('Colleges', sort='-x'),
        color='playerName',
        tooltip=['Colleges'],
    )
    st.altair_chart(Bartop20playerstats, use_container_width=True)
with salarydata:
    salarydata = pd.read_csv("data\salaries.csv")
    st.write('## Salary Data')
    st.write(salarydata)
    top20salarydata = salarydata.head(20)
    Bartop20salarydata = alt.Chart(top20salarydata).mark_bar().encode(
        x='playerName',
        y=alt.Y('salary', sort='-x'),
        color='salary',
        tooltip=['salary'],
    )
    st.altair_chart(Bartop20salarydata, use_container_width=True)
