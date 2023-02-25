import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3

smoothed_data = pd.Series(data).rolling(window_size).mean().tolist()

print(smoothed_data)