import requests
import sys
import re
from pprint import pprint
from lxml import html


def getSyllables(word):
	# get all html data from dictionary page and put into tree
	page = requests.get('http://www.dictionary.com/browse/%s?s=t' % word)
	tree = html.fromstring(page.content)

	# get syllable data from tree
	syllable = tree.xpath("//@data-syllable")

	#print syllable[0]

	# convert to string and parse
	try:
		syllable_str = syllable[0].encode('ascii', 'replace')

		# print syllable_str; checks for hyphenated words
		syllables = re.split('[?-]', syllable_str)

		# return length
		return len(syllables)
	except IndexError:
		# returns -1 if word not found
		return -1

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) != 2:
		sys.exit("Must enter exactly 1 word")
	print getSyllables(str(argv[1]))