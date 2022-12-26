from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

id = []
created_at = []
first_name = []
last_name = []
email = []

for row in range(0, 1000+1):
    
    id.append(row)
    
    created_at.append(fake.date_time_between_dates('-6y', 'now'))

    name = fake.name()
    first_name.append(name.split(" ")[0])
    last_name.append(name.split(" ")[1])

    email_address =  name.split(" ")[0][:2] + name.split(" ")[1][:2] + '@' + fake.free_email_domain()
    email.append(str(email_address).lower())

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