import pandas
import numpy as np

csvData = pandas.read_csv('values.csv', header=None)
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
