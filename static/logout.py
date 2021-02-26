from browser import document, ajax

def logout(event):
	ajax.get("/logout/")

document["logout"].bind("click", logout)
