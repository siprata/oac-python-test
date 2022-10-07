# Import the Libararies
import pandas as pd

########################################################################################################################
#Read the Files

#NETWORK
df1 = pd.read_excel("https://objectstorage.us-ashburn-1.oraclecloud.com/n/idhzcjmyisms/b/CloudWorldDemo/o/", "Input_Test.xlsx")

#Assign to another file

result=df1

result.to_excel("https://objectstorage.us-ashburn-1.oraclecloud.com/n/idhzcjmyisms/b/CloudWorldDemo/o/Output_Test.xlsx")