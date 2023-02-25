
import pandas as pd
import sklearn


from sklearn.model_selection import train_test_split

# Load your data into the X and y variables
# X should be a 2D array with your feature values
# y should be a 1D array with your target values

# Split the data into train and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Split the remaining 80% of the data into train and dev sets (50/50 split)
X_train, X_dev, y_train, y_dev = train_test_split(X_train, y_train, test_size=0.5, random_state=42)

# Print the shape of each set to verify the split
print("Train set shape:", X_train.shape)
print("Dev set shape:", X_dev.shape)
print("Test set shape:", X_test.shape)
