import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier  
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score


#Reading Csv File
loan_approval=pd.read_csv('Encoding techniques\Assessments\loan_approval_dataset.csv', header=0)

#Analyzing the dataframe
print(loan_approval.head(10))
print(loan_approval.dtypes)
print(loan_approval.columns)
print(loan_approval.isnull().sum())

#Seperating input columns and output columns
X=loan_approval.drop(" loan_status",axis=1)
Y=loan_approval[" loan_status"]

print(X.head())
print(Y.head())

#Applying encdoing only on output column
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)


#Spliting the dataframe into the train and test size for both inputs and outputs
X_train, X_Test, Y_train, Y_test=train_test_split(X, Y, train_size=0.8, random_state=23)

#Apply Standard scalar and encoding on categorical columns using column transfer
numerical_cols = loan_approval.select_dtypes(include=['int64']).columns
one_hot_columns=[" education",' self_employed']

Scale_and_encode=ColumnTransformer(transformers=[
    ('scaling', StandardScaler(), numerical_cols),
    ("one_hot_encoding", OneHotEncoder(sparse_output=False), one_hot_columns)
])

# now using pipelining
Model1=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", LogisticRegression())
])
Model2=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", RandomForestClassifier())
])
Model3=Pipeline(steps=[
    ("preprocessed_data", Scale_and_encode),
    ("model", GradientBoostingClassifier())
])

#Training model on train data and predicting values
Model1.fit(X_train, Y_train)
Pred_logistic=Model1.predict(X_Test)

Model2.fit(X_train, Y_train)
pred_random_forest=Model2.predict(X_Test)

Model3.fit(X_train, Y_train)
Pred_Gradient=Model3.predict(X_Test)

#Applying matrices for results
#classification report
print("Classification report for logistic regression")
print(classification_report(Y_test, Pred_logistic))

print("Classification report for Random forest classfier")
print(classification_report(Y_test, pred_random_forest))

print("Classification report for gradient booster classifier")
print(classification_report(Y_test, Pred_Gradient))

#precision score
print("precision score for logistic regression")
print(precision_score(Y_test, Pred_logistic))

print("precision score for Random forest classfier")
print(precision_score(Y_test, pred_random_forest))

print("precision score for gradient booster classifier")
print(precision_score(Y_test, Pred_Gradient))

#recall_score
print("recall_score for logistic regression")
print(recall_score(Y_test, Pred_logistic))

print("recall_score for Random forest classfier")
print(recall_score(Y_test, pred_random_forest))

print("recall_score for gradient booster classifier")
print(recall_score(Y_test, Pred_Gradient))

#f1_score
print("f1_score for logistic regression")
print(f1_score(Y_test, Pred_logistic))

print("f1-score for Random forest classfier")
print(f1_score(Y_test, pred_random_forest))

print("f1-score for gradient booster classifier")
print(f1_score(Y_test, Pred_Gradient))
