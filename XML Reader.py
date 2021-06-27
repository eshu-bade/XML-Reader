import xml.etree.ElementTree as ET
import pandas as pd

"""
First, we load the xml file into python to perform necessary actions

"""
tree = ET.parse('myfile.xml')
root = tree.getroot()
dataframe = pd.DataFrame() # Creating a new dataframe to save it to Excel sheet

for child in root.findall("TestCase"): # Iterating through the XML file to find Requirement ID of sub child
    for each_item in child.findall('TestCaseSpecification'):
        require = each_item.find('Requirement')
        require_ID = require.attrib['ID']
        # print(require_ID)
    dataframe = dataframe.append([require_ID], ignore_index=True)
dataframe.columns = ['Requirement ID']
print(dataframe) # Printing to see the desired data frame
writer = pd.ExcelWriter('Result.xlsx', engine='xlsxwriter')
dataframe.to_excel(writer, sheet_name='Sheet1') #Writing the dataFrame into Excel sheet
writer.save()

#Saving the file and closing