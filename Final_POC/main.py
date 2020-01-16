from classes.AWSTemplate import Template
from classes.AWSMap import Gcptemplate
import argparse


class Oprations():
    def __init__(self):
        pass

    def aceeptfilenames(self,filenames):
        parser = argparse.ArgumentParser()
        parser.add_argument("string", default=[], nargs='*')
        args = parser.parse_args().string
        for x in args:
            filenames.append(x)

    def makegcptemplate(self,filename):
        gcptemplate = Gcptemplate()
        gcptemplate.getgcptemplate(filename)

class Main:
    filenames = []

    oprations = Oprations()
    oprations.aceeptfilenames(filenames)
    for filename in filenames:
        print("filename")
        oprations.makegcptemplate(filename)

main = Main()