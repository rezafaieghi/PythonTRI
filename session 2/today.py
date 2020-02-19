import pandas as pd

patientIDs = ['GS01', 'GS03', 'GS04', 'GS06']

#How to access directories in Python
#import os
#from os.path import dirname, abspath
#
#currentDir = dirname(abspath(__file__))
#inDataDir = "data\\RawGaitData\\"
#outDataDir = "data\\ProcessedGaitData\\"

rawGaitData = {}

for patient in patientIDs:
    fileName = patient + '_new.xls'
    data = pd.read_excel(fileName, sheet_name='results', index_col = False)
    rawGaitData[patient] = data
    
    myColumns = ['Time', 'mos_avg', 'mos_min'] #let's assume that we are interested only in these columns from the whole data
    selectedData = pd.DataFrame(columns = myColumns) #define an empty pandas dataframe to be filled later.

    for index, row in data.iterrows(): #This is how we interate over the rows of a pandas dataframe. 
        time = row[0]
        year = int(time[6:10])
        month = int(time[11:13])
        day = int(time[14:16])
        hour = int(time[18:20])
        minute = int(time[21:23])
        second = int(time[24:26])
        timeStamp = pd.Timestamp(year = year, month = month, day = day, hour = hour, minute = minute, second = second)
        
        mos_avg = row[15]
        mos_min = row['MOS minimum']
        
        newRow = pd.DataFrame([[timeStamp, mos_avg, mos_min]], columns = myColumns) #define a one-row dataframe
        selectedData = selectedData.append(newRow, ignore_index = True) #add the one-row dataframe which was just created to the empty database created earlier


