
class SwearJar:
	def __init__(self):
		print("Contructor called")
		SwearJar.soap(self)

	def say(self, sentence):
		sentence = sentence.lower()
		for bw in self.badWords:
			loc = sentence.find(bw)
			while loc != -1:
				self.counts[bw] += 1
				loc = sentence.find(bw, loc + 1)
			#print(loc, bw)
		# fix shit problem later
		self.wordCount += len(sentence.split())
	def reportCard(self):
		for word in self.counts.keys():
			print("%10s: %s" % (word, self.counts[word]))
		print("%d%% swear words" % (sum(self.counts.values()) / self.wordCount * 100))

	def soap(self):
		#for bw in self.badWords:
		#	self.counts[bw] = 0
		self.wordCount = 0
		self.badWords = ['shit','bullshit','crap','bloody','pissed', 'damn']
		self.counts = {}
		for bw in self.badWords:
			self.counts[bw] = 0





sw = SwearJar()
sw.say("I like shitty pizza for shit shit SHIT")
sw.say("This class is crap today!")

sw.reportCard()
sw.soap()
sw.say("This class is crap today!")
sw.reportCard()




