import pandas as pd

def sampling():
    """Read all data file to matrix
    :returns: TODO

    """
    fileNames = [ 
            # './data/test.csv',
            # './data/test.csv',
            './data/yellow_tripdata_2015-07.csv' ,
            './data/yellow_tripdata_2015-08.csv' ,
            './data/yellow_tripdata_2015-09.csv' ,
            './data/yellow_tripdata_2015-10.csv' ,
            './data/yellow_tripdata_2015-11.csv' ,
            './data/yellow_tripdata_2015-12.csv'
            ]
    matrixs = []
    print('Loading Data')
    # load all csv files
    for fileName in fileNames:
        # read original data
        data = pd.read_csv(fileName)
        matrixs.append(data.sample(100000))

    newData = pd.concat(matrixs)
    newData.to_csv('./data/sampled.csv')

    return newData

sampling()
