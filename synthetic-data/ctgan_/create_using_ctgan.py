import pandas as pd
from ctgan import CTGAN


# Define the schema for each table
customers_columns = [
    'customerNumber', 'customerName', 'contactLastName', 'contactFirstName', 'phone',
    'addressLine1', 'addressLine2', 'city', 'state', 'postalCode', 'country',
    'salesRepEmployeeNumber', 'creditLimit', 'LTV'
]

order_details_columns = [
    'orderNumber', 'productCode', 'quantityOrdered', 'priceEach', 'orderLineNumber'
]

orders_columns = [
    'orderNumber', 'orderDate', 'requiredDate', 'shippedDate', 'status', 'comments', 'customerNumber'
]

products_columns = [
    'productCode', 'productName', 'productLine', 'productScale', 'productVendor',
    'productDescription', 'quantityInStock', 'buyPrice'
]

product_lines_columns = [
    'productLine', 'textDescription', 'htmlDescription', 'imageURL'
]

# Function to generate synthetic data using CTGAN
def generate_synthetic_data(real_data, columns, num_samples):
    ctgan = CTGAN()
    ctgan.fit(real_data, columns)
    synthetic_data = ctgan.sample(num_samples)
    return synthetic_data

# Example real data (for demonstration purposes, replace with actual data)
real_customers_data = pd.DataFrame(columns=customers_columns)
real_order_details_data = pd.DataFrame(columns=order_details_columns)
real_orders_data = pd.DataFrame(columns=orders_columns)
real_products_data = pd.DataFrame(columns=products_columns)
real_product_lines_data = pd.DataFrame(columns=product_lines_columns)

# Generate synthetic data
synthetic_customers_data = generate_synthetic_data(real_customers_data, customers_columns, 10)
synthetic_order_details_data = generate_synthetic_data(real_order_details_data, order_details_columns, 10)
synthetic_orders_data = generate_synthetic_data(real_orders_data, orders_columns, 10)
synthetic_products_data = generate_synthetic_data(real_products_data, products_columns, 10)
synthetic_product_lines_data = generate_synthetic_data(real_product_lines_data, product_lines_columns, 10)

print(synthetic_customers_data.head())
print(synthetic_order_details_data.head())
print(synthetic_orders_data.head())
print(synthetic_products_data.head())
print(synthetic_product_lines_data.head())