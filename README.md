Background
A common element seen on web pages these days are tag clouds (http://en.wikipedia.org/wiki/Tag_cloud). A tag cloud is a visual representation of frequency of words, where more frequent words are represented in larger font. One can also use colors and placement.

We are going to analyze the presidential debate transcript and create a tag cloud for each candidate of the words they used, where the frequency of the words indicates the size of the font in the cloud.

We provide a number of elements to help with this task:
a transcript of the debate
a list of stopwords
some functions

Transcript
The transcript is in debate.txt. It has a particular format. Each time one of the candidates speaks, that line is marked, e.g ‘PRESIDENT OBAMA:’. Once encountered, all words are attributed to that speaker until another label occurs (sometimes it is a question from the moderator so you have to ignore those). Take a look at the file.

Stopwords
Not all words are worth counting. ‘a’, ‘the’, ‘was’, etc. are just junk. A list of such words is provided as stopWords.txt. Each line has a single word. No word in the stop word list should be counted in the tag cloud. 




GOAL:
Get to know what each speaker is speaking about by glancing over the tagcloud.
