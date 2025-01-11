# main.py
from S3LogAnalyzerMain import LogAnalyzer
from S31_Whois import whois_lookup

## Change location
csv_file = r"C:\Users\ArmandsPriede\OneDrive - Vidzemes Augstskola\Pitons\Data\signin_logs2.csv"

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


#Creating instance of LogAnalyzer and launching it
analyzer = LogAnalyzer(csv_file=csv_file, field_mapping=field_mapping)

analyzer.load_csv()  #File
analyzer.match_columns()  #matching
correlations = analyzer.filter_correlations()  #Filtering
analyzer.display_results(correlations)  #Display

#Example of using a range loop for counting total correlations (Range Loop)
total_correlations = 0
for _ in range(len(correlations)): 
    total_correlations += 1

print("Total Correlations Found: {}".format(total_correlations))

# Error handling, source CHAT GPT!!!
while True:
    try:
        val = input("Please enter a number of entry to analyze | Get Whois Lookup: ")
        x = int(val)
        if 1 <= x <= len(correlations):
            selected_entry = correlations[x - 1]  # Get the selected log entry (0-based index)
            ip_address = selected_entry["IP Address"]
            whois_result = whois_lookup(ip_address)  # Perform WHOIS lookup
            print("\nWHOIS Lookup Result for Log Entry {}: {}".format(x, whois_result))
        else:
            print("Invalid entry number. Please enter a number between 1 and {}.".format(len(correlations)))
        break
    except ValueError:
        print("Oops! That was not a valid number! Try again...") #Example from lection presentations

#End of code