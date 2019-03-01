from flask import Flask
app = Flask(__name__)

#bind route to view function
# @app.route('/add/<int:number1>/<int:number2>')   #route
# def sum(number1,number2):   #view function
#     (sum) = (number1) + (number2)
#     return str(sum)

# @app.route("/hi/<name>")
# def hi_duc():
#     return "Hi " + name


items = ['com','pho xao','bun cha']

@app.route('/menu')
def menu():
    return  str(items)
    
@app.route("/food/<int:i>")
def food(i):
    return items[i]


if __name__ == '__main__':
  app.run(debug=True)   