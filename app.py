from flask import Flask, render_template, request,redirect, url_for
import jsonify
import requests
import pickle
import numpy as np
import warnings
import random
warnings.simplefilter('ignore', FutureWarning)
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('credit_card_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Time = int(request.form['Time'])
        Amount=float(request.form['Amount'])
# =============================================================================
#         V1=float(request.form.get('Value'))
#         V2=float(request.form['v2'])
#         V3=float(request.form['v3'])
#         V4=float(request.form['v4'])
#         V5=float(request.form['v5'])
#         V6=float(request.form['v6'])
#         V7=float(request.form['v7'])
#         V8=float(request.form['v8'])
#         V9=float(request.form['v9'])
#         V10=float(request.form['v10'])
#         V11=float(request.form['v11'])
#         V12=float(request.form['v12'])
#         V13=float(request.form['v13'])
#         V14=float(request.form['v14'])
#         V15=float(request.form['v15'])
#         V16=float(request.form['v16'])
#         V17=float(request.form['v17'])
#         V18=float(request.form['v18'])
#         V19=float(request.form['v19'])
#         V20=float(request.form['v20'])
#         V21=float(request.form['v21'])
#         V22=float(request.form['v22'])
#         V23=float(request.form['v23'])
#         V24=float(request.form['v24'])
#         V25=float(request.form['v25'])
#         V26=float(request.form['v26'])
#         V27=float(request.form['v27'])
#         V28=float(request.form['v28'])
# =============================================================================
        V1= random.uniform(-56.40750963, 2.454929991)
        V2= random.uniform(-72.71572756, 22.05772899)
        V3= random.uniform(-48.32558936, 9.382558433)
        V4= random.uniform(-5.683171198, 16.87534403)
        V5= random.uniform(-113.7433067, 34.80166588)
        V6= random.uniform(-26.16050594, 73.30162555)
        V7= random.uniform(-43.55724157, 120.5894939)
        V8= random.uniform(-73.21671846, 20.00720837)
        V9= random.uniform(-13.43406632, 15.59499461)
        V10= random.uniform(-24.58826244, 23.74513612)
        V11= random.uniform(-4.797473465, 12.01891318)
        V12= random.uniform(-18.68371463, 7.848392076)
        V13= random.uniform(-5.791881206, 7.126882959)
        V14= random.uniform(-19.21432549, 10.52676605)
        V15= random.uniform(-4.49894467676621,8.87774159774277)
        V16= random.uniform(-14.1298545174931,17.3151115176278)
        V17= random.uniform(-25.1627993693248,9.25352625047285)
        V18= random.uniform(-9.49874592104677,5.04106918541184)
        V19= random.uniform(-7.21352743017759,5.59197142733558)
        V20= random.uniform(-54.497720494566,39.4209042482199)
        V21= random.uniform(-34.8303821448146,27.2028391573154)
        V22= random.uniform(-10.933143697655,10.5030900899454)
        V23= random.uniform(-44.8077352037913,22.5284116897749)
        V24= random.uniform(-2.83662691870341,4.58454913689817)
        V25= random.uniform(-10.2953970749851,7.51958867870916)
        V26= random.uniform(-2.60455055280817,3.5173456116238)
        V27= random.uniform(-22.5656793207827,31.6121981061363)
        V28= random.uniform(-15.4300839055349,33.8478078188831)
        prediction=model.predict([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
        output=round(prediction[0],2)
        print(output)
        #return render_template('index.html',prediction_text="Your credit card transaction was successful")
        if output==1:
            return render_template('index.html',prediction_texts="Sorry your credit card transaction is predicted fraud")
        else:
            return render_template('index.html',prediction_text="Your credit card transaction was successful")
        #return render_template('index.html')
        print(output)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

