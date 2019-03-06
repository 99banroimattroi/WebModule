from flask import Flask,render_template, request

app = Flask(__name__)


items = [
    {
        "name":"Cơm giang",
        "price": 25000,
    }, 
    {
        "name":"Phở bò",
        "price": 30000,
    },
    {
        "name":"Xôi Xéo",
        "price": 10000,
    },
    ]

@app.route('/')
def menu():
    # return str(items)
    return render_template("menu.html", item_list = items, user = "D.HUNG")

@app.route("/food/<int:i>")  #1 => Detail
def food(i):
    f = items[i]
    # return items[i]
    return render_template("food_detail.html", item = f)

@app.route("/add_food", methods =["GET","POST"])
def add_food():
    if request.method == "GET": 
        return render_template("food_form.html", methods=["GET","POST"])
    elif request.method == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        new_item = {
            "name": n,
            "price": p 
        }
        items.append(new_item)
        return "Đã thêm " + n + " thành công"
        # return n + "" + str(p)
        # return "Gui form chu gi, biet roi"
       

if __name__ == '__main__':
  app.run(debug=True)