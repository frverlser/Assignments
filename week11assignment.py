# Format: {Class: {"cost": int}}
schedule = {
    "Yoga":   {"cost": 5},
    "Boxing": {"cost": 10}
}

# Format: {ID: {"credits": int, "pass_type": str}}
members = {
    "M1": {"credits": 20, "pass_type": "Standard"},
    "M2": {"credits": 5,  "pass_type": "Premium"} # Free classes
}

queue = [
    ("M1", "Yoga", 2),      # Valid. Cost: 10. Rem: 10.
    ("M2", "Boxing", 10),   # Valid. Cost: 0 (Premium). Rem: 5.
    ("M1", "Boxing", 2),    # Error: Cost 20 > 10.
    ("M9", "Zumba", 1),     # Error: Member ID not found.
    ("M1", "Pilates", 1),   # Error: Class not found.
    ("M2", "Yoga", 0)       # Error: Spots must be positive integer.
]
def book_session(members_db, schedule_db, member_id, class_name, spots):
    if member_id not in members_db:
        raise KeyError("Member ID not found")
    if class_name not in schedule_db:
        raise KeyError("Class not found")
    if type(spots) != int or spots < 1:
        raise ValueError("Spots must be positive integer")
    total_credits = spots * schedule_db[class_name]["cost"]
    if members_db[member_id]["pass_type"] == "Premium":
        total_credits = 0
    if members[member_id]["credits"] <= total_credits:
        raise ValueError("Insufficient credits")
    return total_credits

def  process_gym_bookings(members_db, schedule_db, booking_queue):
    counter = 0
    declined = 0
    for id, class_name, spots in booking_queue:
        try:
            abc = book_session(members_db, schedule_db, id, class_name, spots)
            counter += abc
        except (KeyError, ValueError) as e :
            print(f"Booking Error for {id}: {e}")
            declined += 1
    return {'credits_used': counter, 'declined_bookings': declined}

print(process_gym_bookings(members, schedule, queue))    
