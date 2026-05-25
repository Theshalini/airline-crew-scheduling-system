import streamlit as st
import base64
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Airline Crew Scheduling System",
    layout="wide"
)

# --------------------------------------------------
# BACKGROUND FUNCTION
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

        /* NAVBAR BUTTON STYLE */
        div.stButton > button {{
            margin-right: 10px;
            border-radius: 10px;
            padding: 4px 8px;
            font-weight: 500;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# 👉 change path if needed
set_background("assets/bg.jpg")

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center; font-size:20px;">
        ✈️ Airline Crew Scheduling System
    </h1>
    <p style="text-align:center; font-size:16px;">
        Machine Learning Assisted Crew Assignment & Rescheduling System
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# SESSION STATE TAB CONTROL
# --------------------------------------------------
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "home"

# --------------------------------------------------
# NAVBAR BUTTONS
# --------------------------------------------------
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

with col1:
    if st.button("🏠 Home"):
        st.session_state.active_tab = "home"

with col2:
    if st.button("📂 Dataset Preview"):
        st.session_state.active_tab = "dataset"

with col3:
    if st.button("🧠 Assign Crew"):
        st.session_state.active_tab = "assign"

with col4:
    if st.button("🤖 Model Info"):
        st.session_state.active_tab = "model"

with col5:
    if st.button("🧾 About"):
        st.session_state.active_tab = "about"

st.divider()

# --------------------------------------------------
# TAB CONTENT AREA
# --------------------------------------------------
tab = st.session_state.active_tab

# --------------------------------------------------
# HOME TAB (LIKE YOUR FIRST UI)
# --------------------------------------------------
if tab == "home":

    st.markdown(
    """
    <h2 style="text-align:left;">Welcome to the Airline Crew Scheduling Dashboard.</h2>
    <p style="font-size:18px;">
        Upload your datasets to begin crew assignment and scheduling.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# UPLOAD SECTION (LIKE YOUR FIRST UI)
# --------------------------------------------------

st.markdown("## 📂 Upload Datasets")

col1, col2 = st.columns(2)

with col1:
    flights_file = st.file_uploader(
        "Upload Flights CSV",
        type=["csv"],
        key="home_flights"
    )

with col2:
    crew_file = st.file_uploader(
        "Upload Crew CSV",
        type=["csv"],
        key="home_crew"
    )

# --------------------------------------------------
# STATUS MESSAGE
# --------------------------------------------------

if flights_file and crew_file:
    st.success("✅ Flights and Crew datasets uploaded successfully")



# --------------------------------------------------
# DATASET TAB
# --------------------------------------------------
elif tab == "dataset":

    st.header("📂 Dataset Preview")
    st.info("Dataset preview will be added here.")


# --------------------------------------------------
# ASSIGN TAB
# --------------------------------------------------
elif tab == "assign":

    st.header("🧠 Assign Crew")
    st.info("Crew assignment UI will go here.")


# --------------------------------------------------
# MODEL TAB
# --------------------------------------------------
elif tab == "model":

    st.header("⚙ Model Information")
    st.info("Model architecture + ML explanation here.")


# --------------------------------------------------
# ABOUT TAB
# --------------------------------------------------
elif tab == "about":

    st.header("🧾 About")
    st.info("Project details, authors, and description.")