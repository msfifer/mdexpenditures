import pandas
import re

# -*- coding: utf-8 -*-
"""
Created on Sat May 31 13:36:37 2014

@author: Matt
"""

zipcheck = re.compile('[^0-9]')

data08 = pandas.read_csv('Maryland_Funding_FY08_Payments_Data.csv')
dataIndices = [not zipcheck.match(data08['Vendor Zip'][x]) for x in range(len(data08))]
data08 = data08[dataIndices]
data09 = pandas.read_csv('Maryland_Funding_FY09_Payments_Data.csv')
dataIndices = [not zipcheck.match(data09['Vendor Zip'][x]) for x in range(len(data09))]
data09 = data09[dataIndices]
data10 = pandas.read_csv('Maryland_Funding_FY10_Payments_Data.csv')
dataIndices = [not zipcheck.match(data10['Vendor Zip'][x]) for x in range(len(data10))]
data10 = data10[dataIndices]
data11 = pandas.read_csv('Maryland_Funding_FY11_Payments_Data.csv')
dataIndices = [not zipcheck.match(data11['Vendor Zip'][x]) for x in range(len(data11))]
data11 = data11[dataIndices]
data12 = pandas.read_csv('Maryland_Funding_FY12_Payments_Data.csv')
dataIndices = [isinstance(data12['Vendor Zip'][x], str) and not zipcheck.match(data12['Vendor Zip'][x]) for x in range(len(data12))]
data12 = data12[dataIndices]
data13 = pandas.read_csv('Maryland_Funding_FY13_Payments_Data.csv')
dataIndices = [isinstance(data13['Vendor Zip'][x], str) and not zipcheck.match(data13['Vendor Zip'][x]) for x in range(len(data13))]
data13 = data13[dataIndices]

allData = pandas.concat([data08, data09, data10, data11, data12, data13], ignore_index=True)
for x in range(len(allData)):
    if len(allData['Vendor Zip'][x]) < 5:
        allData['Vendor Zip'][x] = '0' * (5 - len(allData['Vendor Zip'][x])) + allData['Vendor Zip'][x] 

# loop through every zip, create a value for each year
allDataComputed = allData.drop_duplicates(cols=['Vendor Zip', 'Year']).copy(deep=True)
allDataComputed['Amount'] = 0
for x in allDataComputed.index:
    allDataComputed['Amount'][x] = sum(allData['Amount'][(allData['Vendor Zip'] == allDataComputed['Vendor Zip'][x]) & (allData['Year'] == allDataComputed['Year'][x])])
    print allDataComputed['Vendor Zip'][x],allDataComputed['Year'][x],allDataComputed['Amount'][x]

# write this as a csv
allDataComputed.to_csv('amount_per_zip.csv')
allDataComputed[allDataComputed['Year'] == 2008].to_csv('amount_per_zip2008.csv')
allDataComputed[allDataComputed['Year'] == 2009].to_csv('amount_per_zip2009.csv')
allDataComputed[allDataComputed['Year'] == 2010].to_csv('amount_per_zip2010.csv')
allDataComputed[allDataComputed['Year'] == 2011].to_csv('amount_per_zip2011.csv')
allDataComputed[allDataComputed['Year'] == 2012].to_csv('amount_per_zip2012.csv')
allDataComputed[allDataComputed['Year'] == 2013].to_csv('amount_per_zip2013.csv')
