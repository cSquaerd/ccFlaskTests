from browser import document
import random
def roll(event):
	print(dir(event))
	document["value"].value = random.randint(1, int(event.target.value[1:]))
	document["die"].innerHTML = event.target.value

for die in ("d4", "d6", "d8", "d10", "d12", "d20"):
	document[die].bind("click", roll)
