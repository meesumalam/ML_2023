


with open('waseemDataset.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in input_file:
            # Replace all occurrences of space with a tab
            line = line.replace(' ', '\t')
            output_file.write(line)
