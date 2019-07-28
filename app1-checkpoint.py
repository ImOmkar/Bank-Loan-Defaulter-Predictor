
from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
import time
import pandas as pd
# load the built-in model 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/getdelay', methods=['POST','GET'])
def get_delay():
    result=request.form
    member_id_input=result['member_id_input']
    #print(type(member_id_input))
    member_id_input=int(member_id_input)
    #print(type(member_id_input))
    
    fT=pd.read_csv(r'C:\Users\adity\Example1\example\venv\finalTest_csv.csv')
    user_new_input = fT[(fT['member_id'] == member_id_input)]
    del user_new_input['member_id']
    loan_amnt=user_new_input['loan_amnt']
    int_rate=user_new_input['int_rate']
    annual_inc=user_new_input['annual_inc']
    print('Loading.....')
    time.sleep(5)
    log_model = joblib.load('RF_BLDP.pkl')
    df=pd.DataFrame(data=user_new_input,index=[0])
    prediction=log_model.predict(df)
    if prediction ==1:
       return render_template('result.html')
    if prediction ==0:
       return render_template('result2.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
