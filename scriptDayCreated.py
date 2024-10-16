import pandas as pd

# Load the CSV file (replace 'path_to_your_csv_file.csv' with the actual file path)
file_path = '/Users/noud/Downloads/PythonWinCoIncidentClosureDataOnly2019WITHactualTIME.csv'
data = pd.read_csv(file_path)

# Convert 'Created' column to datetime format
data['Created'] = pd.to_datetime(data['Created'])

# Add 'Day of Week' column
data['Day of Week'] = data['Created'].dt.day_name()

# Save the updated dataset to a new CSV file
updated_file_path = 'updated_WinCo_Incident_Data_with_Day_of_Week.csv'
data.to_csv(updated_file_path, index=False)

print(f"Updated file saved as: {updated_file_path}")
