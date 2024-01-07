def calculate_sma(data, window=5):
    sma = []
    for i in range(len(data)):
        if i < window:
            sma.append(None)
        else:
            sum_close = sum(float(row['Close']) for row in data[i - window:i])
            sma.append(sum_close / window)
    return sma