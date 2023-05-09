from flask import Flask,render_template,request
import pickle
import numpy as np


model = pickle.load(open('heart.pkl','rb')) 

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
#age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	tha
def Heart_disease():
    age  = int(request.form.get('age'))
    sex =int(request.form.get('sex'))
    cp =int(request.form.get('cp'))
    trestbps = int(request.form.get('trestbps'))
    chol = int(request.form.get('chol'))
    fbs = int(request.form.get('fbs'))
    restecg	 = int(request.form.get('restecg'))
    thalach	 = int(request.form.get('thalach'))
    exang = int(request.form.get('exang'))
    oldpeak	 = float(request.form.get('oldpeak'))
    slope	 = int(request.form.get('slope'))
    ca	= int(request.form.get('ca'))
    thal = int(request.form.get('thal'))


   #prediction

result = model.predict(np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1,-1))
if result[0] == 1:
        result = 'patiant has diabites'
else:
        print('patiatant has not diabites')
    
return str(result)



  


if __name__ == '__main__':
    app.run(debug=True)
