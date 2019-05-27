#!/usr/bin/env python

import pyspark
import sys

if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

input_uri=sys.argv[1]
output_uri=sys.argv[2]

sc = pyspark.SparkContext()
lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split())
sum_lambda = lambda count1, count2: count1 + count2
word_counts = words.map(lambda word: (word, 1)).reduceByKey(sum_lambda)
word_counts.saveAsTextFile(sys.argv[2])
