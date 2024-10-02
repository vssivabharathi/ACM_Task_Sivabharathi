#  Builded a  Regressor from Scratch and Compare it with Standard Libraries

1. Data Selection
House_Rent_dataset taken from Kaggle website

2. Preprocessing:
- normalizing the data  
```X_normalized = (X - X_mean) / X_std```
- splitting the data in 80:20 ratio where 80% train and 20% is test

3. Building Regression
- build the Linear regression with the learning rate of 0.01 and 1000 iterations
- selecting the features ```Size, Rent```
 
4. Standard Libraries
- here i used the Sklearn's Linear Regression
5. Comparison of Results
- with my own linear Regression model ```Mean Squared Error: 2720809986.299927```
- with sklearn linear regression model ```Mean Squared Error (sklearn): 2720800316.247958```
