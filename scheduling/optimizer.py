import pandas as pd

def assign_crew(flight, crew_df):
    """
    Assigns one available crew member to a flight
    and marks them unavailable after assignment.
    """

    # Filter available crew only
    available_crew = crew_df[
        crew_df["availability"].str.lower() == "yes"
    ]

    if available_crew.empty:
        return pd.DataFrame()

    # Pick first available crew
    assigned = available_crew.iloc[[0]]

    # 🔥 THIS IS THE MISSING LINE 🔥
    crew_df.loc[assigned.index, "availability"] = "No"

    return assigned