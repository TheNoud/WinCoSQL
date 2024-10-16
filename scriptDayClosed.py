import pandas as pd

# Load the CSV file
file_path = '/Users/noud/Downloads/PythonWinCoIncidentClosureDataOnly2019WITHactualTIME.csv'
data = pd.read_csv(file_path)

# Convert 'Closed at' column to datetime format
data['Closed at'] = pd.to_datetime(data['Closed at'])

# Add 'Day of Week Closed' column
data['Day of Week Closed'] = data['Closed at'].dt.day_name()

# Save the updated dataset to a new CSV file
updated_file_path = 'updated_WinCo_Incident_Data_with_Day_of_Week_Closed.csv'
data.to_csv(updated_file_path, index=False)

print(f"Updated file saved as: {updated_file_path}")
