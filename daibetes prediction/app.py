from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open('modell.pkl','rb'))

app = Flask(__name__)#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict_diabetes():
    Pregnancies  = int(request.form.get('Pregnancies'))
    Glucose =int(request.form.get('Glucose'))
    BloodPressure =int(request.form.get('BloodPressure'))
    SkinThickness = int(request.form.get('SkinThickness'))
    Insulin  = int(request.form.get('Insulin'))
    BMI  = float(request.form.get('BMI'))
    DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
    Age	 = int(request.form.get('Age'))
   #prediction

    result = model.predict(np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8))
    if result[0] == 1:
        result = 'patiant has diabites'
    else:
        print('patiatant has not diabites')
    
    return str(result)
  

if __name__ == '__main__':
    app.run(debug=True)