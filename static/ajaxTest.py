from browser import document, ajax
import json

def setLabel(request):
	if request.status == 200:
		document["result"].innerHTML = request.text
		document["result"].style = {"visibility" : "visible"}
	else:
		print("AJAX Error:", request.status, request.text)
		document["result"].style = {"visibility" : "hidden"}

def squarePress(event):
	number = document["number"].value
	ajax.post(
		"/ajax/post",
		headers = {"Content-Type" : "application/json"},
		data = json.dumps({"number" : number}),
		oncomplete = setLabel
	)

document["square"].bind("click", squarePress)

