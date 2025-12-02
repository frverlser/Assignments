def calculate_average_sales(sales_list):
    if not sales_list:
        return 0.0
    total = 0
    count = 0
    for sale in sales_list:
        total += sale
        count += 1
    return total / count


def find_top_salesperson(sales_data):
    top_id = None
    top_avg = 0.0

    for employee_id, region, sales_list in sales_data:
        avg = calculate_average_sales(sales_list)

        if top_id is None:
            top_avg = avg
            top_id = employee_id
        else:
            if avg > top_avg:
                top_avg = avg
                top_id = employee_id
            elif avg == top_avg and employee_id < top_id:
                top_id = employee_id

    return top_id


def get_employees_in_region(sales_data, region_name):
    employees = []
    for employee_id, region, sales_list in sales_data:
        if region == region_name:
            employees.append(employee_id)

    a = len(employees)
    for i in range(a):
        for j in range(0, a - i - 1):
            if employees[j] > employees[j + 1]:
                employees[j], employees[j + 1] = employees[j + 1], employees[j]

    return employees


def get_regional_sales_total(sales_data):
    region_total = [] 

    for employee_id, region, sales_list in sales_data:
        total_sales = 0
        for sale in sales_list:
            total_sales += sale

        found = False
        for i in range(len(region_total)):
            if region_total[i][0] == region:
                region_total[i][1] += total_sales
                found = True
                break

        if not found:
            region_total.append([region, total_sales])
    n = len(region_total)
    for i in range(n):
        for j in range(0, n - i - 1):
            if region_total[j][0] > region_total[j + 1][0]:
                region_total[j], region_total[j + 1] = region_total[j + 1], region_total[j]
    result = []
    for item in region_total:
        result.append((item[0], item[1]))

    return result

def analyze_sales_data(sales_data):
    top_salesperson = find_top_salesperson(sales_data)
    north_employees = get_employees_in_region(sales_data, 'North')
    regional_summary = get_regional_sales_total(sales_data)
    return (top_salesperson, north_employees, regional_summary)

sales_data = [
    ('E101', 'North', [50000, 60000, 55000]),
    ('E201', 'South', [70000, 75000, 80000]),
    ('E102', 'North', [85000, 90000, 95000]),
    ('E301', 'West', [65000, 60000, 58000])
]

result = analyze_sales_data(sales_data)
print(result)