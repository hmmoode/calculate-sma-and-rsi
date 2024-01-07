def calculate_sma(data, window=5): # Function to calculate Simple Moving Average (SMA) from historical data
    sma = []  # Initialize an empty list to store SMA values
    for i in range(len(data)): # Iterate through the historical data
        if i < window:
            sma.append(None) # Add None for indexes where there is not enough data for SMA calculation
        else:
            sum_close = sum(float(row['Close']) for row in data[i - window:i])  # Calculate sum of 'Close' values
            sma.append(sum_close / window)  # Calculate SMA and append to the list
    return sma # Return the list containing SMA values
