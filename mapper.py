#!/usr/bin/env python3
import sys
import re
import csv

# Function to clean tweet text
def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove non-alphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    return text

# Input comes from standard input (stdin)
input_stream = sys.stdin.read()
reader = csv.reader(input_stream.splitlines())

header_skipped = False
for row in reader:
    if not header_skipped:
        header_skipped = True
        continue
    
    #Text (last row)
    if len(row) >= 8:
        tweet_text = row[-1]

        # Clean the tweet text
        cleaned_text = clean_text(tweet_text)
        words = cleaned_text.split()

        # Emit (word, 1) pairs
        for word in words:
            if word:
                print(f"{word}\t1")
