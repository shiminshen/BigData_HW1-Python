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
            # './data/yellow_tripdata_2015-09.csv' ,
            # './data/yellow_tripdata_2015-10.csv' ,
            # './data/yellow_tripdata_2015-11.csv' ,
            # './data/yellow_tripdata_2015-12.csv'
            ]
    # useless columns in data
    uselessColums = [
            'RatecodeID',
            'store_and_fwd_flag',
            'payment_type',
            'fare_amount',
            'extra',
            'mta_tax',
            'tolls_amount',
            'improvement_surcharge',
            'total_amount'
            ]
    matrixs = []
    print('Loading Data')
    # load all csv files
    for fileName in fileNames:
        # read original data
        data = pd.read_csv(fileName)
        data = data.drop(uselessColums, axis=1)
        matrixs.append(data.sample(1000000))

    newData = pd.concat(matrixs)
    newData.to_csv('./data/sampled.csv')

    return newData

sampling()
