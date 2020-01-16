import os
import json as js
import pathlib
class Template:
    def __init__(self):
        self.path=os.getcwd()
        file = pathlib.Path("output")
        print(self.path)
        if file.exists ():
            print ("dir exist")
        else:
            os.makedirs("output")
            print("dir created")
        
    def getServices(self,fileName):
        print(fileName)
        resourcesArray = []
        loadedData =js.loads(open(fileName).read())
        serviceNames = []
        resourceData= loadedData['Resources']
        for serviceName in resourceData:
            serviceNames.append(serviceName)
        for serviceName in serviceNames:
            serviceData=resourceData[serviceName]
            #os.makedirs("output")
            #path=os.getcwd()
            #print(path)
            #newpath=path.replace("\\","//")
            resourcesArray.append({str(serviceData['Type']):serviceData['Properties']})
            
        with open(self.path+"//output//"+fileName, "w") as f:
            js.dump(resourcesArray,f,indent=4)



