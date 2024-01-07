from sma import calculate_sma
from rsi import calculate_rsi

def load_historical_data(file_name):
    historical_data = []
    with open(file_name, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            row = {header[i]: values[i] for i in range(len(header))}
            historical_data.append(row)
    return historical_data

def write_to_csv(file_name, header, values):
    with open(file_name, 'w') as file:
        file.write(f"{header}\n")
        for value in values:
            if value is not None:
                file.write(f"{value}\n")
            else:
                file.write("\n")

# Load historical data
historical_data = load_historical_data('orcl.csv')

# Calculate SMA and RSI
sma_values = calculate_sma(historical_data)
rsi_values = calculate_rsi(historical_data)

# Write indicators to distinct CSV files
write_to_csv('orcl-sma.csv', 'SMA', sma_values)
write_to_csv('orcl-rsi.csv', 'RSI', rsi_values)