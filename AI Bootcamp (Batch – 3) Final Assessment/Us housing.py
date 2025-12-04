import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


#Load Dataset
Df=pd.read_csv("US houuse price of 10 states.csv", sep=',')
print(Df)

print(Df.head(10))
print(Df.describe())
print(Df.columns.to_list())
print(Df.isnull().sum())


UsefulColumns=Df[['house_size', 'bed', 'bath', 'price', 'state_name']]
UsefulColumns=pd.DataFrame(UsefulColumns)
print(UsefulColumns.head(10))

#Cleaning 'bed' column
UsefulColumns['bed']=UsefulColumns['bed'].str.replace("bd", "")
UsefulColumns['bed']=UsefulColumns['bed'].str.replace("Studio", "0").astype(float)
UsefulColumns['bed']=UsefulColumns['bed'].fillna(UsefulColumns['bed'].mean()).astype(int)

#Cleaning 'bath' column
UsefulColumns['bath']=UsefulColumns['bath'].str.replace("bd", "")
UsefulColumns['bath']=UsefulColumns['bath'].str.replace("Studio", "0").astype(float)
UsefulColumns['bath']=UsefulColumns['bath'].fillna(UsefulColumns['bath'].mean()).astype(int)
print(UsefulColumns['bath'].isnull().sum())
print(UsefulColumns['bath'].unique())


#Cleaning "price" column
UsefulColumns['price']=UsefulColumns['price'].str.replace("$", '')
UsefulColumns['price']=UsefulColumns['price'].str.replace(",", "").astype(float)
UsefulColumns['price']=UsefulColumns['price'].fillna(UsefulColumns['price'].mode()[0]).astype(int)


# 1. Remove parenthetical text (e.g., '(on 0.25 acres)')
UsefulColumns['house_size'] = UsefulColumns['house_size'].str.replace(r'\s*\(.*\)', '', regex=True)
# 2. Remove 'sqft', commas, and trim any excess whitespace
UsefulColumns['house_size'] = UsefulColumns['house_size'].str.replace('sqft', '', regex=False)
UsefulColumns['house_size'] = UsefulColumns['house_size'].str.replace(',', '', regex=False).str.strip().astype(float)
UsefulColumns['house_size']=UsefulColumns['house_size'].fillna(UsefulColumns['house_size'].median()).astype(int)
print(UsefulColumns['house_size'].head(10))

#Make dataset's csv file after cleaning data
UsefulColumns.to_csv("New.csv")

X=UsefulColumns.drop(['price'], axis=1)
Y=UsefulColumns['price']

sns.lineplot(data=UsefulColumns, x='house_size', y='price')
plt.show()

X_train, X_test, Y_train, Y_test=train_test_split(X, Y, train_size=0.7,random_state=23)

numerical_features = [ "bed", "bath", 'house_size']
encoding=['state_name']
Columns=ColumnTransformer(transformers=[
    ("scale", StandardScaler(), numerical_features),
    ("encode", OneHotEncoder(), encoding)
])

model=Pipeline(steps=[
    ("preprocessor", Columns),
    ("regressor", RandomForestRegressor())
])

model.fit(X_train, Y_train)
pred=model.predict(X_test)


mae = mean_absolute_error(Y_test, pred)
mse = mean_squared_error(Y_test, pred)
r2 = r2_score(Y_test, pred)


print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
