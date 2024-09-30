import faker
import pandas as pd
from pandas import DataFrame
from sdv.single_table import GaussianCopulaSynthesizer, CopulaGANSynthesizer, TVAESynthesizer
from sdv.metadata.single_table import SingleTableMetadata

# Define the schema for each table
orderMetaDataFrame = pd.DataFrame({
    'orderID': [1], 'orderDate': ["2024-01-01"], 'productCode': [9691], 'products': ["Manearth-Onion-Growth-Control-Redensyl"],
    'customerID': [1], 'customerName': ["John Doe"], 'orderValue': [99]
})

# Define metadata for the Customers table
order_metadata = SingleTableMetadata()
order_metadata.detect_from_dataframe(orderMetaDataFrame)
# product_metadata.save_to_json('product_metadata.json')

# Sample real data for Customers (replace with actual data)
# customer = pd.DataFrame({
#     'customerID': [1, 2, 3, 4, 5],
#     'customerName': ["John Doe", "Jane Doe", "Alice", "Bob", "Charlie"]
# })
#
# product = pd.DataFrame({
#     'productCode': [9691, 9091, 8156, 9036, 5762],
#     'productName': ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"],
#     'productLine': ["ProductLine1", "ProductLine2", "ProductLine3", "ProductLine4", "ProductLine5"],
#     'productVendor': ["Vendor 1", "Vendor 2", "Vendor 3", "Vendor 4", "Vendor 5"],
#     'productDescription': ["Description for Product 1", "Description for Product 2", "Description for Product 3",
#                            "Description for Product 4", "Description for Product 5"],
#     'quantityInStock': [100, 200, 300, 400, 500]
# })

order = pd.DataFrame({
    'orderID': [1, 2, 3, 4, 5],
    'orderDate': ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    'productCode': [9691, 9091, 8156, 9036, 5762],
    'products': ["Manearth-Onion-Growth-Control-Redensyl", "Manearth-Percent-Natural-Berry-Toothpaste","Manearth-Natural-Turmeric-Saffron-brightning",
                 "Godrej-Protek-Master-Blaster-Handwash", "Godrej-No-1-Bathing-Soap-Lime"],
    'customerID': [1, 2, 3, 4, 5],
    'customerName': ["John Doe", "Jane Doe", "Alice", "Bob", "Charlie"],
    'orderValue': [99,110,66,89,43]
})

# Concat all the dataframes
real_data: DataFrame = order


# Function to generate synthetic data using GaussianCopula
def generate_synthetic_data(real_data, metadata, num_samples):
    synthesizer = GaussianCopulaSynthesizer(metadata)
    # synthesizer = CopulaGANSynthesizer(metadata, cuda=True)
    # synthesizer = TVAESynthesizer(metadata, cuda=True)
    synthesizer.fit(real_data)
    synthetic_data = synthesizer.sample(num_samples)
    return synthetic_data


if __name__ == '__main__':
    # Generate synthetic data
    num_samples = 50
    synthetic_order_data = generate_synthetic_data(real_data, order_metadata, num_samples)

    for index, row in synthetic_order_data.iterrows():
        synthetic_order_data.at[index, 'orderID'] = faker.Faker().unique.random_int(min=1000, max=9999)

    synthetic_order_data.to_csv(path_or_buf="../../data_dir/using_copula/synthesized_order.csv", index=False)
    print(synthetic_order_data.head())
