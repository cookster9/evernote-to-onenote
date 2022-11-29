#evernote_to_python.py
#get evernote notebooks
#for each notebook...
#get all notes
#load notes to spark RDD Dataset thing. (notebook, note)
    #load notes to Dataframe first, or write to file
    #create dataset from dataframe
    #or you can parallelize a list to make a dataset
#run transform to a valid POST request
#Make sections for each notebook
#Insert notes in correct reverse chronological order

from pyspark import SparkContext

sc = SparkContext()

l = []
for i in range(10):
    l.append(i)

print(l)
data_set = sc.parallelize(l)

print(data_set)