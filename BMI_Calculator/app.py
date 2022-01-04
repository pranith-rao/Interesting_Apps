from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    bmi =''
    if request.method == 'POST' and 'weight' in request.form:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        bmi = bmi_calci(weight,height)
    return render_template("index.html",bmi=bmi) 

def bmi_calci(weight,height):
    return round((weight/((height/100) ** 2)),2)


app.run()
