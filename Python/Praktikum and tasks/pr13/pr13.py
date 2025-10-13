from collections import defaultdict

from unicodedata import category


def read_data(name_file):
    with open(name_file, "r") as file:
        list_sales =  file.readlines()
    sales = []
    for sale in list_sales:
        list_sale = sale.strip().split(',')
        dict_sale = {
            'name': list_sale[0],
            'date': list_sale[1],
            'amount': list_sale[2],
            'category': list_sale[3],
            'year': list_sale[1][:4],
            'month': list_sale[1][5:7]
        }
        sales.append(dict_sale)
    return sales


def process_data(raw_data):
    dict_groups = defaultdict(list)
    for line in raw_data:
        key = line['year'], line['month'], line['category']
        dict_groups[key].append(line)
    print(*dict_groups.values(), sep='\n')
    return dict_groups.values()


def monthly_report(sorted_data):
    category_and_amount = []
    for sales in sorted_data:
        amount_by_category = 0
        for sale in sales:
            category = sale['category']
            if category not in category_and_amount:
                amount_by_category += int(sale['amount'])


        category_and_amount.append({category:amount_by_category})
    return category_and_amount
data = read_data("sales_data.txt")
proc_data = process_data(data)
m_r = monthly_report(proc_data)
print(m_r)
#print(*data, sep='\n')