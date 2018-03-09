import pandas as pd
import numpy as np
path="C:/Users/JUIN/Desktop/python data processing/automobile.csv" #u can use url keyword instead of path if you want to refer online file
df=pd.read_csv(path,header=None) #to read the csv file without header
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers #added headers to dataframe
print(df.dtypes) # to check the data type of data in dataframe
print(df.describe()) #to return statistical summary
print(df.describe(include="all")) # return all value including na value also

df.dropna(subset=['price'],axis=0,inplace=True) #to drop missing values
df['price']=pd.to_numeric(df['price'],errors="coerce")
mean=df['price'].mean()
df=df['price'].replace(np.nan,mean)
print(df)

df['normalized-losses']=pd.to_numeric(df['normalized-losses'],errors="coerce") #to ignore the errors
mean=df['normalized-losses'].mean()
df['normalized-losses'].replace(np.any,mean)
print(df['normalized-losses'])
df["city-mpg"]=235/df["city-mpg"] # to convert mpg to km
df.rename(columns={"city-mpg":"city-L/100km"},inplace=True) #rename the column
print(df)
df["price"]=df["price"].astype("int") #convert data type
df["length"]=df["length"]/df["length"].max() #scaling data method
df["length"]=(df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())  #min max method
df["length"]=(df["length"]-df["length"].mean())/df["length"].std()  #z scores or standard deviation method

binwidth=int((max(df["price"])-min(df["price"]))/3)  # to binning the data
bins=range(min(df["price"]),max(df["price"]),binwidth)
group_names=['Low','Medium','High']
df['price-binned']=pd.cut(df['price'],bins,labels=group_names)
print(df)

df['fuel-type']=pd.get_dummies(df['fuel-type'])  #converting the categorical type of data to numerical data
print(df)
