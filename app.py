import streamlit as st
from supabase import create_client
from datetime import datetime

# Connect to your Supabase database
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("Mood App")
st.header("Emotional Log")

Date = st.date_input("Date of emotions")
Event = st.text_input("What event influenced your emotions?")
Emotion = st.text_input("What emotions did you feel?")
Coping = st.text_input("How did you cope with these emotions?")

if st.button("Save Entry"):
    data = {
        "timestamp": str(Date),
        "event": Event,
        "emotion": Emotion,
        "coping": Coping
    }
    supabase.table("moods").insert(data).execute()
    st.success("Entry saved to SQL!")


