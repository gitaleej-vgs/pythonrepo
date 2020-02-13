#pip install     pyyaml

import json as js
import yaml


class GcpTemplate:
    def __init__(self):
        mappingdata = js.loads(open("newmapping.json").read())
        outputData=js.loads(open("C://Users//personal//Desktop//pythonrepo//task1//output//2ec2withebs.json").read())
        pass

    def getgcptemplate(self):
        servicesNames =[]
        finalArray=[]
        finalGcpArray=[]
        count=0
        for serviceData in outputData:
            dic = {}
            finalDict = {}
            finalGcpDict = {}
            for singleService in serviceData:
                servicesList = singleService.split("::")
                serviceType=servicesList[1]
                properties = mappingdata["Properties"]
                splitedType=servicesList[2].split("'")
                subType=splitedType[0]
                mappings = loadedData['Mappings']
                serviceProperties = serviceData[singleService]
                propBlankDict = {}
                prop={}
                for property in serviceProperties:
                    if property in properties:
                        if property in mappings:
                            propBlankDict[properties[property]] = mappings[property][serviceProperties[property]]
                        else:propBlankDict[properties[property]]=serviceProperties[property]#####does not have corresponding gcp values
                Type =""
                services=loadedData['Services']
                subservices=loadedData['Subservices']
                Type+=services[serviceType]+".v1."+subservices[subType]
                finalGcpDict['name']='resource'+str(count)
                count=count+1
                finalGcpDict['type']=Type
                finalGcpDict['properties']=propBlankDict
                finalGcpArray.append(finalGcpDict)

        tempFileName = "gcpVolume.yaml"
        FinalTempName = "configurationfinalfile.yaml"
        dict = {'resources':[]}
        with open(tempFileName, 'r') as stream:
            docs = yaml.load_all(stream, Loader=yaml.FullLoader)
            dictionary = yaml.safe_load(stream)
            array=[]
            for i in finalGcpArray:
                resourcesList=dictionary['resources']
                for x in resourcesList:
                    if x['type']==i['type']:
                        x['properties'].update(i['properties'])
                        i['properties']=x['properties']
                        propList=i['properties'].keys()
                        if 'machineType' in propList:
                            i['properties']['machineType']='zones/'+i['properties']['zone']+'/machineTypes/'+x['properties']['machineType']
                            array.append(i)
                            break
                dict['resources'] = array
                with open('configurationfinalfile.yml', 'w+') as file:
                    documents = yaml.safe_dump(dict, file,default_flow_style=False,indent=2)