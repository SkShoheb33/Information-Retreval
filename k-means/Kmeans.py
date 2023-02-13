# from random import random
import random
class Kmeans:
    def __init__(self,docIds,n):
        self.numberOfClusters = n
        self.documents = docIds
        self.clusters = {}
        seeds = []
        for i in range(self.numberOfClusters):
            try:
                k = random.randint(0,self.numberOfClusters)
                while k in seeds:
                    k = random.randint(0,self.numberOfClusters)
                seeds.append(k)
                self.clusters[f'cluster {i+1}'] = [[],docIds[k]]
            except IndexError:
                print("Enter valid number of clusters.... ")
    def mean(self,s):
        return sum(s)/len(s)
    def distance(self,docId,mean):
        return abs(docId-mean)
    def clusturing(self):
        while True:
            present = {}
            for cluster in self.clusters:
                present[cluster] = []
            for docId in self.documents:
                m = 1000
                c = ""
                for cluster in self.clusters:
                    if m > self.distance(docId,self.clusters[cluster][-1]):
                        m = self.distance(docId,self.clusters[cluster][-1])
                        c = cluster
                present[c].append(docId)
            if present[c] == self.clusters[c][0]:
                break
            else:
                for cluster in self.clusters:
                    self.clusters[cluster][0] = present[cluster]
                    self.clusters[cluster][1] = self.mean(present[cluster]) 
l = [1,2,3,4,7,12,8,9,11,19]
n = int(input("Enter number of clusters : "))
obj = Kmeans(l,n)
obj.clusturing()
for cluster in obj.clusters:
    print(cluster ," : ",obj.clusters[cluster][0])
