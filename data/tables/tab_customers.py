from faker import Faker
import pandas as pd
from unidecode import unidecode

fake = Faker('pt_BR')

prefixes = []

for _ in range(5):
    prefixes.append(fake.prefix())
    prefixes.append(fake.prefix_female())
    prefixes.append(fake.prefix_male())
    prefixes.append(fake.prefix_nonbinary())

id = []
created_at = []
first_name = []
last_name = []
email = []

for row in range(0, 10000+1):
    
    id.append(row)
    
    created_at.append(fake.date_time_between_dates('-6y', 'now'))

    name = fake.name().split(" ")
    
    if name[0] in prefixes:
        f_name = name[1]
        if len(name[2]) <= 3:
            l_name = str(name[2] + " " + name[3])
        else:
            l_name = name[2]
    else:
        f_name = name[0]
        if len(name[1]) <= 3:
            l_name = str(name[1] + " " + name[2])
        else:
            l_name = name[1]

    first_name.append(f_name)
    last_name.append(l_name)

    email_address =  f_name[:2] + l_name[:4] + '@' + fake.free_email_domain()
    email.append(unidecode(str(email_address)).lower())

customer = {
    'id': id,
    'created_at': created_at,
    'first_name': first_name,
    'last_name': last_name,
    'email': email
}

df = pd.DataFrame(customer, columns = ['id', 'created_at', 'first_name', 'last_name', 'email'])
path = '../csvs/customers.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)