from flask import Blueprint, render_template, redirect, url_for, session, flash,jsonify
from utilities.db.db_manager import DBManager

# MyMatches blueprint definition
MyMatches = Blueprint(
    "MyMatches",
    __name__,
    static_folder="static",
    static_url_path="/",
    template_folder="templates",
)


# matches_found = []

def dogs_matches(dog_id, user_id):
    print(user_id)
    query = """SELECT dogs.DOG_TYPE, dogs.DOG_NATURE, dogs.DOG_SIZE,dogs.DOG_NAME from dogs where dogs.USER_ID=%s"""
    args = (user_id,)
    user_dogs = DBManager.fetch(DBManager,query,args)
   
    ## now finding all the matches for dogs

    matches_found = []
    query = "SELECT * from dogs where dogs.DOG_NATURE = %s AND dogs.DOG_SIZE=%s AND dogs.DOG_TYPE=%s"


    for dat in user_dogs:

        args = (
            dat[1],
            dat[2],
            dat[0],
        )
     
        datas = DBManager.fetch(DBManager,query, args)

        for data in datas:
            if data[0] == user_id:
                print("done")
            else:
                founded = {
                    "Match_for":dat[3],
                    "USER_ID":data[0],
                    "DOG_ID":data[1],
                    "DOG_NAME":data[2],
                    "DOG_TYPE":data[3],
                    "DOG_GENDER":data[4],
                    "DOG_SIZE":data[5],
                    "dob":data[6],
                    "DOG_NATURE":data[7],
                    "IMAGE_SRC":data[8]
                }

                matches_found.append(founded)
    return matches_found


# Routes
@MyMatches.route("/MyMatches")
def MyMatches_page():
    try:
        user = session["user"]
    except:
        flash("Please login to see MyMatches", "warning")
        return redirect("/")

    res = dogs_matches(1,user['USER_ID'])

    query = """SELECT * FROM users"""

    users = DBManager.fetch(DBManager,query)



    print("______________________________resutl_____________")
    print(users)
    print()
    print()
    print(res)
    # query = """SELECT dogs.DOG_ID from dogs where USER_ID = %s"""

    # args = (user["USER_ID"],)
    # result = DBManager.fetch(DBManager, query, args)

  
    # final_result = []
    # matche_list = []

    # query333 = """SELECT dogs.IMAGE_SRC, dogs.DOG_NAME,dogs.DOG_GENDER,dogs.DOG_NATURE,dogs.DOG_SIZE,dogs.DOG_TYPE, matches.DOG_1 FROM dogs
    # RIGHT JOIN matches on dogs.DOG_ID = matches.DOG_1

    # where dogs.USER_ID =%s"""
    # args = (user["USER_ID"],)

    # data = DBManager.fetch(DBManager, query333,args)


    # print("____________________________________latest data _____________________________")
    # print(data)

    # for da in range(len(data)):
    #     print(da)
    # for data in result:
    #     query = """SELECT matches.DOG_2 from matches WHERE matches.DOG_1 = %s"""
    #     args = data
    #     r = DBManager.fetch(DBManager, query, args)
    #     for value in r:
    #         matche_list.append(
    #             value,
    #         )
    # matche_list = [t for t in (set(tuple(i) for i in matche_list))]

    # print(matche_list)
    # for data in range(len(matche_list)):
    #     query = """SELECT dogs.IMAGE_SRC, dogs.DOG_NAME,dogs.DOG_GENDER,dogs.DOG_NATURE,dogs.DOG_SIZE,dogs.DOG_TYPE
    #     from dogs
    #     Where dogs.DOG_ID = %s
    #     """
    #     args = tuple(matche_list[data])

    #     res = DBManager.fetch(DBManager, query, args)
     
    #     final_result.append(res[0])

    return render_template("MyMatches.html", user=user, result=res,users = users)
