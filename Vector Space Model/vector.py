import numpy as np
import pandas as pd
import os
import re
import json
from math import sqrt
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class Vector:
    def __init__(self,corpus):
        self.corpus = corpus
        self.numberOfDocuments = len(os.listdir(self.corpus))
        self.dictionary = []
        self.documents = {}
        self.vectors = {}
        for document in os.listdir(self.corpus):
            self.documents[document[:-4]] = self.tokenize(open(self.corpus+"/"+document,encoding="utf-8").read())
        self.dictionary.sort()
        # for document in os.listdir(self.corpus):
        for document in self.documents:
            self.setVector(document)
                   
    def tokenize(self,document):   #document is string type
        ps = PorterStemmer()
        document = re.sub(r'[^a-z A-Z]',"",document)
        document = document.lower().split()
        n = len(document)
        for i in range(n):
            # print(document)
            document[i] = ps.stem(document[i])
            if document[i] not in self.dictionary:
                self.dictionary.append(document[i])
        return document
    
    
    def setVector(self,document): # document name    document is list type no reutn type (0,2,4,1)
        # print(document)
        ps = PorterStemmer()
        document_title = document
        # document = sorted(query.split())
        document = sorted(self.documents[document])
        self.vectors[document_title] = []
        # print(document)
        for token in self.dictionary:
            # print(token)
            if token in document:
                self.vectors[document_title].append(document.count(token))
            else:
                self.vectors[document_title].append(0)
                    
                
    def getVector(self,document): # it gets vector vector name type : list
        return self.vectors[document]
    
    
    def cosineSimilarity(self,query,document):
        # pass
        # print(query)
        # print(self.dotProduct(query,document),self.modVector(query),self.modVector(document),self.dotProduct(query,document)/(self.modVector(query)*self.modVector(document)))
        try:
            return self.dotProduct(query,document)/(self.modVector(query)*self.modVector(document))
        except ZeroDivisionError:
            # print("No such word in query") 
            pass
        
    def dotProduct(self,vector1,vector2):
        l = 0
        for i in range(len(vector1)):
            l += (vector1[i]*vector2[i])
        return l
    
    
    def modVector(self,vector): #vector 
        d = 0
        for i in vector:
            d += i**2
        return sqrt(d)
    
    def convert_vector(self,query):
        # query = re.sub('^[a-z A-Z]',"",query)
        query = query.lower()
        query = sorted(query.split())
        # for i in range(len(query)):
        #     query[i] = re.sub('^[a-z A-Z]',"",query[i])
        vector = []
        # print(query)
        ps = PorterStemmer()
        for i in range(len(query)):
            query[i] = ps.stem(query[i])
        for token in self.dictionary:
            if token in query:
                vector.append(query.count(token))
            else:
                vector.append(0)
        # print(vector)
        return vector
    
    def getDocument(self,query):
        doc = None
        query = self.convert_vector(query)      
        d = -1
        try: 
            for document in self.vectors:
                if d < self.cosineSimilarity(query,self.getVector(document)):
                    # print(d)
                    d = self.cosineSimilarity(query,self.getVector(document))
                    doc = document
            return doc
        except TypeError:
            return "Sorry! No documents retrived"
    
obj = Vector("documents")
# print(obj.modVector(obj.convert_vector("united states")))
# print(obj.modVector(obj.getVector('america')))
# print(len(obj.convert_vector("united states")))
# print(len(obj.getVector('america')))
# print((obj.convert_vector("united states")).count(0))
# print(obj.getVector('america').count(0))
# print(obj.dotProduct(obj.getVector('america'),obj.convert_vector("united states")))
# print(obj.dictionary)
print(obj.getDocument("tree"))

# print(obj.numberOfDocuments)
# print(os.listdir('documents'))    