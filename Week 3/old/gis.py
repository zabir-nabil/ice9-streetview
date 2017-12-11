import re

class KML2DICT(object):
    def __init__(self,loc):
        with open(loc) as file:
            self.text = file.read()
        self.roads = self.get_dictionary()

    def get_dictionary(self):
        pattern = re.compile(r'<SimpleData name=".*">(.*)</SimpleData>')
        ward_names = pattern.findall(self.text)

        pattern = re.compile(r'<coordinates>(.*)</coordinates>')
        ward_coordinates = pattern.findall(self.text)

        df={}
        for i,j in zip(ward_names,ward_coordinates):
            df[i]=j.split(' ')
        return df

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
