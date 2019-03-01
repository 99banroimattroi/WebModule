from flask import Flask,redirect
app = Flask(__name__)

@app.route('/about-me')

def about_me():
  return '<meta charset="UTF-8"> <h1> ABOUT ME </h1> <h1>Chào các bạn, tôi là Trịnh Đình Hùng, tác giả của website này. Tôi là một full-stack developer, gamer và đủ thứ lơ tơ mơ khác nữa. Nếu các bạn muốn theo dõi tôi trên Facebook hãy truy cập theo mục dẫn phía dưới !</h1> <a href="https://www.facebook.com/thanhthai.uy" target="#">Bấm vào đây để xem trang Facebook</a>  <h2>Name: Trinh Dinh Hung</h2> <h2>Work : Student</h2> <h2>School: Hanoi University of Business and Technology - HUBT</h2> <h2>Hobbies: Watch movie, Traveling, ...</h2> <h4>Bạn có thể xem một hình ảnh có mặt tôi ở lớp C4E26 ở Techkisd nè</h4> <img src="https://scontent.fhan2-3.fna.fbcdn.net/v/t1.0-9/51409969_494853614374559_6245693226540335104_o.jpg?_nc_cat=108&_nc_oc=AQkbAg8lxVamgbXIr9p3uvYJcK7cS_6n9nzKEp_4q-X1h3ct62vsSjLome36S7Hn8TY&_nc_ht=scontent.fhan2-3.fna&oh=eda57b949cabc333e9acf128f786c092&oe=5CE6A0F1" alt="This is me">'
  
@app.route('/school')

def school_me():
  return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)