first_title = (input("Book title 1:\n"))
first_price = float(input("Book price 1:\n"))
quantity1 = int(input("How many books? \n"))

second_title = (input("Book title 2:\n"))
second_price = float(input("Book price 2:\n"))
quantity2 = int(input("How many books?\n"))

third_title = (input("Book title 3:\n"))
third_price = float(input("Book price 3:\n"))
quantity3 = int(input("How many books?\n"))

name = input("Your name:\n")
status = input("Are you a staff?  yes/no :\n ")
order = input("Is textbook order?  yes/no:\n ")

is_faculty_staff = (status == "yes")
is_text_order = (order == "yes")
subtotal = (quantity1 * first_price) + (second_price*quantity2)+(third_price*quantity3)
quantity = quantity1 + quantity2 + quantity3
staff_dis = subtotal * 0.2
order_dis = subtotal*0.25
faculty_discount = subtotal * 0.20 * is_faculty_staff
textbook_discount = subtotal*0.25*is_text_order
main_discount = faculty_discount * (faculty_discount >= textbook_discount) + textbook_discount*(textbook_discount > faculty_discount)
order_applied = (textbook_discount >= faculty_discount)*is_text_order
faculty_applied = (faculty_discount > textbook_discount)*is_faculty_staff
applied_dis = ("Order discount")*order_applied + faculty_applied*("Faculty discount")
applied_discount_name = applied_dis or "No Discount"
bulk_discount = subtotal * 0.08 * (quantity >= 10)
total_dis = main_discount+bulk_discount
small_order_fee = (quantity < 3) * 10000
after_dis = subtotal-total_dis+small_order_fee
tax_fee = after_dis*0.05*(is_text_order == False)
shipping = 20000*(after_dis < 200000)
final_total = shipping+after_dis+tax_fee
saving = total_dis-(tax_fee+shipping+small_order_fee)
print("\n----- RECEIPT -----\n")
print("Customer name:", name)
print("Faculty/Staff:", is_faculty_staff)
print("Textbook order:", is_text_order)
print("\nItems Purchased:")
print("1.", first_title, "—", quantity1, "*", first_price, "=", quantity1 * first_price)
print("2.", second_title, "—", quantity2, "*", second_price, "=", quantity2 * second_price)
print("3.", third_title, "—", quantity3, "*", third_price, "=", quantity3 * third_price)
print("Subtotal:", subtotal)
print("Faculty discount:", faculty_discount)
print("Eligibility: ", is_faculty_staff)
print("Textbook discount:", textbook_discount)
print("Eligibility: ", is_text_order)
print("Applied discount: ", applied_discount_name)
print("Main discount:", main_discount)
print("Bulk discount:", bulk_discount)
print("Total discount:", total_dis)
print("Small order fee:", small_order_fee)
print("Subtotal after fees and dicounts:",after_dis)
print("Tax:", tax_fee)
print("Shipping:", shipping)
print("Final total:", final_total)
print("Net savings:", saving)
