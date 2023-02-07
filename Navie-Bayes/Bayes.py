import pandas as pd
from collections import Counter
class Bayes:
    def __init__(self,csv_file):
        self.data = pd.read_excel(csv_file)
        self.tables = {}
        self.table_names = self.data.columns[1:-1]
        self.predict = self.data.columns[-1]
        self.predicted_values = self.data[self.predict].unique()
        for name in self.table_names:
            self.createTable(name)
    def createTable(self,table_name):
        unique = self.data[table_name].unique()
        c = 0
        self.tables[table_name] = pd.DataFrame(data=None,index=unique,columns=self.predicted_values)
        for row in self.predicted_values: #no yes
            for col in unique: #rows 
                self.tables[table_name][row][col] = len(
                    self.data[(self.data[table_name]==col) & (self.data[self.predict]==row)]
                    )/len(self.data[self.data[self.predict]==row])    
    def classifyQuery(self,query):
        query = query.split()
        count = dict(Counter(query))
        query = list(count.keys())
        result = 0
        m = 0
        try:
            for c in self.predicted_values:
                a = len(self.data[self.data[self.predict]==c])/len(self.data[self.predict])
                for k,i in zip(self.tables,query):
                    a *= (self.tables[k][c][i]**count[i])
                if m<a:
                    m = a
                    result = c
            print("The data predict : ",result)
        except KeyError:
            print("Unable to predict result")
            print("Please Provide relavant data / check splelling mistakes..... ")
        finally:
            print("Successfully executed")
            
obj = Bayes('data.xlsx')
obj.classifyQuery("Rain Mild High Strong")