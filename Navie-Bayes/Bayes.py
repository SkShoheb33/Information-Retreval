import pandas as pd
class Bayes:
    def __init__(self):
        self.data = pd.read_excel('data.xlsx')
        self.tables = {}
        self.table_names = self.data.columns[1:-1]
        self.predict = self.data.columns[-1]
        self.predicted_values = self.data[self.predict].unique()
        print(self.predict)
        for name in self.table_names:
            self.createTable(name)
        # print(self.tables)
        # for table in self.tables:
        #     print(self.tables[table])
    def createTable(self,table_name):
        unique = self.data[table_name].unique()
        c = 0
        self.tables[table_name] = pd.DataFrame(data=None,index=unique,columns=self.predicted_values)
        for row in self.predicted_values: #no yes
            for col in unique: #rows 
                self.tables[table_name][row][col] = len(
                    self.data[(self.data[table_name]==col) & (self.data[self.predict]==row)]
                    )/len(self.data[self.data[self.predict]==row])    
    # def classifyQuery(self,query):
        
obj = Bayes()