#-------------------------------------------------------------------------
# AUTHOR: Estefania Chavez
# FILENAME: Search_engine.py
# SPECIFICATION: Assignement based on the problem 7 which is index term weights and their importance rankings for web search
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

w1, w2, w3, w4, w5, w6, w7, w8 = map(list, zip(dummylist, range(len(dummylist))))

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

docu = []

#couldnt finish coding my though process, i was trying to not hard code, but my brain could not think
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            docu.append (row[0])
            #labels.append(row[1])

d1, d2, d3 = map(list, zip(docu, range(len(docu))))

c=0
c2=0
c3=0
d1counta = 0
d1countb = 0
d1countc = 0
d2counta = 0
d2countb = 0
d2countc = 0 
d3counta = 0
d3countb = 0 
d3countc = 0

for documentNoStop in documentsNoStop:
  for word in d1:
    if word in d1:
      if word in w1: 
        d1counta = d1counta + 1
      elif word in w4: 
        d1counta = d1counta + 1
      elif word in w6:
         d1counta = d1counta + 1
      elif word in w2 or word in w3 or word in w8:
        d1countb = d1countb + 1
      else:
        d1countc = d1countc + 1  
    
    elif word in d2:
      if word in w1:
        d2counta = d2counta + 1
      elif word in w2:
        d2countb = d2countb + 1
      else:
        d2countc = d2countc + 1  
     
    elif word in d3:
      if word in w1:
        d3counta = d3counta + 1
      elif word in w2:
        d3countb = d3countb + 1
      else:
        d3countc = d3countc + 1  
    
    else:
      print()  
       
for stemwords in documentsNoStop:
  for word in d1:
    if word in w1:
      c = c+1
    elif word in w2:
      c2 = c+1
    else:
      c3 = c3+1
  
    
# tfd1love = c/d1counta  
# print(tfd1love)
# tfd1cat = c/d1countb
# print(tfd1cat)
  






#print(docMatrix)

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []



#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here