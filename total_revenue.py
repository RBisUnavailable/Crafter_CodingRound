import csv

def calculate_total_revenue(csv_file_name):
    total_revenue = 0
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header row
        for row in reader:
            sales_value = float(row[1])
            total_revenue += sales_value
    return total_revenue
