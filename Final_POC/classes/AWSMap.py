#pip install     pyyaml
import os

import json as js
import yaml
import pathlib


class Gcptemplate:
    """
    this class gives gcptemplate
    """
    def __init__(self):
        """
        function initializes mappingdata which is going to be use through out the class
        """
        self.path = os.getcwd()  #return current directory path
        self.mappingdata = js.loads(open(self.path+"//mapping//newmapping.json").read())
        pass

    def checkfileexist(self, filename):
        if os.path.isfile(self.createfilepath("AWSTemplates", filename)):
            return True
        else:
            prints("File not exist")
            return False

    def getserviceprop(self,filename):
        """
        :type filename: string         this return the list of resources with their properties
        """
        if self.checkfileexist(filename):
            templateData = js.loads(open(self.createfilepath("AWSTemplates",filename)).read())
        else:
            return
        resources = []
        resourceData = templateData['Resources']
        for serviceName in resourceData:
            print(resourceData[serviceName]['Type'])
            resources.append({resourceData[serviceName]['Type']: resourceData[serviceName]['Type']})
        return resources

    def createfilepath(self,folder,fileName):
        return self.path+"//"+folder+"//"+fileName

    def getgcptemplate(self,filename):
        """
        :type filename: string
        """
        templateData = self.getserviceprop(filename)
        finalGcpArray = []
        count = 0
        print(len(templateData))
        for serviceData in templateData:
            finalGcpDict = {}
            for singleService in serviceData:
                servicesList = singleService.split("::")
                serviceType = servicesList[1]
                properties = self.mappingdata["Properties"]
                splitedType = servicesList[2].split("'")
                subType = splitedType[0]
                mappings = self.mappingdata['Mappings']
                serviceProperties = serviceData[singleService]
                propBlankDict = {}
                for property in serviceProperties:
                    if property in properties:
                        if property in mappings:
                            propBlankDict[properties[property]] = mappings[property][serviceProperties[property]]
                        else:propBlankDict[properties[property]] = serviceProperties[property]#####does not have corresponding gcp values
                Type = ""
                services = self.mappingdata['Services']
                subservices = self.mappingdata['Subservices']
                Type += services[serviceType]+".v1."+subservices[subType]
                finalGcpDict['name'] = 'resource'+str(count)
                count = count+1
                finalGcpDict['type'] = Type
                finalGcpDict['properties'] = propBlankDict
                finalGcpArray.append(finalGcpDict)
        dict = {'resources':[]}
        with open(self.createfilepath("GCPTemplates","gcpVolume.yaml"), 'r') as stream:
            dictionary = yaml.safe_load(stream)
            array = []
            for i in finalGcpArray:
                resourcesList = dictionary['resources']
                for x in resourcesList:
                    if x['type'] == i['type']:
                        x['properties'].update(i['properties'])
                        i['properties'] = x['properties']
                        propList = i['properties'].keys()
                        if 'machineType' in propList:
                            i['properties']['machineType'] = 'zones/'+i['properties']['zone']+'/machineTypes/'+x['properties']['machineType']
                        array.append(i)
                dict['resources'] = array
            with open(self.createfilepath("AWS_GCP_Temp","filename.yaml"), 'w+') as file:
                documents = yaml.safe_dump(dict, file,default_flow_style=False,indent=2)