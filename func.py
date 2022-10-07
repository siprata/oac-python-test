# Import the Libararies
import pandas as pd

########################################################################################################################
#Read the Files

#NETWORK
df1 = pd.read_excel("oci://CloudWorldDemo/Input_Test.xlsx")

#Assign to another file

result=df1

result.to_excel("oci://CloudWorldDemo/Output_Test.xlsx")