import pyspark
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc=SparkContext('local[2]',appName="MyStreamWordCount")
ssc=StreamingContext(sc,2)
lines = ssc.socketTextStream('localhost',9999)
counts = lines.flatMap(lambda line: line.split(" ")).filter(lambda word:len(word)>3).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint();
ssc.start()
ssc.awaitTermination()
