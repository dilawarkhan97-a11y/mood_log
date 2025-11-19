import streamlit as st
import json
from datetime import datetime
import os
import pandas as pd

FILE = os.path.join(os.path.dirname(__file__), "mood_log.json")

def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_entry(entry):
    data = load_data()
    data.append(entry)
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

st.title("Mood App (JSON)")

st.header("Emotional Log")

mood = st.selectbox("Mood", ["Great", "Good", "Normal", "Sad", "Awful"])
intensity = st.text_input("Intensity (1–10)")
note = st.text_area("What caused it?")
context = st.text_area("What was going on in the background?")
uncertainty = st.selectbox("Is uncertainty involved?", ["Yes", "No"])

if st.button("Save"):
    entry = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "mood": mood,
        "intensity": intensity,
        "cause": note,
        "context": context,
        "uncertainty": uncertainty
    }
    save_entry(entry)
    st.success("Entry Saved!")

# -------- Display entries as table -------- #

st.subheader("Previous Entries")

data = load_data()

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.info("No entries yet.")

