#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: 6 or more hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

documentsNoStop = []
dummylist = []
for documents in documents:
  words = documents.split() 
  for word in words:
    if word not in stopWords:
      dummylist.append(word)
      
documentsNoStop.append(dummylist)

print("This the result from removing stop words:")
print(dummylist)
print()
#this is for checking
#print(documentsNoStop)


#Conduct stemming.
#--> add your Python code here
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}

for stemwords in documentsNoStop:
  for i, word in enumerate(stemwords):
    if word in stemming:
      stemwords[i] = stemming[word]
 
 
print("This is the result from stemming words:")
print(stemwords)
print()
#****this is for checking
#for x in stemwords:
  #print(x)
  
#Identify the index terms.
#--> add your Python code here
terms = []

for stemwords in documentsNoStop:
  for word in stemwords:
    if word not in terms:
      terms.append(word)

print("This is the result of indentifying index terms:")
print(terms)
print()

#****for checking
#print(terms)


#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []



#term count




print(docMatrix)

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []



#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here