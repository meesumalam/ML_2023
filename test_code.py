import pandas as pd

# Load the hate speech lexicon
with open('hate_lexicon_small.txt', 'r') as f:
    hate_speech_lexicon = set(f.read().splitlines())

# Load the dataset
f2data = pd.read_csv('WaseemDataSet.txt', sep='\t', header= None, names=['text']) #add waseemdataset here


# Define a function to create feature vectors
def create_feature_vectors(data):
    # Initialize an empty list to store the feature vectors
    feature_vectors = []

    # Loop over each tweet in the dataset
    for tweet in data['text']:
        # Initialize an empty list to store the feature values for this tweet
        feature_values = []

        # Loop over each word in the hate speech lexicon
        for word in hate_speech_lexicon:
            # Check if the word is in the tweet
            if word in tweet:
                # If the word is in the tweet, set the feature value to 1
                feature_values.append(1)
            else:
                # If the word is not in the tweet, set the feature value to 0
                feature_values.append(0)

        # Add the feature values for this tweet to the feature vectors list
        feature_vectors.append(feature_values)

    return feature_vectors

# Create feature vectors for each set
fdata_feature_vectors = create_feature_vectors(f2data)


# Write the feature vectors to separate files
with open('f2data_features.txt', 'w') as f:
    for feature_vector in fdata_feature_vectors:
        f.write(' '.join(map(str, feature_vector)) + '\n')


