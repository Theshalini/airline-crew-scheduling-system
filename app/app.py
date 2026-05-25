import sys
import os
import base64
import streamlit as st
import pandas as pd

# --------------------------------------------------
# Fix Python path
# --------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from scheduling.optimizer import assign_crew

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Airline Crew Scheduling System",
    layout="wide"
)

# --------------------------------------------------
# Background image
# --------------------------------------------------
def set_background(image_path):
    if not os.path.exists(image_path):
        return

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background(os.path.join(ROOT_DIR, "assets", "bg.jpg"))

# --------------------------------------------------
# Title (FORCED SINGLE LINE)
# --------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center; white-space:nowrap;">
        ✈️ Airline Crew Scheduling System
    </h1>
    <p style="text-align:center; font-size:18px;">
        Machine Learning Assisted Crew Assignment & Rescheduling
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Upload datasets
# --------------------------------------------------
st.subheader("📂 Upload Datasets")

col1, col2 = st.columns(2)

with col1:
    flights_file = st.file_uploader("Upload Flights CSV", type=["csv"])

with col2:
    crew_file = st.file_uploader("Upload Crew CSV", type=["csv"])

# --------------------------------------------------
# Load datasets
# --------------------------------------------------
if flights_file and crew_file:
    flights_df = pd.read_csv(flights_file)
    crew_df = pd.read_csv(crew_file)

    # --------------------------------------------------
    # SAFETY FIXES
    # --------------------------------------------------

    # flight_number handling
    if "flight_number" not in flights_df.columns:
        if "flight" in flights_df.columns:
            flights_df["flight_number"] = flights_df["flight"].astype(str)
        else:
            flights_df["flight_number"] = [
                f"FL{1000 + i}" for i in range(len(flights_df))
            ]

    # Default crew_needed if missing
    if "crew_needed" not in flights_df.columns:
        flights_df["crew_needed"] = "Pilot"

    # Default availability if missing
    if "availability" not in crew_df.columns:
        crew_df["availability"] = "Yes"

    # --------------------------------------------------
    # SESSION STATE (KEY FIX 🔥)
    # --------------------------------------------------
    if "crew_state" not in st.session_state:
        st.session_state.crew_state = crew_df.copy()

    crew_df = st.session_state.crew_state

    st.success("Datasets loaded successfully!")

    # --------------------------------------------------
    # Preview datasets
    # --------------------------------------------------
    st.subheader("✈️ Flight Dataset Preview")
    st.dataframe(flights_df.head(10), use_container_width=True)

    st.subheader("👩‍✈️ Crew Dataset Preview")
    st.dataframe(crew_df.head(10), use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # Crew Assignment Section
    # --------------------------------------------------
    st.subheader("🧠 Crew Assignment")

    selected_flight = st.selectbox(
        "Select Flight Number",
        flights_df["flight_number"].unique()
    )

    flight_row = flights_df[
        flights_df["flight_number"] == selected_flight
    ].iloc[0]

    colA, colB = st.columns(2)

    with colA:
        if st.button("Assign Crew"):
            try:
                assignment = assign_crew(flight_row, crew_df)

                if assignment.empty:
                    st.warning("No suitable crew found for this flight.")
                else:
                    st.success("Crew assigned successfully!")
                    st.dataframe(assignment, use_container_width=True)

                    # Save updated crew state
                    st.session_state.crew_state = crew_df

            except Exception as e:
                st.error(f"Assignment failed: {e}")

    with colB:
        if st.button("🔄 Reset Crew Assignments"):
            st.session_state.crew_state = crew_df.copy()
            st.success("Crew availability reset.")

else:
    st.info("Please upload both Flights and Crew datasets to continue.")