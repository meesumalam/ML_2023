import pandas as pd

# Load train, dev, and test data into dataframes
train_data = pd.read_csv('train_data.csv')
dev_data = pd.read_csv('dev_data.csv')
test_data = pd.read_csv('test_data.csv')

# Load hate speech lexicon into a set
lexicon = set()
with open('hate_speech_lexicon.txt', 'r') as f:
    for line in f:
        lexicon.add(line.strip())

# Create feature vectors for train data
train_feature_vectors = []
for tweet in train_data['text']:
    # Initialize feature vector with all zeroes
    feature_vector = [0] * len(lexicon)
    # Set value to 1 if word is in tweet
    for i, word in enumerate(lexicon):
        if word in tweet:
            feature_vector[i] = 1
    train_feature_vectors.append(feature_vector)

# Create feature vectors for dev data
dev_feature_vectors = []
for tweet in dev_data['text']:
    # Initialize feature vector with all zeroes
    feature_vector = [0] * len(lexicon)
    # Set value to 1 if word is in tweet
    for i, word in enumerate(lexicon):
        if word in tweet:
            feature_vector[i] = 1
    dev_feature_vectors.append(feature_vector)

# Create feature vectors for test data
test_feature_vectors = []
for tweet in test_data['text']:
    # Initialize feature vector with all zeroes
    feature_vector = [0] * len(lexicon)
    # Set value to 1 if word is in tweet
    for i, word in enumerate(lexicon):
        if word in tweet:
            feature_vector[i] = 1
    test_feature_vectors.append(feature_vector)
