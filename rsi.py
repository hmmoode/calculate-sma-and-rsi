def calculate_rsi(data, window=14):
    rsi = []
    for i in range(len(data)):
        if i < window:
            rsi.append(None)
        else:
            average_gain = 0
            average_loss = 0
            for j in range(i - (window - 1), i):
                price_diff = float(data[j]['Close']) - float(data[j - 1]['Close'])
                if price_diff > 0:
                    average_gain += price_diff
                else:
                    average_loss -= price_diff

            average_gain /= window
            average_loss /= window

            if average_loss == 0:
                rsi.append(100)
            else:
                rs = average_gain / average_loss
                rsi.append(100 - (100 / (1 + rs)))
    return rsi
