# S3LogAnalyzerMain.py
import pandas as pd

#Use of Class
class LogAnalyzer:
    def __init__(self, csv_file, field_mapping):  # Init method, gets the CSV file and field mapping
        self.csv_file = csv_file  
        self.field_mapping = field_mapping  #Matching columns
        self.matched_columns = {}  #Storing
        self.df = None  #

    def load_csv(self):
        """Load the CSV file into a DataFrame"""
        self.df = pd.read_csv(self.csv_file)

    def match_columns(self):
        """Find matching columns in the CSV based on field_mapping"""
        for key, substring in self.field_mapping.items():  #Loop
            self.matched_columns[key] = next((col for col in self.df.columns if substring in col), None)
        
        # Remove any None values in case a column was not matched as its not needed for this apat of assignment 
        # should increase execusion for large data sets
        self.matched_columns = {k: v for k, v in self.matched_columns.items() if v is not None}

    def filter_correlations(self):
        """Filter rows where Microsoft Graph was accessed via Browser"""
        correlations = []  # List to store results
        i = 0  # Indexig loop
        while i < len(self.df):  
            row = self.df.iloc[i]
            if "Microsoft Graph" in row[self.matched_columns["Resource"]] and "Browser" in row[self.matched_columns["ClientApp"]]:
                correlation_info = {
                    "User": row[self.matched_columns["User"]],
                    "Browser Version": row[self.matched_columns["Browser"]],
                    "MFA Result": row[self.matched_columns["MFAResult"]],
                    "IP Address": row[self.matched_columns["IPAddress"]]
                }
                correlations.append(correlation_info)
            i += 1  # Increment index, so counting works as suposed
        return correlations

    def display_results(self, correlations):
        """Display results"""
        print("\nCorrelations Found (Microsoft Graph accessed from Browser):")
        for correlation in correlations: 
            print("User: {}, Browser Version: {}, MFA Result: {}".format(correlation['User'], correlation['Browser Version'], correlation['MFA Result']))

# End of code