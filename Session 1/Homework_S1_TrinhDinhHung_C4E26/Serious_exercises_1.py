from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def calcbmi(weight,height):

    x = 0.01*height
    BMI = weight/(x*x)
    
    if  BMI < 16:
        return("BMI {:.1f} <16: severely underweight").format(BMI)
    elif BMI < 18.5:
        return("16 <= BMI {:.1f}  < 18.5 : Underweight").format(BMI)
    elif BMI < 25:
        return("18.5 <= BMI {:.1f}  < 25 : Normal").format(BMI)
    elif BMI < 30:
        return("25 <= BMI {:.1f}  < 30 : Overweight").format(BMI)
    else:
        return("BMI {:.1f}  > 30 : Obese").format(BMI)

if __name__ == '__main__':
  app.run(debug=True)