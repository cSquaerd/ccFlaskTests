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

base = fl.Flask(__name__)
base.add_url_rule('/', "index", foo)
base.add_url_rule("/hello/<name>/", "name", bar)
base.add_url_rule("/brython/", "brython", brython)
base.add_url_rule("/dice/", "dice", dice)
base.add_url_rule(
	"/ajax/", "ajaxTest", lambda : fl.render_template("ajaxTest.html")
)
base.add_url_rule("/ajax/post", "ajaxPost", ajaxPost, methods = ["POST"])

if __name__ == "__main__":
	base.run(debug = True)
