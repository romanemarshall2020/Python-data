# Global status report to store messages
status_report: list = []

# Initial state of the sleep study
sleep_study = {
    "maxSheeps": 360,
    "currentCount": 0,
    "remainingSheep": 360,
    "Romane": 150,
    "Shanara": 89,
    "Tracy": 200,
    "count": True
}

def check_sleep_status(sleepstudy: dict):
    """Check the sleep status of individuals and update the global report."""
    global status_report
    keys_to_check = ["Romane", "Tracy", "Shanara"]
    
    for key in keys_to_check:
        if sleepstudy[key] == 0 and f"{key} has fallen asleep" not in status_report:
            # Add to status report only when they fall asleep for the first time
            status_report.append(f"{key} has fallen asleep")
        elif sleepstudy[key] > 0:
            status_report.append(f"{key} is still awake")

def count_sheep(sleepstudy: dict):
    """Decrement sheep count and track who falls asleep."""
    keys_to_decrement = ["maxSheeps", "remainingSheep", "Romane", "Shanara", "Tracy"]

    while sleepstudy["maxSheeps"] > 0 and sleepstudy["count"]:
        # Decrement the counts
        for key in keys_to_decrement:
            sleepstudy[key] -= 1
        
        sleepstudy["currentCount"] += 1

        # Check and update the sleep status
        check_sleep_status(sleepstudy)

        # Print current report after every decrement
        for report in status_report:
            print(report)

        # Stop if all individuals have fallen asleep
        if all(sleepstudy[key] == 0 for key in ["Romane", "Shanara", "Tracy"]):
            sleepstudy["count"] = False
            print("All individuals have fallen asleep.")
            break

    return sleepstudy

# Run the count_sheep function
count_sheep(sleep_study)






	    