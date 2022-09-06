
def printIt(it):
	#it.append(55)
	#it = 7
	it[-1] = "Nothing to see here"
	print(it)

if __name__ == "__main__":

	list = [5,"bob"] #[5,6,7,8]


	print(list)
	printIt(list)
	print(list)