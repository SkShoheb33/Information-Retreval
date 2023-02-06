import pandas as pd
class Bayes:
    def __init__(self) -> None:
        self.data = pd.read_excel('data.xlsx')
        # print(self.data)
        self.labels = self.data.columns[1:-1]
        self.predict = self.data[self.data.columns[-1]].unique()
        # print("hello" ,self.predict)
        self.classes = {}
        for c in self.predict:
            self.classes[c] = self.countValues(self.data[self.data.columns[-1]],c)
        # print("hi",self.classes)
        self.tables = {}
        for lable in self.labels:
            self.tables[lable] = self.create_table(self.data[lable])
        # print(self.labels)

    def countValues(self,col,value):
        # print(col,value)
        c = 0
        for i in col:
            if i == value:
                c+=1
        return c

    def create_table(self,column):
        # print(column)
        rows = column.unique()
        cols = self.predict
        df = {}
        for row in rows:
            print(row,column)
            df[row] = self.countValues(row,column)
        return df
        # print(rows,cols)
        print(df)
obj = Bayes()