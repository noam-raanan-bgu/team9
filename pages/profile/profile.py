from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from settings import DB
from utilities.db.db_manager import DBManager
from datetime import datetime
from pages.create_user.create_user import Upload_dir
from werkzeug.utils import secure_filename
import os

# MyMatches blueprint definition
profile = Blueprint(
    "profile",
    __name__,
    static_folder="static",
    static_url_path="/",
    template_folder="templates",
)


@profile.route("/user_profile")
def user_profile():
    try:
        user = session['user']
    except:
        flash("Please login to access this page", "warning")
        return redirect("/")

    query = """SELECT * FROM dogs WHERE dogs.USER_ID = %s"""
    args = (user['USER_ID'],)
    dogs = DBManager.fetch(DBManager, query, args)
    print(session['user'])
    return render_template("profile.html",
                           user=user,
                           dogs=dogs
                           )


@profile.route("/update_profile", methods=['POST'])
def update_profile():
    try:
        user = session['user']
    except:
        flash("Please login to access this page", "warning")
        return redirect("/")

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    dob = request.form['dob']
    phone = request.form['phone']

    #  query = """INSERT INTO users 
    #     (USER_NAME,EMAIL,PASSWORD,DATE_BIRTH,PHONE_NUMBER,IMAGE_SRC,CITY_ID)
    #     VALUES (%s, %s, %s, %s,%s,%s,%s)"""

    query = "UPDATE users SET USER_NAME=%s, EMAIL=%s, PASSWORD=%s, DATE_BIRTH=%s, PHONE_NUMBER=%s WHERE users.USER_ID=%s"
    args = (name, email, password, dob, phone, user['USER_ID'],)
    try:
        print(query, args)
        DBManager.commit(DBManager, query, args)
        user['USER_NAME'] = name
        user['email'] = email
        user['password'] = password
        user['phone'] = phone
        user['dob'] = dob
        session['user'] = user
    except Exception as e:
        print(e)

    flash("User Details Updated Successfully!", 'success')
    return redirect("/user_profile")
    # <!-- name,email,password,dob,phone -->


@profile.route("/update_dog", methods=["POST"])
def update_dog():
    try:
        user = session["user"]
    except:
        flash("Please login to perform such an action", "warning")
        return redirect("/")
    id = request.form['id']
    name = request.form["name"]
    type = request.form["dog_type"]
    gender = request.form["gender"]
    size = request.form["size"]
    dob = request.form["dob"]
    nature = request.form["nature"]

    dogs = "UPDATE dogs set DOG_NAME=%s, DOG_TYPE=%s,DOG_GENDER=%s,DOG_SIZE=%s,DATE_BIRTH=%s,DOG_NATURE=%s WHERE dogs.DOG_ID=%s"
    argss = (
        name,
        type,
        gender,
        size,
        dob,
        nature,
        id,
    )
    testing = DBManager.commit(DBManager, dogs, argss)

    flash("Dog Details Updated Successfully!", 'success')
    return redirect("/user_profile")


@profile.route("/CreateDog", methods=["GET", "POST"])
def CreateDog():
    if request.method == "POST":

        try:
            user = session["user"]
        except:
            flash("Please login to perform such an action", "warning")
            return redirect("/")

        name = request.form["name"]
        type = request.form["dog_type"]
        gender = request.form["gender"]
        size = request.form["size"]
        dob = request.form["dob"]
        nature = request.form["nature"]
        image = request.files["image"]
        # name,dog_type,gender,size,dob,nature,image
        filename = secure_filename(image.filename)

        dogs = "SELECT * FROM dogs WHERE DOG_SIZE =%s and DOG_NATURE = %s and DOG_TYPE=%s"
        argss = (
            size,
            nature,
            type,

        )
        testing = DBManager.fetch(DBManager, dogs, argss)
        print("__________________________________________________-")
        print(testing)
        query1 = """INSERT INTO dogs
        (USER_ID,DOG_NAME,DOG_TYPE,DOG_GENDER,DOG_SIZE,DATE_BIRTH,DOG_NATURE,IMAGE_SRC)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

        args = (
            user["USER_ID"],
            name,
            type,
            gender,
            size,
            dob,
            nature,
            filename,
        )
        dog_id = DBManager.commit(DBManager, query1, args)

        matches = """INSERT INTO matches (DOG_1,DOG_2,DATE_MATCH) VALUES (%s,%s,%s)"""
        if testing:
            for data in testing:
                matches_args = (
                    dog_id,
                    data[1],
                    datetime.now(),
                )
                DBManager.commit(DBManager, matches, matches_args)

        query2 = """INSERT INTO dog_nature (NAME) VALUES (%s)"""
        args2 = (nature,)
        DBManager.commit(DBManager, query2, args2)

        query3 = """INSERT INTO dog_size (NAME) VALUES(%s)"""
        args3 = (size,)
        DBManager.commit(DBManager, query3, args3)

        query4 = """INSERT INTO dog_type (NAME) VALUES(%s)"""
        args4 = (type,)
        DBManager.commit(DBManager, query4, args4)

        query5 = """INSERT INTO gender (NAME) VALUES(%s)"""
        args5 = (gender,)
        DBManager.commit(DBManager, query5, args5)

        image.save(os.path.join(Upload_dir, filename))
        flash("A new dog has been added successfully!", 'success')
    return redirect("/user_profile")


@profile.route("/delete_dog/<id>")
def delete_dog(id):
    query = "DELETE FROM dogs WHERE DOG_ID=%s"
    args = (id,)
    DBManager.commit(DBManager, query, args)
    flash("Dog Deleted Successfully!", 'success')
    return redirect("/user_profile")
