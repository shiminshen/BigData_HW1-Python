from loadFile import loadTaxiData, loadWeatherData 
import pandas as pd

# load taxi data
tData = loadTaxiData()
# get neccesary data
subData = tData[['pYear', 'pMonth', 'pDay', 'passenger_count']]
# count sum of passenger in each day
dailyPassengerData = subData.groupby(['pYear', 'pMonth', 'pDay']).sum().reset_index()

# load weather data
wData = loadWeatherData()
# change column names of weather data for merging with taxi data
wData.columns = ['pYear', 'pMonth', 'pDay', 'maxTemp', 'minTemp', 'rain', 'snow', 'wetGround']

formatedData = pd.merge(dailyPassengerData, wData, on=['pYear', 'pMonth', 'pDay'])

print(formatedData)
