import pandas as pd

# Get the CSV file
csv_file = r"C:\Users\ArmandsPriede\OneDrive - Vidzemes Augstskola\Pitons\Data\signin_logs.csv"

# Load the CSV file into a DataFrame
signin_logs_df = pd.read_csv(csv_file)

# Define substrings to match for each key field (Dictionary)
field_mapping = {
    "User": "User",
    "UserName": "Username",
    "IPAddress": "IP",
    "Location": "Location"
}

# Dynamically find the matching column names (using List and Dictionary)
matched_columns = {}
for key, substring in field_mapping.items():
    matched_columns[key] = next((col for col in signin_logs_df.columns if substring in col and "User agent" not in col and "User ID" not in col), None)

# Remove any None values in case a column was not matched
matched_columns = {k: v for k, v in matched_columns.items() if v is not None}

# Extract the matched columns into a filtered DataFrame (List)
filtered_logs = signin_logs_df[list(matched_columns.values())]

# Display first 5 rows (Tuple use example)
for row in filtered_logs.itertuples(index=False, name='SignInLog'):
    print(row)

# Create a set of unique locations from the filtered logs (Set)
unique_locations = set(filtered_logs[matched_columns["Location"]])
print("\nUnique Locations:")
print(unique_locations)

# Count occurrences of each user in the logs (Dictionary for counting)
user_counts = {}
for user in filtered_logs[matched_columns["User"]]:
    user_counts[user] = user_counts.get(user, 0) + 1

print("\nUser Sign-In Counts:")
for user, count in user_counts.items():
    print(f"{user}: {count}")
