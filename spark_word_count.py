from pyspark import SparkContext, SparkConf
import re

#Initialize Spark Context
conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

input_file = "hdfs:///user/hadoop/tweets.csv"  # Update this path if necessary
lines = sc.textFile(input_file)

#Function to split lines into words
def split_words(line):
    text = line.split(',')[-1]
    # Remove URLs and other unwanted characters
    text = re.sub(r"http\S+", "", text)
    # Split text into words
    return text.split()

#FlatMap to split each line into words
words = lines.flatMap(split_words)

#Map each word to a (word, 1) pair
word_pairs = words.map(lambda word: (word.lower(), 1))

#Reduce by key to count occurrences of each word
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

#Collect the results and sort by count in descending order
sorted_word_counts = word_counts.map(lambda x: (x[1], x[0])).sortByKey(False)

output_file = "hdfs:///user/hadoop/output2"  # Save to the specified output directory
sorted_word_counts.saveAsTextFile(output_file)

#Stop the Spark Context
sc.stop()
