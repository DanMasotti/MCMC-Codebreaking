from bs4 import BeautifulSoup
from word2number import w2n
import re
import string
from contractions import contractions
import unidecode


def clean_text(dirty_text):
	text = expand_contractions(remove_accented_chars(strip_html_tags(dirty_text)))
	# get rid of punctuation
	text = text.translate(str.maketrans('', '', string.punctuation))
	# get rid of numbers
	text = re.sub(r'[0-9]+','',text)
	# make all lowercase
	text = text.lower()
	#get rid of huge spaces by splitting on word, then joining adding a space
	text = text.split()
	text = ' '.join(text)
	return text


def strip_html_tags(text):
	"""remove html tags from text"""
	soup = BeautifulSoup(text, "html.parser")
	stripped_text = soup.get_text(separator=" ")
	return stripped_text

def remove_accented_chars(text):
	"""remove accented characters from text, e.g. café"""
	text = unidecode.unidecode(text)
	return text

def expand_contractions(text):
	"""expand shortened words, e.g. don't to do not"""
	contractions_re = re.compile('(%s)' % '|'.join(contractions.keys()))
	def replace(match):
		return contractions[match.group(0)]
	return contractions_re.sub(replace, text)