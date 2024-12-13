from flask import Flask, jsonify,request
import config
from CC_Fraud_Detection.utils import CcFraudDetection
app = Flask(__name__)

## installation
# pip install pandas
# pip install Flask
# pip install scikit-learn

@app.route("/")
def get_home():
    return "Credit Card Fraud Detection"

@app.route("/predict_result",methods = ["POST","GET"])
def get_result():
    if request.method == "POST":
        data = request.form
        merchant = data["merchant"]
        amt = float(data["amt"])
        city = data["city"]
        year = int(data["year"])
        month = int(data["month"])
        day = int(data["day"])
        hour = int(data["hour"])
        minute = int(data["minute"])
        age = int(data["age"])
        category = data["category"]
        state = data["state"]
        job = data["job"]
        


        obj = CcFraudDetection(merchant,amt,city,year,month,day,hour,minute,age,category,state,job)
        result = obj.get_result()

        return jsonify({"Result" : f"Credit Card Fraud Prediction is {result}"})
    

if __name__ == "__main__":
    app.run()