import re


str = "This is a long sentence no that is very long for sure."

loc = 0
while(loc != -1):
	loc = str.find('en', loc+1)
	print(loc)

# The better way to do it!
res = re.findall(" [a-z][a-z] ", str, flags=0)
print("There were %d matches" % len(res))
for s in res:
	print(s)


