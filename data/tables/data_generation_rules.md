## Intro

Here's how we'll define the data creation process.
We're probably using the Faker python package to generate data and populate the tables.
Below is some guidance on what we need to do.

## Schema

### ecommerce.order_lines

1. The product, customer, and location IDs must always match in the ID columns of the products, customers, and locations tables, respectively.
2. The value in the `pre_tax_price` field must be less than the `price` field. The fee percentage will depend on the location (state) of the order.

### ecommerce.products

1. Propositalmente, Treats (Dog) e Treat para gato (sem o 's'), para tratamento.
2. Tamanho e preço juntos em details para a pessoa poder tratar.

### ecommerce.customers

### ecommerce.order_item_refunds

1. The distinct count of order_item_ids must be less than the count of values in the order_items table.

### public.locations

### support.tickets

1. Not every ticket needs to be related to an order or item. When it happens (a.k.a. `order_id` or `order_item_id` fields not null), they must find a relationship in the corresponding columns of the order_items table.