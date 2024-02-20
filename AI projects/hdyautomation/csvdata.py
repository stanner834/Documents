import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame, specifying the separator as ','
df = pd.read_csv('newdata.csv', sep=',')

# Split the 'Name,Age,Email,Phone,Address' column into separate columns
df = df['Name,Age,Email,Phone,Address'].str.split(',', expand=True)
df.columns = ['Name', 'Age', 'Email', 'Phone', 'Address']

# Display the DataFrame
print("Original data:")
print(df)
print()

# Perform some basic data analysis
print("Data analysis:")
print("Number of rows:", len(df))
print("Summary statistics for numerical columns:")
print(df.describe())
print()

# Analyze categorical columns
print("Unique values in categorical columns:")
for column in df.select_dtypes(include=['object']):
    print(column + ":", df[column].unique())

# Visualize age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'].astype(int), bins=10, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)

# Visualize count of each categorical variable
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=column, palette='Set2')
    plt.title(f'Count of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True)

# Show all plots together
plt.show()
