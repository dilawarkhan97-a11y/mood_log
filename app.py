import streamlit as st
import json
from datetime import datetime

FILE= "mood_log.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
def save_entry(entry):
    data=load_data()
    data.append(entry)
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
        
st.title("Mood App(JSON)")

st.header("Emotional log")

mood = st.selectbox("Mood", ["Great", "Good","Normal","Sad","Awful"])
note =st.text_area("Event")

if st.button("Save"):
    entry ={
        "time" : datetime.now().isoformat(timespec="seconds"),
        "mood" : mood,
        "Event" : note
    }
    save_entry(entry)
    st.success("Entry Saved")

st.subheader("Previous entries")
st.json(load_data())

