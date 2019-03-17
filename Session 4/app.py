from flask import Flask,render_template, request
import food

app = Flask(__name__)

@app.route('/food_list')
def food_list():
    #get all food   1.function ? 2. write function ?
    all_food = food.get({})
    #render: food+ html
    # return str(items)
    return render_template("food_list.html", f_list = all_food)


@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    # return f["Name"]
    return render_template("food_detail.html", food = f)


@app.route("/add_food", methods =["GET","POST"])
def add_food():
    if request.method == "GET": 
        return render_template("food_form.html", methods=["GET","POST"])
    elif request.method == "POST":
        form = request.form
        n = form["Name"]
        p = form["Price"]
        new_item = {
            "Name": n,
            "Price": p 
        }
        items.append(new_item)
        return "Đã thêm " + n + " thành công"

        
if __name__ == '__main__':
  app.run(debug=True)



