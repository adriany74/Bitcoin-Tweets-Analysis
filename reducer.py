#!/usr/bin/env python3
import sys

# Initialize an empty dictionary to store word counts
word_counts = {}

# Input comes from standard input (stdin)
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if word in word_counts:
        word_counts[word] += count
    else:
        word_counts[word] = count

for word, count in word_counts.items():
    print(f"{word}\t{count}")
