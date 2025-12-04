import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


File_path = "used_cars_data.csv"
Used_car = pd.read_csv(File_path,usecols=(1,2,3,4,5,6,7,8,9))
print(Used_car)

print("info of the dataset: ")
print(Used_car.info())
print("Cols names in dataset: ")
print(Used_car.columns)
print("Describtion of the dataset: ")
print(Used_car.describe())
print("check missing values in the dataset: ")
print(Used_car.isna().sum())

sns.lineplot(data=Used_car, x='mileage (kms)', y='price (eur)')
plt.show()


#Extract engine size and horse power from engine text example --> SC 1.2 TSI 90cv Style
Used_car['Engine_Size'] = Used_car['engine'].str.extract(r"(\d\.\d)").astype(float)
Used_car['Horsepower'] = Used_car['engine'].str.extract(r"(\d+)\s?cv").astype(float)


#Filling missing values of engine size and horsepower
Used_car["Engine_Size"] = Used_car["Engine_Size"].fillna(Used_car["Engine_Size"].median())
Used_car["Horsepower"] = Used_car["Horsepower"].fillna(Used_car["Horsepower"].median())
Used_car["Horsepower"] = Used_car["Horsepower"].astype(int)
print(Used_car)

# Clean fuel column bcz there is some special characters inside col
Used_car['fuel'] = Used_car['fuel'].str.replace(r'[^\w\s]', '', regex=True).str.title()
Used_car['location'] = Used_car['location'].str.replace(r'[^\w\s]', '', regex=True).str.replace(r'\s*\d+$', '', regex=True).str.title()

print(Used_car)

#split the data into train and test
X = Used_car.drop(["price (eur)","engine"],axis=1)
y = Used_car["price (eur)"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.15,random_state=42)
print("Train size of X train and X test")
print(f"Train size: {round(len(X_train) / len(X) * 100)}% \n\
Test size: {round(len(X_test) / len(X) * 100)}%")

enc_cols = ["brand","model","fuel","gearbox","location"]
scaling_cols = ["mileage (kms)","year","Horsepower"]

preprocessor = ColumnTransformer(transformers=[
    ("OHE",OneHotEncoder(sparse_output=False,handle_unknown="ignore"),enc_cols),
    ("scaling",StandardScaler(),scaling_cols)],remainder="passthrough")
Model = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("Alogorithm", RandomForestRegressor(n_estimators=100))
])

Model.fit(X_train,y_train)
y_preds = Model.predict(X_test)

mae = mean_absolute_error(y_test, y_preds)
mse = mean_squared_error(y_test, y_preds)
r2 = r2_score(y_test, y_preds)
print("Model evaluation:")
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

result = pd.DataFrame({"Actual" : y_test, "Predicted" : y_preds})
print(f"Actual vs Predicted: \n{result}")
