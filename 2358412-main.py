from sma import calculate_sma
from rsi import calculate_rsi

# Function to load historical data from a CSV file into a list of dictionaries
def load_historical_data(file_name):
    historical_data = [] # Initialize an empty list to store the historical data
    with open(file_name, 'r') as file:
        header = file.readline().strip().split(',') # Read the header row and split it by commas
        for line in file: # Iterate through each line in the file
            values = line.strip().split(',') # Split the line by commas to get individual values
            row = {header[i]: values[i] for i in range(len(header))} # Create a dictionary for each row
            historical_data.append(row)  # Append the row dictionary to the list
    return historical_data # Return the list containing historical data dictionaries
    
# Function to write data to a CSV file
def write_to_csv(file_name, header, values):
    with open(file_name, 'w') as file:
        file.write(f"{header}\n") # Write the header to the CSV file
        for value in values:  # Iterate through the values
            if value is not None:
                file.write(f"{value}\n")  # Write the value to the file if it's not None
            else:
                file.write("\n")  # Write a blank line if the value is None

# Load historical data
historical_data = load_historical_data('orcl.csv')

# Calculate SMA and RSI
sma_values = calculate_sma(historical_data)
rsi_values = calculate_rsi(historical_data)

# Write indicators to distinct CSV files
write_to_csv('orcl-sma.csv', 'SMA', sma_values)
write_to_csv('orcl-rsi.csv', 'RSI', rsi_values)
