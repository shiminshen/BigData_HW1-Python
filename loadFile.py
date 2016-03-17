import numpy as np
import pandas as pd
import csv

def loadTaxiData():
    """Read all data file to matrix
    :returns: TODO

    """
    fileNames = [ 
            './data/test.csv'
            # './data/yellow_tripdata_2015-07.csv' ,
            # './data/yellow_tripdata_2015-08.csv' ,
            # './data/yellow_tripdata_2015-09.csv' ,
            # './data/yellow_tripdata_2015-10.csv' ,
            # './data/yellow_tripdata_2015-11.csv' ,
            # './data/yellow_tripdata_2015-12.csv'
            ]
    matrixs = []
    print('Loading Data')
    # load all csv files
    for fileName in fileNames:
        # read original data
        data = pd.read_csv(fileName)
        matrixs.append(data)

    newData = pd.concat(matrixs)
    # split pickup time to year, month, day, hour, minute, second
    pickupTime = newData['tpep_pickup_datetime'].str.split('[: -]').apply(pd.Series,1)
    # change type of data columes
    pickupTime[[0,1,2,3,4,5]] = pickupTime[[0,1,2,3,4,5]].astype(int)
    # change column names
    pickupTime.columns = ['pYear', 'pMonth', 'pDay', 'pHour', 'pMinute', 'pSecond']

    newData = newData.join(pickupTime)

    return newData

def loadWeatherData():
    """ Read weather files into data frame
    :returns: TODO

    """
    fileName = './data/weatherData.csv'
    return pd.read_csv(fileName)
