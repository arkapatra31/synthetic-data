import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer, CopulaGANSynthesizer, TVAESynthesizer
from sdv.metadata.single_table import SingleTableMetadata

# Define the schema for each table
product_columns = pd.DataFrame({
    'productCode': [9691], 'productName': ["Mamaearth-Onion-Growth-Control-Redensyl"],
    'productLine': ["ProductLine2"], 'productScale': ["01:18"],
    'productVendor': ["Johnson, Garcia and Ferguson", ], 'productDescription': ["Description for Product 1"],
    'quantityInStock': [971], 'buyPrice': [554.12]
})

# Define metadata for the Customers table
product_metadata = SingleTableMetadata()
product_metadata.detect_from_dataframe(product_columns)
#product_metadata.save_to_json('product_metadata.json')

# Sample real data for Customers (replace with actual data)
real_product_data = pd.DataFrame({
    "productCode": [9691,
                    9091,
                    8156,
                    9036,
                    5762,
                    6930,
                    1687,
                    7489,
                    4745,
                    1027
                    ],
    "productName": ["Mamaearth-Onion-Growth-Control-Redensyl",
                    "Mamaearth-Percent-Natural-Berry-Toothpaste",
                    "Mamaearth-Natural-Turmeric-Saffron-brightning",
                    "Mamaearth-Illuminate-Vitamin-Radiant-Turmeric",
                    "Mamaearth-Blemishes-Pigmentation-Blemish-Mulberry",
                    "Mamaearth-Face-Wash-100-ml",
                    "Mamaearth-Moisturizing-Baby-Bathing-Oatmeal",
                    "Godrej-Protekt-Master-Blaster-Handwash",
                    "Godrej-No-1-Bathing-Soap-Lime",
                    "Godrej-No-1-Bathing-Soap-Turmeric"],
    "productLine": ["ProductLine2",
                    "ProductLine1",
                    "ProductLine2",
                    "ProductLine3",
                    "ProductLine4",
                    "ProductLine3",
                    "ProductLine3",
                    "ProductLine1",
                    "ProductLine2",
                    "ProductLine4"],
    "productScale": ["01:18",
                     "01:18",
                     "01:10",
                     "01:10",
                     "01:12",
                     "01:10",
                     "01:18",
                     "01:18",
                     "01:10",
                     "01:10"],
    "productVendor": ["Johnson, Garcia and Ferguson",
                      "Smith Group",
                      "Pennington and Sons",
                      "Marshall-Ross",
                      "George PLC",
                      "Chavez-Robinson",
                      "Whitehead, Horton and Johnson",
                      "Lang-Morris",
                      "Sanchez PLC",
                      "Anderson-Dunn"],
    "productDescription": ["Description for Product 1",
                           "Description for Product 2",
                           "Description for Product 3",
                           "Description for Product 4",
                           "Description for Product 5",
                           "Description for Product 6",
                           "Description for Product 7",
                           "Description for Product 8",
                           "Description for Product 9",
                           "Description for Product 10"],
    "quantityInStock": [971,
                        457,
                        730,
                        620,
                        383,
                        609,
                        190,
                        477,
                        358,
                        462
                        ],
    "buyPrice": [554.12,
                 462.07,
                 383.78,
                 919.4,
                 973.08,
                 581.44,
                 609.67,
                 924.64,
                 774.57,
                 829.3
                 ]
})


# Function to generate synthetic data using GaussianCopula
def generate_synthetic_data(real_data, metadata, num_samples):
    synthesizer = GaussianCopulaSynthesizer(metadata)
    #synthesizer = CopulaGANSynthesizer(metadata, cuda=True)
    #synthesizer = TVAESynthesizer(metadata, cuda=True)
    synthesizer.fit(real_data)
    synthetic_data = synthesizer.sample(num_samples)
    return synthetic_data


# Generate synthetic data
synthetic_product_data = generate_synthetic_data(real_product_data, product_metadata, 50)
synthetic_product_data.to_csv(path_or_buf="../data_dir/using_copula/gaussian/synthesized_products.csv", index=False)
print(synthetic_product_data.head())

