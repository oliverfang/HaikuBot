import re
import os
import sys
sys.path.append(os.getcwd())
from getSyllables import getSyllables
from pprint import pprint


def isHaiku(s):
	# almost never going to be a haiku longer than 100 characters
	if len(s) > 100:
		return False
	print s
	# remove punctuation
	s = s.replace("\n", " ")
	out_punc = s
	out = re.sub('[!?.,]', '', s)

	# parse string using space delimiter and put into list
	sentence = filter(None, out.split(" "))
	sentence_punc = filter(None, out_punc.split(" "))
	#print sentence
	#print sentence_punc

	# get number of syllables for each word
	syllables = []
	for word in sentence:
		syllables.append(getSyllables(word))

	#print syllables
	#print sum(syllables)

	# if not 17 syllables, wrong
	if sum(syllables) != 17:
		return False

	curr_syll = 0
	target_syll = [5, 7, 5]

	# data structure for haiku
	haikuArr = []
	line = []

	ind = 0
	for i in range(0, len(syllables)):
		# add up syllables
		curr_syll += syllables[i]
		# create lines as we go
		line.append(sentence_punc[i])
		# if word ends on the right syllable, continue checking
		if curr_syll == target_syll[ind]:
			ind += 1
			curr_syll = 0
			# add the line to the haiku
			haikuArr.append(line)
			line = []
		# if exceeded, then not a haiku
		elif curr_syll > target_syll[ind]:
			return False
	# if we made it here, must be haiku, so return it
	haiku = []
	for line in haikuArr:
		newline = ' '.join(line)
		haiku.append(newline)
	return haiku

if __name__ == "__main__":
	# argv = sys.argv
	# if len(argv) != 2:
	# 	sys.exit("Must enter exactly 1 word")
	pprint(isHaiku("Follow that airplane!\n Of course I am off-campus.\n\n An emergency!"))