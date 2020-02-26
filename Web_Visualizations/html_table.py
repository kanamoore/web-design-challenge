import pandas as pd

# Read the csv file
df = pd.read_csv('..\Resources\cities.csv')

# Save to file
df.to_html('cities_table')

# Assign to string
htmlTable = df.to_html()

print(htmlTable)