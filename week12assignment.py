def process_donations(filename):
    data = """Alice,HomelessShelter,200,100
Bob,FoodBank,50,50
Charlie,HomelessShelter,400,200
Diana,AnimalRescue,1000,0
Corrupt,Line,No,Money
Eve,FoodBank,20,10
Frank,AnimalRescue,300,300"""
    with open(filename, "w") as file:
        file.write(data)
        
    with open(filename, "r") as filename:
        cause_totals = {}
        top_donors = []
        for line in filename:
            try:
                name, cause, cashamount, checkamount = line.strip().split(",")
                total = int(cashamount) + int(checkamount)
                cause_totals[cause] = cause_totals.get(cause, 0) + total
                if total > 500:
                    top_donors.append((name, total))
            except ValueError:
                continue
    return cause_totals, top_donors

def write_fundraising_report(cause_totals, top_donors):
    with open("fundraising_summary.txt", "w") as f:
        f.write("FUNDS RAISED PER CAUSE\n----------------------\n")
        for cause, total in cause_totals.items():
            f.write(f"{cause}: ${total:.2f}\n")
        f.write("\nGOLD TIER DONORS\n")
        f.write("---------------------\n")
        for name, total in top_donors:
            f.write(f"{name}: (${total:.2f})\n")

cause_totals, top_donors = process_donations("donations.txt")
write_fundraising_report(cause_totals, top_donors)