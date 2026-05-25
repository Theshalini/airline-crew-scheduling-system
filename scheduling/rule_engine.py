def is_crew_available(crew_row, flight_duration):
    """
    Checks duty + rest time constraints
    """
    MAX_DUTY_HOURS = 8

    return (crew_row["duty_hours"] + flight_duration) <= MAX_DUTY_HOURS