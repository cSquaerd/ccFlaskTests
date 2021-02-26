from browser import document, ajax, window

def redirect(reply):
	if reply.status == 200:
		window.location.href = reply.text

def login(event):
	user = document["user"].value
	if len(user) > 0:
		ajax.post(
			"/login/",
			data = {"user" : user},
			oncomplete = redirect
		)
	else:
		document["error"].innerHTML = "You need to enter something!"

document["login"].bind("click", login)
