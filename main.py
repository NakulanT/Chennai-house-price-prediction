import pandas as pd
import pickle
from sklearn.ensemble import GradientBoostingRegressor

with open('model.pkl', 'rb') as model_file:
     model = pickle.load(model_file)

def predict(area , int_sqft , dist_mainroad , n_bedroom , n_bathroom , n_room ,park_facil) :
    data_row = [area,int_sqft,dist_mainroad,n_bedroom,n_bathroom,n_room,park_facil]
    columns = ['AREA', 'INT_SQFT', 'DIST_MAINROAD', 'N_BEDROOM', 'N_BATHROOM', 'N_ROOM', 'PARK_FACIL']
    test = pd.DataFrame([data_row], columns=columns)
    result = model.predict(test)
    print(type(result),result)
    return result[0]
    return 0