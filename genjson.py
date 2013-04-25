import json
import os

obj = {"id":1, "tree":{"p":[]}}

a = os.listdir('p')
for char in a:
	obj['tree']['p'][char] = []
	for post in os.listdir('p' + "/" + char):
		obj['tree']['p'][char].append({'post':post})

print json.dumps(obj)
