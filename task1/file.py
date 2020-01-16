import json as js
class Template:
    def __init__(self):
        pass
    def getServices(self,fileName):
        print(fileName)
        loadedData =js.loads(open(fileName).read())
        reskey = []
        resource= loadedData['Resources']
        for i in resource:
            reskey.append(i)
        for x in reskey:
            d=resource[x]
            #print(d['Type'])
            print(d['Properties'])


