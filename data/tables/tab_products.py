from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

id = []
title = []
product_type = []
status = []

for row in range(0, 1000+1):
    
    id.append(row)
    
    title.append(fake.word(ext_word_list=['Camiseta - M','Camiseta - F','Croped - F','Camisa - M', 'Camisa - F', # Camisetas
                                          'Slim - M','Skinny - F','Flared - F','Wide Leg - F', # Jeans
                                          'Bermuda - M','Bermuda - F','Shorts - F' # Bermudas
                                         ]))

product = {
    'id': id,
    'title': title,
    'product_type': product_type,
    'status': status
}

df = pd.DataFrame(product, columns = ['id', 'title', 'product_type', 'status'])
path = '../csvs/customers.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)