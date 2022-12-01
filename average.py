import pandas
import numpy as np

def getAve(path):
    csvData = pandas.read_csv(path, header=None)
    ave = []
    newCol = []
    newDF = pandas.DataFrame()
    for i in range(len(csvData.columns)):
        newCol.append(i)
        size = len(csvData[i])
        ave.append(np.sum(csvData[i])/size)
        newDF[i] = np.sum(csvData[i])/size
    resultDF = pandas.DataFrame(ave)
    resultDF.to_csv('result.csv')


getAve('./values.csv')
