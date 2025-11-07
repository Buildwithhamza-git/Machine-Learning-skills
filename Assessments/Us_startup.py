import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor  
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

#Reading Csv File
Startup=pd.read_csv('Encoding techniques/Assessments/startup_valuation_data.csv', header=0)

#Analyzing the dataframe
print(Startup.head(10))
print(Startup.dtypes)
print(Startup.columns)
print(Startup.isnull().sum())
Startup.columns = Startup.columns.str.strip()

#Seperating input columns and output columns
X=Startup.drop("Valuation (USD)",axis=1)
Y=Startup["Valuation (USD)"]

print(X.head())
print(Y.head())

#Spliting the dataframe into the train and test size for both inputs and outputs
X_train, X_Test, Y_train, Y_test=train_test_split(X, Y, train_size=0.8, random_state=23)

#Apply Standard scalar and encoding on categorical columns using column transfer
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
one_hot_columns=["State or Location","Industry"]

Scale_and_encode=ColumnTransformer(transformers=[
    ('scaling', StandardScaler(), numerical_cols),
    ("one_hot_encoding", OneHotEncoder(sparse_output=False), one_hot_columns)
])

# now using pipelining
Model1=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", LinearRegression())
])
Model2=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", RandomForestRegressor())
])
Model3=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", GradientBoostingRegressor())
])

#Training model on train data and predicting values
Model1.fit(X_train, Y_train)
Pred_linear=Model1.predict(X_Test)

Model2.fit(X_train, Y_train)
pred_random_forest=Model2.predict(X_Test)

Model3.fit(X_train, Y_train)
Pred_Gradient=Model3.predict(X_Test)

#Applying matrices for results
#Metrices for r2_score
print("metrices of r2_score")
print("r2_score for linear regression:")
print(r2_score(Y_test, Pred_linear))

print("r2_score for Random forest regressor:")
print(r2_score(Y_test, pred_random_forest))

print("r2_score for gradient booster regressor:")
print(r2_score(Y_test, Pred_Gradient))

#Metrices for mean_absolute_error
print('matrices of mean_absolute_error')
print("mean_absolute_error for linear regression:")
print(mean_absolute_error(Y_test, Pred_linear))

print("mean_absolute_error for Random forest regressor:")
print(mean_absolute_error(Y_test, pred_random_forest))

print("mean_absolute_error for gradient booster regressor:")
print(mean_absolute_error(Y_test, Pred_Gradient))

#Metrices for root_mean_squared_error
print("root_mean_squared_error for linear regression:")
print(root_mean_squared_error(Y_test, Pred_linear))

print("root_mean_squared_error for Random forest regressor:")
print(root_mean_squared_error(Y_test, pred_random_forest))

print("root_mean_squared_error for gradient booster regressor:")
print(root_mean_squared_error(Y_test,Pred_Gradient))
