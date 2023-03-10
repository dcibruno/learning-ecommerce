from faker import Faker
import pandas as pd
import random
import csv
from datetime import datetime
from dateutil.parser import parse

fake = Faker('pt_BR')

key_check = []

id = []
order_id = []
customer_id = []
product_id = []
created_at = []
pre_tax_price = []
price = []
quantity = []
fulfillment_status = []
location_id = []

# Open, read, and create lists using data from CSVs

csv_product_ids = []
csv_product_prices = []
with open("../csvs/products.csv") as products_csv:
    csv_reader = csv.reader(products_csv)
    next(csv_reader)
    for row in csv_reader:
        csv_product_ids.append(int(row[0]))
        csv_product_prices.append(float(row[5]))

csv_customer_ids = []
csv_customer_creation_dates = []
with open("../csvs/customers.csv") as customers_csv:
    csv_reader = csv.reader(customers_csv)
    next(csv_reader)
    for row in csv_reader:
        csv_customer_ids.append(int(row[0]))
        csv_customer_creation_dates.append(parse(row[1]))

csv_locations_ids = []
csv_locations_taxes = []
with open("../csvs/locations.csv") as locations_csv:
    csv_reader = csv.reader(locations_csv)
    next(csv_reader)
    for row in csv_reader:
        csv_locations_ids.append(int(row[0]))
        csv_locations_taxes.append(float(row[3]))

# Generate order_items data points

ind = 0
for row in range(10000):

    # id (order_item_id)
    
    id.append(row)

    # fulfillment_status

    if (ind % 2 == 0 or ind % 3 == 0 or ind % 5 == 0):
        fulfillment_status.append('fulfilled')
    else:
        fulfillment_status.append('restocked')

    # product_id and price
    
    product_random_index = random.randint(0,len(csv_product_ids)-1)
    product_id.append(csv_product_ids[product_random_index])
    price.append(csv_product_prices[product_random_index])

    # quantity

    quantity.append(random.randint(1, 4))

    # order_id

    if len(order_id) == 0:
        order_id.append(ind)
    else:
        if (str(ind) + str(product_id[-1])) in key_check:
            ind = ind + 1
            order_id.append(ind)
        else:
            ind = ind + random.randint(0, 1)
            order_id.append(ind)
    
    # customer_id, created_at, and location_id

    customer_random_index = random.randint(0,len(csv_customer_ids)-1)
    location_random_index = random.randint(0,len(csv_locations_ids)-1)
    if (len(order_id) == 1 and ind == 0):
        customer_id.append(csv_customer_ids[customer_random_index])
        created_at.append((fake.date_time_between_dates(csv_customer_creation_dates[customer_random_index], 'now')))
        location_id.append(csv_locations_ids[location_random_index])
    elif order_id[-2] == order_id[-1]:
        customer_id.append(customer_id[-1])
        created_at.append(created_at[-1])
        location_id.append(location_id[-1])
    else:
        customer_id.append(csv_customer_ids[customer_random_index])
        created_at.append((fake.date_time_between_dates(csv_customer_creation_dates[customer_random_index], 'now')))
        location_id.append(csv_locations_ids[location_random_index])
    
    # pre_tax_price
    
    pre_tax_price.append(round((price[row] - csv_locations_taxes[location_random_index] * price[row]), 2))

    # Key Check!

    key_check.append(str(ind) + str(product_id[-1]))

customer = {
    'id': id,
    'order_id': order_id,
    'customer_id': customer_id,
    'product_id': product_id,
    'created_at': created_at,
    'pre_tax_price': pre_tax_price,
    'price': price,
    'quantity': quantity,
    'fulfillment_status': fulfillment_status,
    'location_id': location_id
}

df = pd.DataFrame(customer, columns = ['id', 'order_id', 'customer_id', 'product_id', 'created_at', 'pre_tax_price', 'price', 'quantity', 'fulfillment_status', 'location_id'])
path = '../csvs/order_items.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)