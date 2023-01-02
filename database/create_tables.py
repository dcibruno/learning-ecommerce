import os

from dotenv import load_dotenv, find_dotenv
import psycopg2

load_dotenv(find_dotenv())                                                 
                                                                                
conn = psycopg2.connect(
    user=os.getenv("database_user"),
    password=os.getenv("database_password"),
    host=os.getenv("database_ip"),
    port=os.getenv("database_port"),
    dbname=os.getenv("database_name")
)

cur = conn.cursor()

cur.execute("""
    
    DROP TABLE IF EXISTS customers;
    
    CREATE TABLE customers (
    id int8 PRIMARY KEY,
    created_at timestamp,
    first_name varchar(25),
    last_name varchar(25),
    email varchar(25)
)
""")

with open('../data/csvs/customers.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'customers', sep=',')

cur.execute("""
    
    DROP TABLE IF EXISTS locations;
    
    CREATE TABLE locations (
    id int4 PRIMARY KEY,
    city varchar(25),
    state varchar(25),
    city_tax float4
)
""")

with open('../data/csvs/locations.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'locations', sep=',')

cur.execute("""
    
    DROP TABLE IF EXISTS products;
    
    CREATE TABLE products (
    id int4 PRIMARY KEY,
    title varchar(35),
    category varchar(3),
    subcategory varchar(6),
    size varchar(10),
    price float4
)
""")

with open('../data/csvs/products.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'products', sep=',')

cur.execute("""
    
    DROP TABLE IF EXISTS order_items;
    
    CREATE TABLE order_items (
    id int8 PRIMARY KEY,
    order_id int8,
    customer_id int8,
    product_id int4,
    created_at timestamp,
    pre_tax_price float4,
    price float4,
    quantity int4,
    fulfillment_status varchar(10),
    location_id int4
)
""")

with open('../data/csvs/order_items.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'order_items', sep=',')

conn.commit()
conn.close()