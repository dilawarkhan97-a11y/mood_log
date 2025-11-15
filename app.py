import streamlit as st
from postgrest import PostgrestClient
from datetime import datetime

# Connect to Supabase REST endpoint
url = st.secrets["SUPABASE_URL"] + "/rest/v1"
key = st.secrets["SUPABASE_KEY"]

client = PostgrestClient(url, headers={"apikey": key, "Authorization": f"Bearer {key}"})

st.title("Mood App")
st.header("Emotional Log")

Date = st.date_input("Date of emotions")
Event = st.text_input("What event influenced your emotions?")
Emotion = st.text_input("What emotions did you feel?")
Coping = st.text_input("How did you cope with these emotions?")

if st.button("Save entry"):
    row = {
        "timestamp": str(Date),
        "event": Event,
        "emotion": Emotion,
        "coping": Coping,
    }

    try:
        response = client.from_("moods").insert(row).execute()
        st.write("Insert response:", response)
        st.success("Saved to SQL!")
    except Exception as e:
        st.error("Insert error:")
        st.exception(e)

st.markdown("---")

if st.button("Show saved logs"):
    try:
        data = client.from_("moods").select("*").execute()
        st.write(data)
    except Exception as e:
        st.error("Select error:")
        st.exception(e)


