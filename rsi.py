def calculate_rsi(data, window=14): # Function to calculate Relative Strength Index (RSI) from historical data
    rsi = [] # Initialize an empty list to store RSI values
    for i in range(len(data)): # Iterate through the historical data
        if i < window:
            rsi.append(None) # Add None for indexes where there is not enough data for RSI calculation
        else:
            average_gain = 0 # Initialize average gain
            average_loss = 0 # Initialize average loss
            for j in range(i - (window - 1), i): # Calculate average gain and average loss within the window
                price_diff = float(data[j]['Close']) - float(data[j - 1]['Close'])
                if price_diff > 0:
                    average_gain += price_diff
                else:
                    average_loss -= price_diff

            average_gain /= window # Calculate average gain
            average_loss /= window # Calculate average loss

            if average_loss == 0:
                rsi.append(100) # Append 100 if average loss is zero to avoid division by zero
            else:
                rs = average_gain / average_loss  # Calculate RS (Relative Strength)
                rsi.append(100 - (100 / (1 + rs)))  # Calculate RSI and append to the list
    return rsi # Return the list containing RSI values
