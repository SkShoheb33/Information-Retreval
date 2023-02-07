import pandas as pd
class Bayes:
    def __init__(self):
        self.data = pd.read_excel('data.xlsx')
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
        result = 0
        m = 0
        for c in self.predicted_values:
            a = 1
            for k,i in zip(self.tables,query):
                a *= self.tables[k][c][i]
            if m<a:
                m = a
                result = c
        print(result)
            
obj = Bayes()
obj.classifyQuery("Sunny Hot High Strong")