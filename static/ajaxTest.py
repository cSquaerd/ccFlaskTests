from browser import document, ajax

def setLabel(request):
#	print("in setLabel")
#	print(request.status)
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
		data = {"number" : number},
		oncomplete = setLabel
	)

document["square"].bind("click", squarePress)

