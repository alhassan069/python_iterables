sales_data = [
("Q1", [("Jan",1000), ("Feb",1200), ("Mar",1100)]),
("Q2",[("Apr", 1300), ("May",1250), ("Jun", 1400)]),
("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep",1300)])
]

highest_sale_month = ("",0)
monthly_sales = []
print("Total Sales for each quarter")
for quarter in sales_data:
    name, months = quarter
    total = 0
    for month in months:
        monthly_sales.append(month)
        if month[1] > highest_sale_month[1]:
            highest_sale_month = month
        total += month[1]
    print(name, total)
print("Highest Sale month")
print(highest_sale_month)

print("Monthly Sales")
print(monthly_sales)
