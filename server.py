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
    user_id = User.save(request.form)
    return redirect(f'/user/show/{user_id}')

@app.route('/users/show/<int:user_id>')
def show(user_id):
    user = User.get_one(user_id)
    print(user.first_name)
    return render_template('show_user.html', user=user)

@app.route('/users/update/<int:user_id>')
def update(user_id):
    user = User.get_one(user_id)
    return render_template('update.html', user=user)

@app.route('/users/update/process/<int:user_id>', methods=['POST'])
def process_update(user_id):
    User.update_user(request.form, id=user_id)
    return redirect('/users/show_all')

@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    User.delete_user(user_id)
    return redirect('/users/show_all')

if __name__ == "__main__":
    app.run(debug=True)

