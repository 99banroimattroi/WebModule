from flask import Flask
app = Flask(__name__)

@app.route("/user/<name>")
def username(name):
  Users = { 
      "huy":  {
                "Name":"Nguyen Quang Huy", 
                "Age": 29
             },
      "duc":  {
                "Name":"Hoang Huy Duc",
                "Age": 22
             },
      "hung": {
                "Name":"Trinh Dinh Hung",
                "Age": 20
              }
    }
  if name not in Users:
    return "User not found"
  else:
    return str(Users[name])

if __name__ == '__main__':
  app.run(debug=True)