import pandas
import numpy

data1=pandas.read_csv('datasets/train.csv')
wordCloud=pandas.read_csv('Training/wordCloud.csv', encoding='utf-8')

print(data1.shape)
print(wordCloud.shape)
