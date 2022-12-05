#evernote_to_python.py
# https://sparkbyexamples.com/pyspark-tutorial/
#get evernote notebooks
#for each notebook...
#get all notes
#load notes to spark RDD Dataset thing. (notebook, note)
    #load notes to Dataframe first, or write to file
    #create dataset from dataframe
    #or you can parallelize a list to make a dataset
    #okay just kidding you don't really have to transform anything. So no reason to use spark
#run transform to a valid POST request
    #create a lambda function that takes the input (note text) and turns it into a valid post request that will make a note in onenote
#Make sections for each notebook
#Insert notes in correct reverse chronological order

from pyspark import SparkContext

sc = SparkContext()

l = []
for i in range(10):
    l.append(i)

print(l)
data_set = sc.parallelize(l)

print(data_set.count())
data_set2 = data_set.map(lambda x: x*2)
for element in (data_set2.collect()):
    print(element)