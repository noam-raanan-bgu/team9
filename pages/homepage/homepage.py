from flask import Blueprint, render_template, redirect, url_for, session

# homepage blueprint definition
Homepage = Blueprint(
    "Homepage",
    __name__,
    static_folder="static",
    static_url_path="/",
    template_folder="templates",
)


# Routes
@Homepage.route("/")
def index():
    try:
        user = session["user"]
    except:
        user = ""
    return render_template("homepage.html", user=user)
