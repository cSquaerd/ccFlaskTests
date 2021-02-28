from browser import document, ajax
import json

def setLabel(request):
	reply = json.loads(request.text)
	if request.status == 200:
		if "result" in reply:
			print("Correct result from server")
			document["result"].innerHTML = reply["result"]
		else:
			print("Server encountered and error")
			document["result"].innerHTML = reply["error"]
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

