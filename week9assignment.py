def calculate_bid(bid_text):
    texts = bid_text.split("\n")
    subtotal = 0
    fee_rate = 0
    deposit = 0
    for text in texts:
        if "hrs at" in text:
            part = text.split()

            hours = float(part[2])          
            rate = float((part[5]).replace("$","").replace("/hr",""))     

            subtotal = subtotal + hours * rate

        if text[:4] == "FEE:":
            fee_str = text.split()[1] 
            fee_num = fee_str.replace("%","")
            fee_rate = float(fee_num) / 100

        if text[:8] == "DEPOSIT:":
            deposit_str = text.split()[1]
            deposit_num = deposit_str.replace("$","")
            deposit = float(deposit_num)
    total = (subtotal - deposit) * (1 + fee_rate)
    return f"${total:.2f}"



    # Test Case 1: Standard bid
bid1 = """Framing -> 10 hrs at $50.00/hr
Wiring -> 5 hrs at $80.00/hr
FEE: 10%
DEPOSIT: $100.00"""
print(calculate_bid(bid1))

# Test Case 2: No deposit
bid2 = """Plumbing -> 2 hrs at $100.00/hr
Cleanup -> 1 hrs at $20.00/hr
FEE: 5%"""
print(calculate_bid(bid2))

# Test Case 3: Deposit, no fee
bid3 = """Painting -> 4 hrs at $25.00/hr
Sanding -> 2 hrs at $15.00/hr
DEPOSIT: $30.00
FEE: 0%"""
print(calculate_bid(bid3))