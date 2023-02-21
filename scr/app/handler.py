import pickle
import pandas as pd
from flask import Flask, request, Response, render_template
from preprocessing.Preprocessing import Preprocessing  
import os
import lightgbm


# Loading Model Local
model = pickle.load(open('/Users/Alysson/Documents/Projects/Heal-Insurance-Classification/models/model_lgbm_tunned.pkl', 'rb'))

# Loading Model Cloud
# model = pickle.load(open('models/model_xgb_tunned.pkl', 'rb')) # handler cloud

# initialize API
app = Flask( __name__ )

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()
    if test_json: #there is data
        if isinstance(test_json, dict): #unique row 
            test_raw = pd.DataFrame(test_json, index = [0])
        else: # multiple rows
            test_raw = pd.DataFrame(test_json, columns = test_json[0].keys()) 
                   
        
        pipeline = Preprocessing() 
        test_prep = pipeline.data_preparation( test_raw )#
        df_response = pipeline.get_prediction( model, test_raw, test_prep )
        #df_response = test_prep.get_prediction( model, test_raw, test_prep )

        return df_response#.to_json( orient='records', date_format='iso' )
         
    else:
        Response('{}', status = 200, mimetype = 'application/json')    


        
if __name__=="__main__":
    app.run(debug=True)
    #port = os.environ.get('PORT',5000)
    #app.run('0.0.0.0',port=port)
    #app.run('127.0.0.1')#ssh -R 80:localhost:8080 nokey@localhost.run