import pandas as pd
from faker import Faker
import random

fake = Faker()
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        customers.append({
            'customerNumber': fake.unique.random_int(min=1000, max=9999),
            'customerName': fake.company(),
            'contactLastName': fake.last_name(),
            'contactFirstName': fake.first_name(),
            'phone': fake.phone_number(),
            'addressLine1': fake.street_address(),
            'addressLine2': fake.secondary_address(),
            'city': fake.city(),
            'state': fake.state(),
            'postalCode': fake.zipcode(),
            'country': fake.country(),
            'salesRepEmployeeNumber': fake.random_int(min=1000, max=9999),
            'creditLimit': round(random.uniform(1000, 10000), 2),
            'LTV': round(random.uniform(1000, 10000), 2)
        })
    return pd.DataFrame(customers)

if __name__ == '__main__':
    num_records = 100
    customers = generate_customers(num_records)
    customers.to_csv(path_or_buf="../data_dir/using_faker/customers.csv", index=False)
    print(customers.head())