def group_expenses(transaction_list):
    result = {}
    for item in transaction_list:
        date, category, cost = item.split("/")
        cost = float(cost)
        if category not in result:
            result[category] = []
        result[category].append((date, cost))
    return result

def summarize_budget(expense_dict):
    sum = {}
    for category, entries in expense_dict.items():
        total = 0
        for date, cost in entries:
            total += cost 
        sum[category] = total
    return sum

transaction_list = [
    "01-Oct/Food/15.50",
    "02-Oct/Gas/40.00",
    "03-Oct/Food/12.25",
    "04-Oct/Rent/800.00",
    "05-Oct/Gas/35.00",
    "05-Oct/Food/8.75"
]

grouped = group_expenses(transaction_list)
summary = summarize_budget(grouped)

for category, total in summary.items():
    print(f"{category} : ${total:.2f} total")
