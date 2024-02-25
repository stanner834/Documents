import pandas as pd

import pandas as pd

import pandas as pd

# Read data from CSV file into a DataFrame
df = pd.read_csv("clean_data.csv")

# Print the DataFrame to check its structure and contents
print("DataFrame:")
print(df)

# Summary statistics for all columns
summary_all_columns = df.describe()

# Print summary statistics for all columns
print("\nSummary Statistics for all columns:")
print(summary_all_columns)


