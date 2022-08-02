from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.db.db_manager import DBManager
from werkzeug.utils import secure_filename
from datetime import datetime
import os

# create_user blueprint definition
Create_user = Blueprint(
    "Create_user",
    __name__,
    static_folder="static",
    static_url_path="/CreateUser",
    template_folder="templates",
)


basdir = os.path.abspath(os.path.dirname(__file__))
Upload_dir = basdir + "/static/media/"


# Routes
@Create_user.route("/CreateUser", methods=["GET", "POST"])
def CreateUser_page():

    if request.method == "POST":
        # username,gender,email,password,dob,phone,image,city
        username = request.form["username"]
        gender = request.form["gender"]
        email = request.form["email"]
        password = request.form["password"]
        dob = request.form["dob"]
        phone = request.form["phone"]
        image = request.files["image"]
        city = request.form["city"]

        print(image)
        filename = secure_filename(image.filename)
        # query = """INSERT INTO users VALUES ()"""
        query = """INSERT INTO users 
        (USER_NAME,EMAIL,GENDER,PASSWORD,DATE_BIRTH,PHONE_NUMBER,U_IMAGE_SRC,CITY)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        image.save(os.path.join(Upload_dir, filename))


        args = (
            username,
            email,
            gender,
            password,
            dob,
            phone,
            filename,
            city,
        )
        data = DBManager.commit(DBManager, query, args)
        user_query = """SELECT * FROM users WHERE USER_ID =%s"""
        user_args = (data,)
        data2 = DBManager.fetch(DBManager, user_query, user_args)
        flash(f"{username}'s Account Created Successfully!",'success')
        return redirect("/")
    return render_template("Create_User.html")


@Create_user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        passwod = request.form["password"]
        query = """SELECT * FROM users WHERE EMAIL = %s"""
        users_details = DBManager.fetch(DBManager, query, (email,))

        print(users_details)
        if users_details:
            if users_details[0][4] == passwod:
                user = {
                        "USER_ID": users_details[0][0],
                        "USER_NAME": users_details[0][1],
                        "gender": users_details[0][2],
                        "email": users_details[0][3],
                        "password": users_details[0][4],
                        "dob": users_details[0][5],
                        "phone": users_details[0][6],
                        "image": users_details[0][7],
                        "city": users_details[0][8]
                }
                session["user"] = user
                flash(f"Wellcome {users_details[0][1]}!",'success')
                return redirect("/")
            else:
                flash("Incorrect Password/Email", 'danger')
                return redirect("/")
        else:
            flash("Incorrent Password/Email",'danger')
            return redirect("/")
        return redirect("/")




@Create_user.route("/contact_us", methods=["POST"])
def contact_us():
    # name,email,message,image
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    image = request.files["image"]

    filename = secure_filename(image.filename)

    query = """INSERT INTO contact_us (NAME,EMAIL,TIME_UPLOADED,TEXT,IMAGE_SRC) VALUES (%s,%s,%s,%s,%s)"""
    args = (name, email, datetime.now(), message, filename)

    DBManager.commit(DBManager, query, args)

    image.save(os.path.join(Upload_dir, filename))

    flash("We got Your Message! Thanks", 'success')
    return redirect("/")


@Create_user.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    flash("Logged out", 'warning')
    return redirect("/")
