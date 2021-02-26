from browser import document, ajax

def login(event):
	user = document["user"].value
	if len(user) > 0:
		ajax.post("/login/", data = {"user" : user})
	else:
		document["error"].innerHTML = "You need to enter something!"

document["login"].bind("click", login)
