import pandas as pd

def sampling():
    """Read all data file to matrix
    :returns: TODO

    """
    fileNames = [ 
            './data/yellow_tripdata_2015-07.csv' ,
            './data/yellow_tripdata_2015-08.csv' ,
            './data/yellow_tripdata_2015-09.csv' ,
            './data/yellow_tripdata_2015-10.csv' ,
            './data/yellow_tripdata_2015-11.csv' ,
            './data/yellow_tripdata_2015-12.csv'
            ]
    # useless columns in data
    uselessColums = [
            'RatecodeID',
            'tpep_dropoff_datetime',
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
    chunkSize = 2 ** 100
    sampleNum = 1000000
    print('Loading Data')
    # load all csv files
    for fileName in fileNames:
        # read original data
        chunks = []
        for chunk in pd.read_csv(fileName, chunksize=chunkSize):
            chunk = chunk.drop(uselessColums, axis=1)
            chunks.append(chunk)

        matrixs.append(pd.concat(chunks).sample(frac=0.05))
        print(fileName + ' loaded')

    newData = pd.concat(matrixs)
    newData.to_csv('./data/' + str(0.05) + 'sampled.csv')

    return newData

sampling()
