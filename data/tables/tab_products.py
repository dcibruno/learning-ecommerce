from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

# Reference: chewy.com

pet_shop_list = [
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Power Chew Double Bone",
        "size":"XL",
        "price":"30.69"
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"CoreStrength Rattlez Ball",
        "size":"L",
        "price":"9.99"
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Bacon Flavor Wishbone Tough",
        "size":"M",
        "price":"8.99"
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Extreme Tires",
        "size":"L",
        "price":"15.99"
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Lobster",
        "size":"M",
        "price":"10.59"
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Peanut Butter Oven Baked",
        "size":"M",
        "price":"4.07"
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Crunchy with Real Mixed Berries",
        "size":"S",
        "price":"8.98"
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Classic Chicken",
        "size":"S",
        "price":"6.37"
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Colorful Springs",
        "size":"10 Count",
        "price":"4.75"
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Basic Plush Mice",
        "size":"5 Count",
        "price":"4.64"
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Guacamole Bowl",
        "size":"4 Count",
        "price":"5.64"
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Kitty Crinkle Balls Indoor",
        "size":"12 Count",
        "price":"6.33"
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"Party Mix Beachside Crunch Flavor",
        "size":"20-oz",
        "price":"10.29"
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"Irresistibles Soft Salmon",
        "size":"3-oz",
        "price":"1.49"
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"MixUps Catnip Fever Flavor",
        "size":"16-oz",
        "price":"8.49"
    }
]

id = []
title = []
category = []
subcategory = []
size = []
price = []

ind = 0
for item in pet_shop_list:

    id.append(ind)
    ind += 1

    title.append(item['title'])

    category.append(item['category'])

    subcategory.append(item['subcategory'])

    size.append(item['size'])
    
    price.append(item['price'])

product = {
    'id': id,
    'title': title,
    'category': category,
    'subcategory': subcategory,
    'size': size,
    'price': price
}

df = pd.DataFrame(product, columns = ['id', 'title', 'category', 'subcategory', 'size', 'price'])
path = '../csvs/products.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)