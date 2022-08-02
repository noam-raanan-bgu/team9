from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile("settings.py")

###### Pages
## jomepage
from pages.homepage.homepage import Homepage

app.register_blueprint(Homepage)

## create_user
from pages.create_user.create_user import Create_user

app.register_blueprint(Create_user)

## marketPlace
from pages.marketPlace.marketPlace import MarketPlace

app.register_blueprint(MarketPlace)


## myMatches
from pages.myMatches.myMatches import MyMatches

app.register_blueprint(MyMatches)

## profile
from pages.profile.profile import profile
app.register_blueprint(profile)

if __name__ == "__main__":
    app.run(debug=True)
