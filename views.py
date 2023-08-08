from flask import Blueprint , render_template , request , jsonify , redirect , url_for

#saving bluprint variable
views = Blueprint(__name__,"views")


#making home route
@views.route("/")
def home():
    return render_template("base.html", name="Aryan")

#name from the url
@views.route("/deadprofile/<username>")
def deadprofile(username):
    return render_template("profile.html.html", name=username)

#name from query
#eg: /profile?name=joe
@views.route("/profile")
def profile():
    args=request.args
    name = args.get('name')
    return render_template("profile.html", name=name)

#return json
@views.route("/json")
def get_json():
    return jsonify({"name":"aryan" , "try": "always" , "sleep":"never"})

#getting data back
@views.route("/data")
def get_data():
    #access json from root
    data = request.json
    return jsonify(data)

#redirect
@views.route("/redirect-home")
def redirect_home():
    return redirect(url_for("views.home"))

