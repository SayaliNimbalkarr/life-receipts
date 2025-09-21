import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Life Receipts", page_icon="🧾", layout="centered")

st.title("🧾 Life Receipts")
st.caption("Log your daily activities and instantly get a digital receipt.")

# --- FORM SECTION ---
with st.form("activity_form", clear_on_submit=True):
    activity = st.text_input("Activity name*", placeholder="e.g. Reading, Workout")
    category = st.selectbox(
        "Category*", 
        ["Productive", "Health", "Leisure", "Learning", "Other"]
    )
    start_time = st.time_input("Start time*")
    end_time = st.time_input("End time*")
    notes = st.text_area("Notes (optional)", placeholder="Add details if you like…")
    submitted = st.form_submit_button("Add Entry")

    if submitted:
        st.success(f"✅ {activity} logged from {start_time} to {end_time}")

        # Save to a simple in-memory table (or a CSV/database later)
        new_row = {
            "Activity": activity,
            "Category": category,
            "Start": start_time.strftime("%H:%M"),
            "End": end_time.strftime("%H:%M"),
            "Notes": notes,
            "Logged_At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        if "log_df" not in st.session_state:
            st.session_state.log_df = pd.DataFrame(columns=new_row.keys())
        st.session_state.log_df = pd.concat(
            [st.session_state.log_df, pd.DataFrame([new_row])],
            ignore_index=True
        )

# --- DISPLAY SECTION ---
if "log_df" in st.session_state and not st.session_state.log_df.empty:
    st.subheader("Today's Entries")
    st.dataframe(st.session_state.log_df)
else:
    st.info("No activities logged yet.")
