import numpy as np
import pandas as pd
import os
import re
import json
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class MyEngine:
    def __init__(self,corpus):
        ps = PorterStemmer()
        self.corpus = corpus
        self.document = []
        self.data = {}
        # self.labels = {}  # here labels take the names and satus of the file
        self.dictionary = {}
        self.id = 0
        self.doc_id = 0
        self.model = {}
        self.model['documents'] ={}
        self.model['data'] = {}
        self.model['postings'] = {}
        # print('hello')
        for file in os.listdir(corpus):
            # self.labels[] = True
            self.model['data'][file[:-4]] = []
            # print(self.corpus+file)
            # self.model['documents'][file[:-4]] = (self.doc_id,True)
            self.model['documents'][file[:-4]] = {}
            self.model['documents'][file[:-4]]['id'] = self.doc_id
            self.model['documents'][file[:-4]]['status'] = True
            self.doc_id += 1
            document = self.removeAllTheSpecialCharacter(open(self.corpus+file,encoding='utf-8').read()).lower().split()
            for word in document:
                word = ps.stem(re.sub(r'[^a-zA-Z0-9]', '',word ))
                if word not in self.dictionary:
                    self.dictionary[word] =self.id
                    self.model['postings'][word] = [self.model['documents'][file[:-4]]['id']]
                    self.id += 1
                elif self.model['documents'][file[:-4]]['id'] not in self.model['postings'][word]:
                    self.model['postings'][word].append(self.model['documents'][file[:-4]]['id'])
                self.model['data'][file[:-4]].append(self.dictionary[word])
        #posting compression starts here
        words_length = len(self.dictionary)
        # print(self.model['postings']['of'])
        for word in self.model['postings']:
            self.model['postings'][word].sort()
            prev = self.model['postings'][word][0]
            n = len(self.model['postings'][word])
            for i in range(1,n):
                self.model['postings'][word][i] -= prev
                prev = self.model['postings'][word][i]
        # print(self.data)
        # print(self.labels)
        # print(self.dictionary)
        # print(self.model)
    # def postingCompression(self):
        with open('stories.json','w') as fp:
            json.dump(self.model,fp)        
    def removeAllTheSpecialCharacter(self,word):
        special_characters = [".",";","!","@","#","$","%","^","&","*","(",")","{","}","[","]",":","'","/","<",">",'"',"+"]
        return "".join(filter(lambda char: char not in special_characters , word))
obj = MyEngine('stories/')
# print(obj.model['postings'])