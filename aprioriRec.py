# Product recommendation using Apriori algorithm

# Import required libraries
import numpy as np
import pandas as pd

import itertools

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def dataFrameToTransaction(dataset):
	#Transforming the list into a list of lists, so that each transaction can be indexed easier
	transactions = []
	for i in range(0, dataset.shape[0]):
	    transactions.append([str(dataset.values[i, j]) for j in range(0, dataset.shape[1]) if str(dataset.values[i, j]) != 'nan'])
	return transactions

def Encoder(transactions):
    # Encode data to form matrix    
    te = TransactionEncoder()
    te_data = te.fit(transactions).transform(transactions)

    df = pd.DataFrame(te_data,columns=te.columns_)
    return df

def getItems(itemName, k = 10):
    itemList = []
    item = frozenset({itemName})
    for i in data.itertuples():  
        if itemName in i[2] and len(itemList) < k:
            itemList.append(list(i[2].difference(item)))
    
    return (list(itertools.chain(*itemList)))


# Load dataset
dataset = pd.read_csv('input/Market_Basket_Optimisation.csv', header = None)

transactions = dataFrameToTransaction(dataset)
df = Encoder(transactions)

# Apply apriori algorithm (min support = 0.01)
df1 = apriori(df,min_support=0.01,use_colnames=True)

# sort in dscending order of support
df1 = df1.sort_values(by="support",ascending=False)

# add number of elements as length
df1['length'] = df1['itemsets'].apply(lambda x:len(x))

# select elements with 2 or more items and support >= 0.03
data = df1[(df1['length']>=2) & (df1['support']>=0.03)]

#itemList = getItems('chocolate')
#print(itemList)