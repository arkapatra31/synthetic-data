import pandas as pd
from faker import Faker
import random

fake = Faker()
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        country_details = fetch_country_data()
        customers.append({
            'customerNumber': fake.unique.random_int(min=1000, max=9999),
            'customerName': fake.company(),
            'contactLastName': fake.last_name(),
            'contactFirstName': fake.first_name(),
            'phone': fake.phone_number(),
            'addressLine1': country_details.get('addressLine1'),#fake.street_address(),
            'addressLine2': country_details.get('addressLine2'),#fake.secondary_address(),
            'city': country_details.get('city'),#fake.city(),
            'state': country_details.get('state'),#fake.state(),
            'postalCode': country_details.get('postalCode'),#fake.zipcode(),
            'country': country_details.get('country'),#fake.country(),
            'salesRepEmployeeNumber': fake.random_int(min=1000, max=9999),
            'creditLimit': round(random.uniform(1000, 10000), 2),
            'LTV': round(random.uniform(1000, 10000), 2)
        })
    fetch_country_data()
    return pd.DataFrame(customers)

def fetch_country_data():
    country_details = pd.read_csv("./data-generation/country_data.csv", encoding='ISO-8859-1').sample(n=1)
    return country_details.to_dict(orient='records')[0]

if __name__ == '__main__':
    num_records = 1000
    customers = generate_customers(num_records)
    customers.drop_duplicates(subset=["customerNumber","phone", "addressLine1"], keep='first', inplace=True)
    customers.to_csv(path_or_buf="./customers.csv", index=False)
    print(customers.head())