import numpy as np
import pandas as pd


# Series
data_series = np.random.normal(0,1,100)
p_series = pd.Series(data_series)

#print(p_series.head(5))
#print(p_series.tail(5))

data_series_2 = np.random.normal(0,5,100)
frame={'column1':data_series,
    'column2': data_series_2}

df=pd.DataFrame(frame)

