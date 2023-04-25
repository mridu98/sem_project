import pickle
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle


__model = None
model=None

def get_estimated_Quality(DO,BOD,totalCaliform,fecalCaliform):

    pridictData=[DO,BOD,totalCaliform,fecalCaliform]
    with open('model.pkl', 'rb') as file:
     model = pickle.load(file)
       
    df = pd.read_csv('Months (4).csv')
    encoder = LabelEncoder()
    encoder.fit(df['E'])
    encoded_data = encoder.transform(df['E'])
    df['E'] = encoded_data
    df = df.dropna()
    X = df.iloc[:,:-1].values 
    y = df.iloc[:,-1].values
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
   
   
   
    y_pred = model.predict(sc.transform([pridictData])) 
    if y_pred == [0]:
      return "B"
    elif y_pred == [1]:
      return "C"
    elif y_pred == [3]:
      return "D"
    elif y_pred == [5]:
      return "E"
    else :
      return "A"
  


def load_saved_artifacts():
    print("loading saved artifacts...start")

        
       

    global model
    if model is None:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(model.predict([[10.42,1.6,920,540]])[0])
    print(get_estimated_Quality(10.0,23.0,700.0,1000.0))
