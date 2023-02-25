import random

# Set the random seed for reproducibility
random.seed(123)

# Read in your sorted data
with open("output.txt", "r") as f:
    data = f.readlines()

# Shuffle the data
random.shuffle(data)

# Calculate the sizes of each set
n = len(data)
train_size = int(0.8 * n)
dev_size = int(0.1 * n)

# Split the data into three sets
train_data = data[:train_size]
dev_data = data[train_size:train_size+dev_size]
test_data = data[train_size+dev_size:]

# Write the data to separate files
with open("train.txt", "w") as f:
    f.writelines(train_data)

with open("dev.txt", "w") as f:
    f.writelines(dev_data)

with open("test.txt", "w") as f:
    f.writelines(test_data)
