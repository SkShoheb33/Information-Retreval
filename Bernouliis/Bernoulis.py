import pandas as pd
class Bernoullis:
    def __init__(self,csv_file):
        self.data = pd.read_excel(csv_file)
        self.tables = {}
        self.features = self.data.columns[1:-1]
        self.predict = self.data.columns[-1]
        self.predicted_values = self.data[self.predict].unique()
        for feature in self.features:
            self.create_table(feature)
    def create_table(self,table_name):
        rows = self.data[table_name].unique()
        self.tables[table_name] = pd.DataFrame(data=None,index=rows,columns=self.predicted_values)
        for c in self.predicted_values:
            for row in rows:
                self.tables[table_name][c][row] = len(
                    self.data[(self.data[self.predict]==c)&(self.data[table_name]==row)]
                    )/len(
                        self.data[self.data[self.predict]==c]
                    )
    def classifyQuery(self,query):
        query = list(set(query.split()))
        m = 0
        result = ""
        for c in self.predicted_values:
            a = len(self.data[self.data[self.predict]==c])/len(self.data[self.predict])
            for table in self.tables:
                a = len(self.data[self.data[self.predict]==c])/len(self.data[self.predict])
                for row in self.tables[table].index:
                    if row in query:
                        a *= self.tables[table][c][row]
                    else:
                        a *= (1-self.tables[table][c][row])
            print(a)
            if m < a:
                m = a
                result = c
        print(result)
obj = Bernoullis('data.xlsx')
obj.classifyQuery("Rain Mild High Strong")