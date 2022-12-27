from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

# Reference: chewy.com

pet_shop_list = [
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Power Chew Double Bone",
        "detail":"XL - $30.69",
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"CoreStrength Rattlez Ball",
        "detail":"L - $9.99",
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Bacon Flavor Wishbone Tough",
        "detail":"M - $8.99",
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Extreme Tires",
        "detail":"L - $15.99",
    },
    {
        "category":"Dog",
        "subcategory":"Toy",
        "title":"Lobster",
        "detail":"M - $10.59",
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Peanut Butter Oven Baked",
        "detail":"M - $4.07",
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Crunchy with Real Mixed Berries",
        "detail":"S - $8.98",
    },
    {
        "category":"Dog",
        "subcategory":"Treats",
        "title":"Classic Chicken",
        "detail":"S - $6.37",
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Colorful Springs",
        "detail":"10 Count - $4.75",
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Basic Plush Mice",
        "detail":"5 Count - $4.64",
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Guacamole Bowl",
        "detail":"4 Count - $5.64",
    },
    {
        "category":"Cat",
        "subcategory":"Toy",
        "title":"Kitty Crinkle Balls Indoor",
        "detail":"12 Count - $6.33",
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"Party Mix Beachside Crunch Flavor",
        "detail":"20-oz - $10.29",
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"Irresistibles Soft Salmon",
        "detail":"3-oz - $1.49",
    },
    {
        "category":"Cat",
        "subcategory":"Treat",
        "title":"MixUps Catnip Fever Flavor",
        "detail":"16-oz - $8.49",
    }
]

id = []
title = []
category = []
subcategory = []
detail = []

ind = 0
for item in pet_shop_list:

    id.append(ind)
    ind += 1

    title.append(item['title'])

    category.append(item['category'])

    subcategory.append(item['subcategory'])

    detail.append(item['detail'])

product = {
    'id': id,
    'title': title,
    'category': category,
    'subcategory': subcategory,
    'detail': detail,
}

df = pd.DataFrame(product, columns = ['id', 'title', 'category', 'subcategory', 'detail'])
path = '../csvs/products.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)