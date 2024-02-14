import os
import pandas as pd
import numpy as np

# Determine the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the number of products and months
num_products = 5
num_months = 12

# Create a DataFrame with random sales data
products = [f'Product {i}' for i in range(1, num_products + 1)]
months = pd.date_range(start='2023-01-01', periods=num_months, freq='M')
sales_data = np.random.randint(1000, 5000, size=(num_months, num_products))
df = pd.DataFrame(sales_data, columns=products, index=months)

# Save the sales data to an Excel file
excel_file_output = 'random_sales_data.xlsx'
excel_file_path = os.path.join(script_dir, excel_file_output)
df.to_excel(excel_file_path)

print(f"Random sales data saved to {excel_file_path}")
