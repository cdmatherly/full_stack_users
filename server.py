from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all users
    return render_template("index.html")

@app.route('/users/show_all')
def show_all():
    users = User.get_all()
    return render_template('show_all.html', all_users = users)

@app.route('/users/create')
def create():
    return render_template('create.html')

@app.route('/users/create/process', methods=['POST'])
def process_create():
    User.save(request.form)
    return redirect('/users/show_all')

@app.route('/user/show/<int:user_id>')
def show(user_id):
    user = User.get_one(user_id)
    return render_template('show_user.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)

