## Intro

Rules definitions for the data generation process!

## Schema

### ecommerce.order_items

1. Generate the `id` and the `fulfillment_status` (on the ID level).
2. Append random IDs from the csv_product_ids products list to the `product_id` list and the related `price` to the price list.
3. `quantity` is a random integer between 1 and 4.
4. The `order_id` depends on the product ID. If the latest value on the `product_id` list is the same as the list's past value, the script changes the value for the order ID.
5. For the same order, the same `customer_id`, `location_id`, and `created_at`. The latter must be greater than the customer creation date.
7. The `pre_tax_price` must be less than the `price`; the percentage depends on the location (city) of the order.

### ecommerce.products

1. Use a prebuilt `pet_shop_list` dictionary containing category, subcategory, title, size, and price for an item.
2. Dog subcategories are Toy and Treats, while Cat subcategories are Toy and Treat (w/o the 's'). That's intentional so that analysts can work on data cleaning.

### ecommerce.customers

1. Rely on Faker's [person](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html) and [date_time](https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html#faker.providers.date_time.Provider.date_time_between) providers to generate names (w/o prefixes), emails, and customer creation date times.

### public.locations

1. Generate latitude and longitude coordinates using the [local_latlng](http://fake.local_latlng) faker provider.
2. Get the raw address, city, and state from each coordinate using [geopy](https://pypi.org/project/geopy/).

### ecommerce.order_item_refunds

1. Not a priority.

### support.tickets

1. Not a priority.