import pandas as pd
import matplotlib.pyplot as plt
import re

import pandas as pd
import io  # Import io module for StringIO

# Load the data from CSV
data = """Name,Age,Email,Phone,Address
John Doe,35,johndoe@example.com,555-1234,123 Main St
Jane Smith,28,janesmith@example.com,555-5678,456 Elm St
Michael Johnson,42,michaeljohnson@example.com,555-9012,789 Oak St
Emily Brown,31,emilybrown@example.com,555-3456,101 Pine St
David Wilson,39,davidwilson@example.com,555-7890,202 Maple St"""

# Create a DataFrame
df = pd.read_csv(io.StringIO(data))  # Use io.StringIO instead of pd.compat.StringIO

# Rest of the code remains the same...


# Summary Statistics
mean_age = df['Age'].mean()
median_age = df['Age'].median()
min_age = df['Age'].min()
max_age = df['Age'].max()
num_individuals = len(df)

print("Summary Statistics:")
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")
print(f"Number of Individuals: {num_individuals}")

# Age Distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Email Domain Analysis
df['Email Domain'] = df['Email'].apply(lambda x: re.search("@([\w.]+)", x).group(1))
email_domain_counts = df['Email Domain'].value_counts()
print("\nEmail Domain Analysis:")
print(email_domain_counts)

# Phone Number Format Analysis
phone_number_formats = df['Phone'].apply(lambda x: re.match(r'^\d{3}-\d{4}$', x) is not None)
if all(phone_number_formats):
    print("\nAll phone numbers have the correct format (###-####).")
else:
    print("\nSome phone numbers have incorrect format.")

# Address Analysis
address_counts = df['Address'].value_counts()
print("\nAddress Analysis:")
print(address_counts)

# Name Analysis
first_names = df['Name'].apply(lambda x: x.split()[0])
last_names = df['Name'].apply(lambda x: x.split()[-1])
first_name_counts = first_names.value_counts()
last_name_counts = last_names.value_counts()
print("\nFirst Name Analysis:")
print(first_name_counts)
print("\nLast Name Analysis:")
print(last_name_counts)

# Data Quality Checks
missing_values = df.isnull().sum().sum()
if missing_values == 0:
    print("\nNo missing values found in the dataset.")
else:
    print(f"\nFound {missing_values} missing values in the dataset.")

# Customer Segmentation (N/A with current data)

# Geospatial Analysis (N/A with current data)
