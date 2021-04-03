import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loadFile():
    data = pd.read_csv('births.csv')
    processData(data)

def processData(data):
   data['day'].fillna(0,inplace=True)
   data['day'] = data['day'].astype(int)
   data['decade'] = 10*(data['year']//10)

   makeVisualization(data)
   dataExplorations(data)



def makeVisualization(data):
    sns.set()
    birth_decade = data.pivot_table('births',index='decade',columns='gender',aggfunc='sum')
    birth_decade.plot()
    plt.ylabel('Total births per year')
    plt.show()

def dataExplorations(data):
    quartiles = np.percentile(data['births'],[25,50,75])
    outlier = quartiles[1]
    sig = 0.74 * (quartiles[2] - quartiles[0])
    try:
        data['day'] = data['day'].astype(int)
        data['Index'] = pd.to_datetime(1000*data.year + 100* data.month +data.day,format = '%Y%m%d' )
        data['dayofweek'] = data.index.dayofweek
        data.pivot_table('births',index='dayofweek',columns='decade',aggfunc='mean').plot()
        plt.gca().set_xticklabels(['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'])
        plt.ylabel('mean births by day')
        plt.show()
        print(data)
    except:
        print(data)



loadFile()
