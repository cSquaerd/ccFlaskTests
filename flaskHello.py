import flask as fl

def foo():
	return "<h1>Hello World!</h1>"

def bar(name):
	return "<h2> Hello " + name + "!</h2>"

def brython():
	return fl.render_template("brython.html")

def dice():
	return fl.render_template(
		"diceroll.html",
		dice = ("d4", "d6", "d8", "d10", "d12", "d20")
	)

def ajaxPost():
	if fl.request.method == "POST":
		try:
			x = int(fl.request.form["number"])
		except ValueError:
			return "ValueError: Cannot parse as int"

		return fl.jsonify(x ** 2)

def login():
	if fl.request.method == "GET":
		if "user" in fl.session:
			return fl.render_template("loggedIn.html", user = fl.session["user"])
		else:
			return fl.render_template("login.html")
	elif fl.request.method == "POST":
		fl.session["user"] = fl.request.form["user"]
		return fl.url_for("userpage")

def logout():
	del fl.session["user"]
	return fl.redirect(fl.url_for("login"))

def sessionTest():
	if "user" in fl.session:
		return fl.render_template("userpage.html", user = fl.session["user"])
	else:
		return "<h1>Can I see your passport?</h1>\n" + \
			"<h2>You're not supposed to be in here!</h2>"

base = fl.Flask(__name__)
base.secret_key = b"\x13\xbf\xd0r\xba\xe2<\x0b\xc0{\xa2Tn\x18T\x8c"
base.add_url_rule('/', "index", foo)
base.add_url_rule("/hello/<name>/", "name", bar)
base.add_url_rule("/brython/", "brython", brython)
base.add_url_rule("/dice/", "dice", dice)
base.add_url_rule(
	"/ajax/", "ajaxTest", lambda : fl.render_template("ajaxTest.html")
)
base.add_url_rule("/ajax/post", "ajaxPost", ajaxPost, methods = ["POST"])
base.add_url_rule("/login/", "login", login, methods = ["GET", "POST"])
base.add_url_rule("/logout/", "logout", logout)
base.add_url_rule("/user/", "userpage", sessionTest)

if __name__ == "__main__":
	base.run(debug = True)
