import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Data/flights.csv')
#print(df.head(10))
#print(df.info())
#print(df.isnull().sum())
#print(df.describe().round(2))
#print(df['Origin'].value_counts())
#print(df['Origin'].unique())


#df['Year'] = df['Fly Date'].astype(str).str.slice(0,4,).astype(int)
#flight_in_2000 = df[df['Year']==2000]
#non_lax_flights=df[~df['Origin'].isin(['LAX'])]
#print(non_lax_flights.head())
#print('LAX' in non_lax_flights['Origin'].unique())
#only_lax_flights=df[df['Origin'].isin(['LAX'])]
#print(only_lax_flights['Origin'].unique())

#passenger_and_distance=df[(df['Passengers']>100)&(df['Distance']<1000)]
#print(passenger_and_distance[['Passengers','Distance']])


#la_ny=df[(df['Origin City']).str.contains('New York|Los Angeles')| 
##         (df['Destination City']).str.contains('New York|Los Angeles')]
#
#print(la_ny[['Origin City','Destination City']].head())
#print(la_ny.info())

#large_origin = df[df['Origin Population']>1000000]
#print(large_origin[['Origin Population','Origin City']])\

#underbook= df.query('Seats > Passengers')
#print(underbook[['Seats', 'Passengers']])

#busy_shorthaul=df.query('Distance<500 & Flights >10')
#print(busy_shorthaul[['Distance','Flights']])
#busy_shorthaul.to_csv('shorthaul.csv')


#busiest_routes = df.groupby(['Origin','Destination']).agg({'Passengers':'sum', 'Flights':'sum'})
#busiest_routes = busiest_routes.sort_values(by=['Passengers','Flights'], ascending=[False,False])

#print(busiest_routes.head())

#df['Month']=pd.to_datetime(df['Fly Date'],format='%Y%m').dt.to_period('M')
#monthly_trends = df.groupby('Month').agg({'Flights':'sum'})
#monthly_trends=monthly_trends.sort_values(by='Month')
#print(monthly_trends.head())

#distance_bins = pd.cut(df['Distance'], bins=[0,500,1000,2000,3000,4000, df['Distance'].max()])
#distance_group = df.groupby(distance_bins).agg({'Flights':'sum','Passengers':'sum'})
#print(distance_group.sort_values(by='Distance', ascending=False))


#busiest_airports = df.groupby('Origin').agg({'Flights':'sum'}).nlargest(10,'Flights')
#busiest_airports.plot(kind='bar')
#plt.title('Top 10 Busiest Airports by Outoing Flights')
#plt.xlabel('Airport')
#plt.ylabel('Number of Flights')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

#busiest_routes=df.groupby(['Origin','Destination']).agg({'Passengers':'sum'}).nlargest(10,'Passengers')
#busiest_routes.plot(kind='bar', color='darkblue')
#plt.title('Top 10 Busiest Routes by Number of Passengers')
#plt.xlabel('Route')
#plt.ylabel('Number of Passengers')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()



#df['Year']=df['Fly Date'].astype(str).str.slice(0,4)
#year_groups = df.groupby('Year')
#year_groups.agg({'Flights':'sum'}).plot(kind='line')
#plt.title('Total Number of Flights per Year')
#plt.xlabel('Year')
#plt.ylabel('Flights')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()


#df['Year']=df['Fly Date'].astype(str).str.slice(0,4)
#year_groups = df.groupby('Year')
#year_groups.agg({'Passengers':'sum'}).plot(kind='line')
#plt.title('Total Number of Flights per Year')
#plt.xlabel('Year')
#plt.ylabel('Passengers')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

#distance_bins = pd.cut(df['Distance'], bins=[0,500,1000,2000,3000,4000, df['Distance'].max()])
#distance_groups = df.groupby(distance_bins).agg({'Flights':'sum'})
#distance_groups.plot(kind='pie', y='Flights')
#plt.title('Distribution of Flights by Distance')
#plt.tight_layout()
#plt.show()

#top_50_routes=df.groupby(['Origin City','Destination City']).agg({'Passengers':'sum'}).nlargest(5,'Passengers')
#top_50_routes.plot(kind='pie',y='Passengers')
#plt.title('Distribution of Passengers by Route')
#plt.tight_layout()
#plt.show()

#route_groups = df.groupby(['Origin','Destination']).agg({'Distance':'mean','Passengers':'sum'})
#route_groups.plot(kind='scatter',x='Distance', y='Passengers')
#plt.title('Distance vs Passengers')
#plt.tight_layout()
#plt.show()

#df['Distance'].plot(kind='hist')
#plt.title('Distribution of Distances')
#plt.xlabel('Distance')
#plt.ylabel('Frequency')
#plt.tight_layout()
#plt.show()

df['Total City Population'] = df['Origin Population']+ df['Destination Population']
df['Year']=df['Fly Date'].astype(str).str.slice(0,4)
city_populations = df.groupby(['Origin','Destination','Year']).agg({'Passengers':'sum','Total City Population':'sum'}).sort_values(by='Year')
city_populations.plot(kind='scatter', x='Total City Population', y='Passengers')
plt.title('Number of Passengers by Total City Population')
plt.xlabel('Total City Population')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()