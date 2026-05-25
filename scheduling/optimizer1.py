import pandas as pd

def assign_crew(flight, crew_df):
    """
    Simple rule-based crew assignment.
    Does NOT depend on aircraft_type.
    """

    # Default: every flight needs 1 pilot + 1 cabin crew
    required_roles = ["Pilot", "Cabin"]

    assigned = []

    for role in required_roles:
        available = crew_df[crew_df["role"] == role]

        if available.empty:
            continue

        # Pick first available crew
        assigned.append(available.iloc[0])

    if not assigned:
        return pd.DataFrame()

    return pd.DataFrame(assigned)