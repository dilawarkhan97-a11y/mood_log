import streamlit as st

st.title("Mood App")
st.header("Emotional Log")

Date = st.date_input("What is the date of emotions?")
Event = st.text_input("What event influenced your emotions?")
Emotions = st.text_input("What emotions did you feel?")
Coping = st.text_input("How did you cope or block these emotions?")

if st.button("Save Entry"):
    st.success("Entry recorded (but not saved anywhere yet).")

