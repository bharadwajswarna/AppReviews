import streamlit as st
import pandas as pd

header = st.container()
reviewfilter = st.container()
parameters_desc = st.container()
parameters = st.container()
skills_container = st.container()

with header:
    st.title('App Reviews Analysis')

with reviewfilter:
    import pickle
    file = open("topic_hdfc.pkl",'rb')
    df = pickle.load(file)
    file.close()

    genre = st.radio(
     "Choose a theme",
     ('1', '2', '3','4'))

    if genre == '1':
        st.write(df)
        #st.write(df.loc[df['Dominant_Topic']==1.0)
    elif genre == '2':
        st.write(df[df['Dominant_Topic']]==2.0)
    elif genre == '3':
        st.write(df.loc[df.Dominant_Topic]==3.0)
    elif genre == '4':
        st.write(df.loc[df.Dominant_Topic]==4.0)




