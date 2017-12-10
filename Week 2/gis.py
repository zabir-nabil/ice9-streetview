import pandas as pd

class KmltoPd(object):
    def __init__(self,loc):
        data = pd.read_csv(open(loc, 'r'))

        sim = data['ns1:SimpleData']
        cor = data['ns1:coordinates']

        self.roads = {}

        for a, b in zip(sim, cor):
            self.roads[a] = b.split(' ')

    def toNumber(self,x):
        return [float(i) for i in x][::-1]

    def transform(self,alist):
        for a in alist:
            yield self.toNumber(a.split(','))

    def generate(self,ward):
        return list(self.transform(self.roads[ward]))
    def tostring(self,ward):
        temp=self.generate(ward)
        raw=''
        for items in temp:
            raw+= str(items).replace('[','').replace(' ','').replace(
                ']','|')
        return raw[:-1]
    def getKeys(self):
        return self.roads.keys()
