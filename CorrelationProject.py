import csv
import plotly.express as px
import numpy as p

#fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
#fig.show()  
 
Icecream=[]    
Temperature=[]

with open("Correlation4.csv",newline="")as f:
    df=csv.DictReader(f)
    for row in df:
        Icecream.append(float(row["Marks In Percentage"]))
        Temperature.append(float(row["Days Present"]))

    

correlation=p.corrcoef(Icecream,Temperature)
print(correlation)
