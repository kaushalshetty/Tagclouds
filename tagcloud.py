import re,string,json
import matplotlib.pyplot as plt
from pytagcloud import create_tag_image,make_tags
from pytagcloud.lang.counter import get_tag_counts
from collections import Counter


def find_speakers(jsonObj):
	return [speaker.keys()[0].encode('utf-8') for speaker in jsonObj]

def rem_punctuation(s) :
	out = s.translate(string.maketrans("",""),string.punctuation)
	return out

def rem_stop_words(s):
	stop_word_file = open("stopWords.txt","r+")
	stop_word_list = stop_word_file.read().split()
	cleaned_list = filter(lambda x: x not in stop_word_list,s.lower().split())
	#print cleaned_list
	return " ".join(cleaned_list)

def create_tag_clouds(dict):

	for i in range(len(dict)):
		word_freq = Counter(dict[dict.keys()[i]].split()).most_common(50)
		tags = make_tags(word_freq,maxsize=120)
		create_tag_image(tags,dict.keys()[i]+".png",size=(1900,1000),fontname='Lobster')


file = open("debatetest.txt","r+")
content = file.read()
content = re.sub(r'"','',content)
content = re.sub(r'[a-z]+:',"",content)
content = re.sub(r"MR",'"},{"MR',content)
content = re.sub(r':','":"',content)
content = re.sub(r'"},','[',content,1)

content = re.sub(r'\n','',content)
content+='"}]'
#print content
wfile = open("test.txt","w+")
wfile.write(content)
speech_json = json.loads(content)
speakers = list(set(find_speakers(speech_json)))
speech_dict = {}
for i in range(len(speakers)):
	speech_dict[speakers[i]] = ""
for speech in speech_json:
	for i in range(len(speakers)):
		if speakers[i] in speech:
			speech_dict[speakers[i]]+=speech[speakers[i]].encode('utf-8')
for i in range(len(speech_dict)):
	cleaned_text = rem_stop_words(rem_punctuation(speech_dict.values()[i]))
	speech_dict[speech_dict.keys()[i]] =  cleaned_text

create_tag_clouds(speech_dict)
