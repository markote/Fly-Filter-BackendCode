# coding=utf-8
'''
Reads the json "citiesInfo.json" and produces "citiesCompleteInfo.json" that have images for all the cities.
'''
from django.core.management.base import BaseCommand
import csv
import requests
import time
import json
import random

inputJson="citiesInfo.json"
outputJson="citiesCompleteInfo.json"


def firstPassing(result):
    
    im_country={} 
    
    for city in result:
        if city["imatge"] != None :
            if city["country"] not in im_country :
                im_country[city["country"]]=[]
            im_country[city["country"]]+=[city["imatge"]]

    return im_country


def completeJson(im_country, result):
    for city in result:
        if city["imatge"] == None and city["country"] in im_country:
            i_rand=random.randint(0,len(im_country[city["country"]])-1)
            city["imatge"] = im_country[city["country"]][i_rand]

    return result

class Command(BaseCommand):
    
    help=("Read the json and complete missing images")

    def add_arguments(self,parser):
        #the json generated by the citiesInfo.py command
        pass
    
    def handle(self, *args, **options):
        try:
            with open(inputJson,"r") as json_file:
                result = json.load(json_file)
                
                

            im_country=firstPassing(result)
            result=completeJson(im_country,result)

            with open(outputJson,"w") as json_file:
                json.dump(result, json_file)

        except Exception as e:
            print("Exception occured")
            import traceback
            traceback.print_exc()

