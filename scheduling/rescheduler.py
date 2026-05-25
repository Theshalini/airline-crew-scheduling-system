def mark_crew_unavailable(crew_df, crew_id, reason="Sick"):
    crew_df.loc[crew_df["crew_id"] == crew_id, "status"] = reason
    crew_df.loc[crew_df["crew_id"] == crew_id, "availability"] = "No"
    return crew_df