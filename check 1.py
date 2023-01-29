import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import csv
import math
from api_call import api_call
from add import add

from csv import reader
avg_temp,humidity=api_call()    
crops=[] 
add()
#print("1")   
with open("Finaldb.csv","r") as myfile:
    filereader=reader(myfile)
    j=0
    #print(type(filereader))
    for i in filereader:
        
        listt=i[3].split(".")
        
        if listt[0].isdigit() and listt[1].isdigit():
            a1=int("0"+listt[0])+int("0"+listt[1])/100000000
            listh=i[4].split(".")
            a2=int("0"+listh[0])+int("0"+listh[1])/100000000
            #print(a1,a2,avg_temp-273.16,humidity)
            if abs(a1-avg_temp+273.16)<0.1 and abs(a2-humidity)<10:
                         crops.append(i[7])
                         
print(crops)  
myfile.close() 
                
    
            
            




