from flask import Flask, render_template, request
app = Flask(__name__)

items = [
  {
    "model":"SH150", 
    "daily_fee":100000, 
    "image":"https://hondaxemay.com.vn/wp-content/uploads/2018/12/150i_ABS_Matt-Black.jpg", 
    "time": 2019
  }
]

@app.route('/')
def menu():
    return render_template("menu_bike.html", item_list = items, user = "D.HUNG")

@app.route("/new_bike", methods = ['GET','POST'])
def new_bike():
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        d = form["daily_fee"]
        i = form["image"]
        y = form["time"]
        new_item = {
          "model":m, 
          "daily_fee":d, 
          "image":i, 
          "year":y
        }
        items.append(new_item)
        return "<h1>Đã thêm thành công !</h1>  " + "<h2>Chi tiết:</h2>" + str(items)  

if __name__ == '__main__':
  app.run(debug=True)