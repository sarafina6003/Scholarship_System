from flask import Flask, render_template, flash, session, redirect, url_for, make_response
from app_forms import MyForm, LoginForm, AddForm
from user_model import User, Product
from flask_bcrypt import generate_password_hash, check_password_hash
from peewee import OperationalError, IntegrityError

app = Flask(__name__)
app.secret_key = "starry_6003_serafynurh"


@app.route('/', methods=("GET", "POST"))
def index():
    form = MyForm()
    if form.validate_on_submit():
        # everything is okay
        names = form.names.data
        email = form.email.data
        age = form.age.data
        password = form.password.data
        print("Names {0} Email {1} Age {2}".format(names, email, age))
        password = generate_password_hash(password)
        try:
            User.create(names=names, email=email, age=age, password=password)
            flash("User was registered successfully")
        except IntegrityError:
            flash("User by {0} exists".format(email))

    return render_template("index.html", form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = User.get(User.email == email)
            check = check_password_hash(user.password, password)
            print(check)
            if check:
                print("Logged in successfully!")
                # return render_template("add_products.html",user=user)
                session["names"] = user.names
                session["id"] = user.id
                return redirect(url_for("add_products"))
            else:
                flash("Wrong username or password")
        except Exception:
            print("User does not exist")
            flash("Please create an account first!")
    return render_template("login.html", form=form)


@app.route("/add_products", methods=("GET", "POST"))
def add_products():
    form = AddForm()
    if form.validate_on_submit():
        # everything is okay
        name = form.name.data
        sat = form.sat.data
        date = form.date.data
        owner= session["id"]
    #print("Name {0} sat {1} date {2} ".format(names,sat,date))

        try:
           Product.create(name=name, sat=sat, date=date, owner=owner)
           flash("SAT was saved successfully")
        except IntegrityError:
           flash("Unable to save")
    return render_template("add_products.html", names=session["names"], form=form)

    # if "names" not in session:
    # return redirect(url_for("login"))
    # else:
    # return render_template("add_products.html", names =session["names"])


@app.route("/view_products", methods=("GET", "POST"))
def view_products():
    if "names" not in session:
        return redirect(url_for("login"))
    else:
        owner = session["id"]
        product = Product.select().where(Product.owner==owner)
        return render_template("view_products.html", names=session["names"], product=product)

@app.route("/delete/<int:id>")
def delete(id):
    del_product = Product.get(Product.id==id)
    del_product.delete_instance()
    return make_response (view_products())

@app.route("/logout")
def logout():
    session.pop("names")
    session.pop("id")
    return redirect(url_for("login"))


if __name__ == '__main__':
    # User.drop_table()
    try:
        Product.create_table()
    except OperationalError:
        pass

    try:
        User.create_table()
    except OperationalError:
        pass
    app.run(host="0.0.0.0", port=9999)

    # my ip address=192.168.89.187
    # walt's ip =http://192.168.89.227:8000
    # running my app =192.168.89.187:9999
