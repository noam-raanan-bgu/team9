
from flask import Blueprint, render_template, redirect, url_for, request, session, flash

# from requests import session
from utilities.db.db_manager import DBManager
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# marketPlace blueprint definition
MarketPlace = Blueprint(
    "MarketPlace",
    __name__,
    static_folder="static",
    static_url_path="/MarketPlace",
    template_folder="templates",
)


basdir = os.path.abspath(os.path.dirname(__file__))
Upload_dir = basdir + "/static/media/"

# Routes
@MarketPlace.route("/MarketPlace", methods=["GET", "POST"])
def MarketPlace_page():
    try:
        user = session["user"]
        err = ""
        query_post = """SELECT * FROM products WHERE USER_ID =%s"""
        post_args = (user["USER_ID"],)
        post_fetch = DBManager.fetch(DBManager, query_post, post_args)
        if not post_fetch:
            err = "Please login to see all your posts"
        print(post_fetch)
    except:
        flash("Please login to see the MarketPlace", "warning")
        return redirect("/")

    # query = """SELECT * FROM products"""
    query2 = """SELECT products.NAME, products.CATEGORY_ID,products.TIME_UPLOADED,products.FREE,
    products.PRICE, products.DESCRIPTION, products.IMAGE_SRC,
    users.USER_NAME, users.EMAIL,users.PHONE_NUMBER, users.CITY,products.PRODUCT_ID,users.U_IMAGE_SRC
    FROM products
    JOIN users on products.USER_ID = users.USER_ID
    WHERE products.CATEGORY_ID = 1"""

    query3 = """SELECT products.NAME, products.CATEGORY_ID,products.TIME_UPLOADED,products.FREE,
    products.PRICE, products.DESCRIPTION, products.IMAGE_SRC, 
    users.USER_NAME, users.EMAIL,users.PHONE_NUMBER, users.CITY,products.PRODUCT_ID,users.U_IMAGE_SRC
    FROM products
    RIGHT JOIN users on products.USER_ID = users.USER_ID
    WHERE products.CATEGORY_ID = 2"""

    query4 = """SELECT products.NAME, products.CATEGORY_ID,products.TIME_UPLOADED,products.FREE,
    products.PRICE, products.DESCRIPTION, products.IMAGE_SRC, 
    users.USER_NAME, users.EMAIL,users.PHONE_NUMBER, users.CITY,products.PRODUCT_ID,users.U_IMAGE_SRC
    FROM products
    JOIN users on products.USER_ID = users.USER_ID
     WHERE products.CATEGORY_ID = 3"""

    market_data = DBManager.fetch(DBManager, query2)

    accessories_query = DBManager.fetch(DBManager, query3)

    training = DBManager.fetch(DBManager, query4)

    # market_data = DBManager.fetch(DBManager,query)
    if request.method == "POST":
        try:
            user = session["user"]
            print(user)
        except:
            flash("Please Login to Perform this action", "warning")
            return redirect("/")

        image = request.files["image"]
        title = request.form["title"]
        category = request.form["category"]
        isfree = request.form["isfree"]
        notfree = request.form["isfree"]
        try:
            price = request.form["price"]
        except:
            price = 0
        description = request.form["description"]

        filename = secure_filename(image.filename)
        image.save(os.path.join(Upload_dir, filename))
        query = """INSERT INTO products
        (USER_ID,NAME,CATEGORY_ID,TIME_UPLOADED,FREE,PRICE,DESCRIPTION,IMAGE_SRC)
        VALUES (%s, %s, %s, %s,%s,%s,%s ,%s)"""

        args = (
            user["USER_ID"],
            title,
            category,
            datetime.now(),
            isfree,
            price,
            description,
            filename,
        )
        data = DBManager.commit(DBManager, query, args)
        flash("Post Created Successfully!", 'success')
        return redirect("/MarketPlace")

    return render_template(
        "MarketPlace.html",
        market_data=market_data,
        now=datetime.now(),
        accessories_query=accessories_query,
        training=training,
        err=err,
        post_fetch=post_fetch,
        user=user,
    )


@MarketPlace.route("/delete_post/<id>")
def delete_post(id):
    query = """DELETE FROM products WHERE products.PRODUCT_ID =%s"""
    args = (id,)

    DBManager.commit(DBManager,query,args)
    flash("Post Deleted Successfully!", 'success')
    return redirect("/MarketPlace")