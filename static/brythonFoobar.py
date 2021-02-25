from browser import document
def foo(event):
	print(event.x, event.y, "Foobar!")

document["foo"].bind("click", foo)
