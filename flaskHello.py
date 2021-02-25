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

base = fl.Flask(__name__)
base.add_url_rule('/', "index", foo)
base.add_url_rule("/hello/<name>/", "name", bar)
base.add_url_rule("/brython/", "brython", brython)
base.add_url_rule("/dice/", "dice", dice)

if __name__ == "__main__":
	base.run()
