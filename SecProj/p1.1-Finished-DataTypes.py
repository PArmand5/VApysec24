import pandas as pd

# Get the CSV file
## Change location
csv_file = r"C:\Users\ArmandsPriede\OneDrive - Vidzemes Augstskola\Pitons\Data\signin_logs.csv"

# Load the CSV file into a DataFrame
signin_logs_df = pd.read_csv(csv_file)

# Define substrings to match for each key field (Dictionary). Links file information to code
field_mapping = {
    "User": "User",
    "UserName": "Username",
    "IPAddress": "IP",
    "Location": "Location"
}

# Find the matching column names (using List and Dictionary). Links required data
matched_columns = {}
for key, substring in field_mapping.items():
    matched_columns[key] = next((col for col in signin_logs_df.columns if substring in col and "User agent" not in col and "User ID" not in col), None)

# Remove any None values in case a column was not matched as its not needed for this apat of assignment, but will be used in futher development of solution.
matched_columns = {k: v for k, v in matched_columns.items() if v is not None}

# Extract the matched columns into a filtered DataFrame (List). Filtering.
filtered_logs = signin_logs_df[list(matched_columns.values())]

# Display first 5 rows (Tuple use example).Checking if code works with shor data display
for row in filtered_logs.itertuples(index=False, name='SignInLog'):
    print(row)

# Create a set of unique locations from the filtered logs (Set). Might be used for analysis, as example unknow location for company.
unique_locations = set(filtered_logs[matched_columns["Location"]])
print("\nUnique Locations:")
print(unique_locations)

# Count occurrences of each user in the logs (Dictionary for counting). Indicates user actions, helps to understand if thre is something suspicious
user_counts = {}
for user in filtered_logs[matched_columns["User"]]:
    user_counts[user] = user_counts.get(user, 0) + 1
#Dispay of inrmation indicated previously
print("\nUser Sign-In Counts:")
for user, count in user_counts.items():
    print(f"{user}: {count}")
