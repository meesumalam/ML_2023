
import pandas as pd 


from sklearn.model_selection import train_test_split

# Load your data into the X and y variables
# X should be a 2D array with your feature values
# y should be a 1D array with your target values

# Split the data into train and test sets (80/20 split)
df = pd.read_csv('WaseemDataWithLabels2.txt', sep='\t') #add waseemdataset here
X = df['text']
y = df['label']
#print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Split the remaining 80% of the data into train and dev sets (50/50 split)
X_test, X_dev, y_test, y_dev = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

# Print the shape of each set to verify the split
print("Train set shape:", X_train.shape)
print("Dev set shape:", X_dev.shape)
print("Test set shape:", X_test.shape)

train = pd.DataFrame(
    {'text': X_train,
     'label': y_train}
)

dev = pd.DataFrame(
    {'text': X_dev,
     'label': y_dev}
)

test = pd.DataFrame(
    {'text': X_test,
     'label': y_test}
)

train.to_csv('train.txt', sep='\t', index=False)
test.to_csv('test.txt', sep='\t', index=False)
dev.to_csv('dev.txt', sep='\t', index=False)


