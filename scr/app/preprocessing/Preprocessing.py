import pandas as pd
import numpy as np
#from sklearn.preprocessing import MinMaxScaler
import pickle

class Preprocessing(object):
    def __init__(self):        
        #self.home_path=''
        self.home_path='/Users/Alysson/Documents/Projects/Heal-Insurance-Classification/'#local

        self.age                    = pickle.load( open( self.home_path + 'scr/app/features/age.pkl', 'rb'))
        self.annual_premium         = pickle.load( open( self.home_path + 'scr/app/features/annual_premium.pkl', 'rb'))
        self.driving_license        = pickle.load( open( self.home_path + 'scr/app/features/driving_license.pkl', 'rb'))
        self.gender                 = pickle.load( open( self.home_path + 'scr/app/features/gender.pkl', 'rb'))
        self.policy_sales_channel   = pickle.load( open( self.home_path + 'scr/app/features/policy_sales_channel.pkl', 'rb'))
        self.previously_insured     = pickle.load( open( self.home_path + 'scr/app/features/previously_insured.pkl', 'rb'))
        self.region_code            = pickle.load( open( self.home_path + 'scr/app/features/region_code.pkl', 'rb'))
        self.vehicle_age            = pickle.load( open( self.home_path + 'scr/app/features/vehicle_age.pkl', 'rb'))
        self.vehicle_damage         = pickle.load( open( self.home_path + 'scr/app/features/vehicle_damage.pkl', 'rb'))

    
    def data_preparation(self, data):

        data["gender"] = [0 if i == 'Female' else 1 for i in data["gender"]]
        data["vehicle_damage"] = [0 if i == 'No' else 1 for i in data["vehicle_damage"]]
        data['vehicle_age'] = data['vehicle_age'].apply(lambda x: 0 if x == '< 1 Year' else 1 if x == '1-2 Year' else 3) 



        data['age'] = self.age.fit_transform( data[['age']].values )
        data['annual_premium'] = self.annual_premium.fit_transform( data[['annual_premium']].values )
        data['driving_license'] = self.driving_license.fit_transform( data[['driving_license']].values )
        data['gender'] = self.gender.fit_transform( data[['gender']].values )
        data['policy_sales_channel'] = self.policy_sales_channel.fit_transform( data[['policy_sales_channel']].values )
        data['previously_insured'] = self.previously_insured.fit_transform( data[['previously_insured']].values )
        data['region_code'] = self.region_code.fit_transform( data[['region_code']].values )
        data['vehicle_age'] = self.vehicle_age.fit_transform( data[['vehicle_age']].values )
        data['vehicle_damage'] = self.vehicle_damage.fit_transform( data[['vehicle_damage']].values )        
        

        selected_features = [#'id',
                     'age',
                     'gender',   
                     'region_code',
                     'policy_sales_channel',
                     'driving_license',
                     'vehicle_age',                    
                     'vehicle_damage',
                     'previously_insured',
                     'annual_premium',
                     #'vintage'
                    ]
        
        # log_columns = data[selected_features].skew().sort_values(ascending=False)
        # log_columns = log_columns.loc[log_columns > 0.75]    
    
        # # Log Transformations
        # for col in log_columns.index:
        #     data[col] = np.log1p(data[col])
    
        #Scaling
        #mms = MinMaxScaler()
        #for col in data[selected_features]:
        #    data[col] = mms.fit_transform(data[[col]]).squeeze()


        return data[selected_features]           



    def get_prediction( self, model, test_raw, test_prep ):
        #prediction
        y_pred = model.predict_proba( test_prep )
        y_pred = y_pred[:, 1]
        #retorna o dataset recebido, com a coluna prediction preenchida
        test_raw['prediction'] =  y_pred
        
        return test_raw.to_json( orient='records', date_format='iso' )
    

# data_raw = pd.read_csv('/Users/Alysson/Documents/Projects/Heal-Insurance-Classification/data/train_raw.csv', index_col=0)
# data_raw.shape    