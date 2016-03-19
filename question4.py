from loadFile import loadTaxiData
import pandas as pd

# load taxi data
tData = loadTaxiData()
# get neccesary data
subData = tData[['pYear', 'pMonth', 'pDay', 'passenger_count']]
# count sum of passenger in each day
dailyPassengerData = subData.groupby(['pYear', 'pMonth', 'pDay']).sum().reset_index()

formatedData = pd.merge(dailyPassengerData, wData, on=['pYear', 'pMonth', 'pDay'])

