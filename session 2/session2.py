import pandas as pd
import matplotlib.pyplot as plt

"""
    Simply start by creating an array including paticipant IDs in the study.
"""
patientIDs = ['GS01', 'GS03', 'GS04', 'GS06']


"""
    Create an empty dictionary to be filled later.
"""
gaitData = {}


"""
    Loop over participants, read their files, extract desired info and put them
    in new data sets.
"""
for patient in patientIDs: #in each iteration, the 'patient' variable will take a value from 'patientIDs'.
    fileName = patient + '_new.xls'
    data = pd.read_excel(fileName, sheet_name='results', index_col = False)

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
        mos_min = row[16]
        newRow = pd.DataFrame([[timeStamp, mos_avg, mos_min]], columns = myColumns) #define a one-row dataframe
        selectedData = selectedData.append(newRow, ignore_index = True) #add the one-row dataframe which was just created to the empty database created earlier
    
    """
        This section will look at all data measured at the same time and 
        calcualates an average of multiple measurements and adds that to the 
        output data.
    """
    outputData = pd.DataFrame(columns = myColumns)
    uniqueValues = selectedData.Time.unique()
    for v in uniqueValues:
        df = selectedData.loc[selectedData['Time'] == v]
        finalMosAvg = df['mos_avg'].mean()
        finalMosMin = df['mos_min'].mean()
        newRow = pd.DataFrame([[v, finalMosAvg, finalMosMin]], columns = myColumns)
        outputData = outputData.append(newRow, ignore_index = True)
        
        meanMOSAVG = outputData['mos_avg'].mean()
        meanMOSMIN = outputData['mos_min'].mean()
        gaitData[patient] = (meanMOSAVG, meanMOSMIN)
    
    """
        Export results to a .csv file
    """
    outputData.to_csv(patient + '_processed.csv')
    
    """
        Some plotting
    """
#    plt.figure()
    plt.scatter(outputData['Time'],outputData['mos_avg'])
    plt.title(patient)
    plt.xlabel('Time')
    plt.ylabel('MOS_AVG')
    plt.grid()
    plt.ylim([0,0.5])
    print(patient, 'is done.')