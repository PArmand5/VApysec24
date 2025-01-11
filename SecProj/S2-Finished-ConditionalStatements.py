import pandas as pd
#SameRequirements as S1l; bop
# Get the CSV file
## Change location
csv_file = r"C:\Users\ArmandsPriede\OneDrive - Vidzemes Augstskola\Pitons\Data\signin_logs2.csv"
signin_logs_df = pd.read_csv(csv_file)

# Define substrings to match for each key field (Dictionary). Links file information to code
field_mapping = {
    "User": "User",
    "UserName": "Username",
    "IPAddress": "IP",
    "Location": "Location",
    "ClientApp": "Client app",
    "MFAResult": "Multifactor authentication result",
    "Browser": "Browser",
    "Resource": "Resource"
}

# Find the matching column names (using List and Dictionary). Links required data
matched_columns = {}
for key, substring in field_mapping.items():
    matched_columns[key] = next((col for col in signin_logs_df.columns if substring in col), None)

# Remove any None values in case a column was not matched as its not needed for this apat of assignment, should increase execusion for large data sets
matched_columns = {k: v for k, v in matched_columns.items() if v is not None}

# Extract relevant columns
filtered_logs = signin_logs_df[list(matched_columns.values())]

# Initialize results list for displaying correlations
correlations = []

# Use while loop to iterate through filtered logs (while loop)
i = 0
while i < len(filtered_logs):
    row = filtered_logs.iloc[i]
    
    # Check correlation condition: Resource is "Microsoft Graph" and Client app is "Browser". Typical attacers method to get data from Microsoft365 environment
    if "Microsoft Graph" in row[matched_columns["Resource"]] and "Browser" in row[matched_columns["ClientApp"]]:
        # Capture relevant information: Browser version and MFA result - IF MFA accepted user might be compromised
        correlation_info = {
            "Browser Version": row[matched_columns["Browser"]],
            "MFA Result": row[matched_columns["MFAResult"]],
            "User": row[matched_columns["User"]]
        }
        correlations.append(correlation_info)
    
    i += 1

# Use for loop to display the correlations (For Loop)
print("\nCorrelations Found (Microsoft Graph accessed from Browser):")
for correlation in correlations:
    print(f"User: {correlation['User']}, Browser Version: {correlation['Browser Version']}, MFA Result: {correlation['MFA Result']}")

# Example of using a range loop for counting total correlations (Range Loop)
total_correlations = 0
for _ in range(len(correlations)):
    total_correlations += 1

print(f"\nTotal Correlations Found: {total_correlations}")

 #End of assignment task, future development in next files
