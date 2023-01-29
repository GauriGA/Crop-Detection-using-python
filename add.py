import pandas as pd
import requests
import json
import csv
import datetime
from api_call import api_call
from csv import writer
def add():
    avg_temp,humidity=api_call() 
    x=datetime.datetime.now()
    with open("DailyDelhiClimateTrain.csv","a") as myfile:
        writerobj=writer(myfile)
        writerobj.writerow([("x.year"+"-"+"x.month"+"-"+"x.day"),avg_temp,humidity])
    myfile.close()
    
    
    