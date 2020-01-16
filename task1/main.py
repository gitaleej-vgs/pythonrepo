from classes.AWSTemplate import Template 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string", default=[], nargs='*')
args = parser.parse_args().string
temp = Template()
for x in args:
    temp.getServices(x)
