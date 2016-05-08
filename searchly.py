#! /usr/bin/env python
import requests
import json

query = raw_input("Your query: ")

if len(query.split(' ')) > 1:
	queries = query.split(' ')
	query = ''
	for word in queries:
		word = word.lower()
		word = word[0].upper() + word[1:]
		query = query + word + ' '
else:
	query = query.lower()
	query = query[0].upper() + query[1:]
query.replace(" ","%20")
url = "https://api.duckduckgo.com/?q="+query+"&format=json"
try:
	response = requests.get(url)
	data = response.content
	parsed_data = json.loads(data)
	if parsed_data['AbstractText'] == '':
		stripped = parsed_data['RelatedTopics'][0]["Text"].strip(query)
		print '\n' + stripped
	else:	
		print '\n' + parsed_data['AbstractText']
	print "Source: " + parsed_data['AbstractURL']
except:
	print "definition not found or error raised"
