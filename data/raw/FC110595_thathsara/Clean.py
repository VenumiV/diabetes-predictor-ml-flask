import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier

data = pd.read_csv('../Healthcare-Diabetes.csv')

columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
data[columns_with_zeros] = data[columns_with_zeros].replace(0, pd.NA)

data_cleaned = data.dropna()

X = data_cleaned.drop(columns=['Id', 'Outcome'])
y = data_cleaned['Outcome']

scalar = MinMaxScaler()
X_normalized = scalar.fit_transform(X)

processed_data = pd.DataFrame(X_normalized, columns=X.columns)
processed_data['Outcome'] = y.values

processed_data.to_csv('../../processed/FC110595_thathsara/Healthcare-Diabetes.csv', index=False)

print("Processed data saved as 'processed_diabetes_data.csv'")