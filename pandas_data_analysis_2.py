import numpy as np
import pandas as pd


# Series
#data_series = np.random.normal(0,1,100)
#p_series = pd.Series(data_series)

#print(p_series.head(5))
#print(p_series.tail(5))

#data_series_2 = np.random.normal(0,5,100)
#frame={'column1':data_series,
#    'column2': data_series_2}

#df=pd.DataFrame(frame)

#students_ids = [n for n in range(200,220)]
##math_scores = np.random.normal(70,10,20)
#english_scores = np.random.normal(65,8,20)
#history_scores = np.random.normal(80,7,20)



#df=pd.DataFrame({
#    'Student ID': students_ids,
#    'Math Scores': math_scores,
#    'English Scores': english_scores,
#    'History Scores': history_scores
#})

#print(df)
#print("Math Scores: ", df['Math Scores'])
#print("Sorted by Maths: ", df.sort_values(by='Math Scores'))
#print("Rows 5 - 10: ", df.loc[5:10])
#print("Rows 5-10, Only Math and English: ", df.loc[5:10,['Math Scores','English Scores']])
#print(".loc version: ", df.iloc[5:10,1:3])

#print(df[df['Math Scores']>75])

#print(df[(df['Math Scores']>75) & (df['English Scores']<60)])

#df['Total'] = df['Math Scores'] + df['English Scores'] + df['History Scores']

#df.drop(columns='Total', inplace=True)
#print(df)

#data = {
#    'A': [1,2, np.nan, 4, 5],
#    'B': [np.nan, 2,3,4,5],
#    'C':[1,2,3, np.nan, np.nan]
#}

#df =pd.DataFrame(data)
#print(df.isna())

#df_dropped = df.dropna()
#print(df_dropped)

#df_dropped_col = df.dropna(axis=1)
#print(df_dropped_col)

#df_filled = df.fillna(0)
#print(df_filled)

#df= pd.concat([df,df.iloc[2]])
#print(df)

#df_no_duplications = df.drop_duplicates()
#print(df_no_duplications)

# map()

#def categorize(value):
#    if pd.isna(value):
#        return 'Missing'
#    elif value <3:
#        return 'Low'
#    else:
#        return 'High'
#df['B'] = df['B'].map(categorize)
#print(df)

data = {
    'School': ['A','B','A','B','A','B','A','B'],
    'Student ID':[1001,1002,1003,1004,1005,1006,1007,1008],
    'Math': np.random.randint(60,100,8),
    'English': np.random.randint(70,100,8),
    'History': np.random.randint(50,100,8)
}

df=pd.DataFrame(data)
print(df)

grouped = df.groupby('School')
#print('Mean scoresby school: ')
#print(grouped.mean())

agg_data = grouped.agg({
    'Math':['mean','median','std'],
    'English':['mean','max'],
    'History':['min','max']
})   
print(agg_data)

df['Class']=['X','X','Y','Y','X','Y','Y','X']
grouped_multi = df.groupby(['School','Class'])
#print(grouped_multi.mean())
