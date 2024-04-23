import pandas as pd
import os
#f="D:\code\python\json project\Billionaire Plus_Details.json"
#df = pd.read_json(f, orient='index')
#print(df)
#df.to_excel("D:\code\python\json project\output1.xlsx")
#function to convert json data to df
#f="D:\code\python\json project\Billionaire Plus_Details.json"
#df = pd.read_json(f, orient='index')
#function to convert df to excel
def convertjsontodf():
    f=input("Enter directory path")
    l=os.listdir(f)
    for i in l:
       j= os.path.join(f,i)
       print(i)
       df = pd.read_json(j, orient='index')
       df.to_excel("D:\code\python\json project\output.xlsx")
    print(df)
#main func
convertjsontodf()
