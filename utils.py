import pickle
import json
import config
import numpy as np

class CcFraudDetection():
    def __init__(self,merchant,amt,city,year,month,day,hour,minute,age,category,state,job):
        self.merchant = merchant
        self.amt = amt
        self.city = city
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.age = age
        self.category = category
        self.state = state
        self.job = job
        
    def load_model(self):
        ## Read Model 
        with open(config.model_path,"rb") as file:
            self.model = pickle.load(file)
        # read json file
        with open(config.json_path,"r") as file:
            self.json_data = json.load(file)
        # read std scale file
        with open(config.std_scale_path,"rb") as file:
            self.stdscale = pickle.load(file)

    def get_result(self):
        self.load_model() # calling model
        test_array = np.zeros(len(self.json_data["columns"]),dtype=int)
        test_array[0] = self.json_data["label_category"][self.category]
        test_array[1] = self.amt
        test_array[2] = self.json_data["label_state"][self.state]
        test_array[3] = self.year
        test_array[4] = self.month
        test_array[5] = self.day
        test_array[6] = self.hour
        test_array[7] = self.minute
        test_array[8] = self.age
        category_1 = "category_"+ self.category
        category_index = self.json_data["columns"].index(category_1)
        test_array[category_index] = 1
        state_1 = "state_"+ self.state
        state_index = self.json_data["columns"].index(state_1)
        test_array[state_index] = 1
        test_array[36] = self.json_data["label_jobs"][self.job]
        std_array = self.stdscale.transform([test_array])
        predict_result = self.model.predict(std_array)[0]

        return predict_result
    

 


