import numpy as np
import pandas as pd

"""
    READ DATA FROM EXCEL
    Note that the Excel file is stored in a folder named 'data'. The folder 
    itself must be in the same directory where your code is saved.
    read_excel() returns data in a data structure called 'Dataframe'. dataframe
    is a special 2D data structures much like every excel sheet.
"""
dataQI = pd.read_excel('data\\CIHI - Public.xlsx',sheet_name='QI')
dataHome = pd.read_excel('data\\CIHI - Public.xlsx', sheet_name='Homes')



"""
    SELECT DATA USING .LOC METHOD
    The .loc[] method provides a label-based data selection inside a dataframe.
    Here, we are interested to find number of falls in each year. As such, we 
    crate three subsets of the dataQI dataframe using the .loc[] method. Note 
    that there are two conditions for inside .loc[] calls. The first one filters
    indicators related to falls, AND the second the filters a particular year
    in the data.
"""
df2014 = dataQI.loc[(dataQI['indicator']=='Falls in the Last 30 Days in Long-Term Care') & (dataQI['year_to']==2014)]
df2015 = dataQI.loc[(dataQI['indicator']=='Falls in the Last 30 Days in Long-Term Care') & (dataQI['year_to']==2015)]
df2016 = dataQI.loc[(dataQI['indicator']=='Falls in the Last 30 Days in Long-Term Care') & (dataQI['year_to']==2016)]



"""
    CALCULATE MEAN and STD
    Now that we have three subsets of records of falls in different years, we
    want to see what is the average and standard deviation of falls in each year
    across all nursing homes. From the dataset we know that the actual number of 
    falls are in a column labeled 'result'. As such, for every subset extracted
    in the previous step, we select the 'result' column. Then, we call mean()
    and std() functions that are provided by each dataframe in Pandas. In order
    to have easy-to-read values, we round results using round(x,n) functions in
    which x is the value to be rounded and n is the number of desired decimal
    points.
"""
mean2014 = round(df2014['result'].mean(),2)
std2014 = round(df2014['result'].std(),2)
mean2015 = round(df2015['result'].mean(),2)
std2015 = round(df2015['result'].std(),2)
mean2016 = round(df2016['result'].mean(),2)
std2016 = round(df2016['result'].std(),2)



"""
    PRINT RESULTS
    To print a variable x in python it is sufficient to call print(x). To add 
    more descriptions to it, we can addtionally print strings. However, every 
    section of the print output must be separated by a comma.
"""
print('mean no. of falls for 2014', mean2014, 'with std. of', std2014)
print("mean no. of falls for 2015", mean2015, 'with std. of', std2015)
print('mean no. of falls for 2016', mean2016, 'with std. of', std2016)


"""
    ==================== ADDITIONAL ITEMS ====================
    The printed results indicates that the average number of falls in nursing 
    homes tend to increa year by year. Let us now see what is the distribution
    of falls across nursing homes every year. One way to do this is to look at
    the histograms of falls across nursing homes for each year. To do this, we
    can again select the 'result' column of year-specific subsets and call the
    hist() method. You should be able to see plots on the interactive console
    on the right side window.
"""
df2014['result'].hist()
df2015['result'].hist()
df2016['result'].hist()


"""
    Histograms indicate close to normal distributions for all years. In each 
    year, there are a few homes with more than 25 falls which seems to be a lot.
    Let's see what are the names of thse nursing homes. To do this, we have to
    extract home IDs in dataQI and look for them in the other Excel sheet which
    was dataHome.
"""
#First, let's find the homes with more than 25 homes
df2014Above25Falls = df2014.loc[df2014['result']>25] 
df2015Above25Falls = df2015.loc[df2015['result']>25]
df2016Above25Falls = df2016.loc[df2016['result']>25]

#Second, let's extract home IDs from the above extracted set
HomeIDs2014Above25Falls = df2014Above25Falls['cihi_public_hid'] 
HomeIDs2015Above25Falls = df2015Above25Falls['cihi_public_hid']
HomeIDs2016Above25Falls = df2016Above25Falls['cihi_public_hid']

"""
    It is now the time to look in dataHome dataframe and print names. For this
    step we need to write a for-loop. Here are some explanations. We will cover
    these in detail in the next session.
    
    It is important to note that in Python vertical space does matter! When you
    write a for loop, you need to indent whatever code you have inside the loop
    as shown in the below example.
    
    You will note a for loop is written the following way:
        for i in HomeIDs2014Above25Falls:
    This basically says that iterate over HomeIDs2014Above25Falls and in each
    iteration assign one element from HomeIDs2014Above25Falls to i. You can 
    use print(i) to check the values of i and see how it works.
    
    The rest of for-loops are basically finding home name with its index in the
    other dataframe (dataHomes).
"""
print('=============================================')
print('List of homes with more than 25 falls in 2014')
for i in HomeIDs2014Above25Falls:
    homeName = dataHome.loc[dataHome['cihi_public_hid']==i]
    print(homeName['name'].values)

print('=============================================')
print('List of homes with more than 25 falls in 2014')
for i in HomeIDs2015Above25Falls:
    homeName = dataHome.loc[dataHome['cihi_public_hid']==i]
    print(homeName['name'].values)

print('=============================================')
print('List of homes with more than 25 falls in 2014')
for i in HomeIDs2016Above25Falls:
    homeName = dataHome.loc[dataHome['cihi_public_hid']==i]
    print(homeName['name'].values)


"""The above code has a lot of repetition. To avoid it, it is a good idea to 
    write a function to do the job. To do this, we define a function called
    PrintHomeNames(). The signature to define a function is:
        def <function name>(list of agumentes separated by comma):
    
    Remember that indentationas are important and mean something in Python. Here,
    again for code inside the function we apply one indentation. For everthing 
    inside the for loop, we apply another indentation.
"""

def PrintHomeNames(list): #define function
    print('=============================================')
    for i in list:
        homeName = dataHome.loc[dataHome['cihi_public_hid']==i]
        print(homeName['name'].values)  

PrintHomeNames(HomeIDs2014Above25Falls) #call the function for different years
PrintHomeNames(HomeIDs2015Above25Falls)
PrintHomeNames(HomeIDs2016Above25Falls)
