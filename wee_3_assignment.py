print("=== Laundromat Service Calculator ===")
print("Enter machine size: small, medium, or large. Type 'done' when finished selecting loads")
total=0.0
while True:
    size=input("Enter machine size: ")
    if size=="done":
        break
    elif size=="small":
        price=4.50
        print("Price: 4.50$")
    elif size=="medium":
        price=6.50
        print("Price: 6.50$")
    else:
        price=9.00
        print("Price: 9.00$")

    total+=float(price)
    print(f"Current total: {total:.2f} \n")

print("\n=== Service Summary ===")
print(f"Subtotal: ${total:.2f}")

if total>=30.00:
    print("Frequent Customer Discount: -$4.00")
    total-=4.00

print(f"Final Total: ${total:.2f}")
print("Thank you for your business!")