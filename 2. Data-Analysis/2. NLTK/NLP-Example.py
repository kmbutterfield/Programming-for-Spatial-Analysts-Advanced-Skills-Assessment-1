'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Practical: 7; NLTK
    Author: kmbutterfield
    File name: NLP-Example.py
    Description: Finding location names within T.S. Eliot's "The Waste Land".
'''

import os
import requests
import nltk
import time
import pandas as pd
#import csv

''' Extract raw text from T.S.Eliot's "The Waste Land" online text file '''

# Read in the web page's text file
url = "http://www.gutenberg.org/files/1321/1321-0.txt"
raw = requests.get(url).text

# Cut down the text to the poem
start = "il miglior fabbro"
start_pos = raw.find(start) + len(start)
end_pos = raw.rfind("Line 415 aetherial] aethereal")
raw = raw[start_pos:end_pos]

# Use tokenize lexical scanner on the raw test
tokens = nltk.word_tokenize(raw)
type(tokens)
text = nltk.Text(tokens)

# Find 20 most common words (includes punctuation)
fdist = nltk.FreqDist(text)
fdist.plot(50, cumulative=True) # create graph of words
print(fdist.most_common(20))

# Find 20 most common word lengths
fdist =  nltk.FreqDist(len(w) for w in text)
fdist.plot(50)
print(fdist.most_common(20))

# Find all the words over 10 letters long
sorted_words = sorted(set(text))
long_words = [w for w in sorted_words if len(w) > 10]
print(long_words)

'''  Extract raw text from T. S. Eliot's "The Waste Land" online text file '''

# Speech tagging
nltk.download('averaged_perceptron_tagger')
tagged = nltk.pos_tag(text)

# Extract the Proper Noun and remove tags with numbers and capitals.
propernouns = []
for tag in tagged:
    if tag[1] == "NNP" and tag[0].isalpha() and not tag[0].isupper():
        propernouns.append(tag[0])

# Replace the value below with your personal API key:
mykey = "..."

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

df = pd.DataFrame()

for noun in propernouns:
    params = {
        'address': noun,
        'key' : mykey
    }

    # Request to get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    if res['results']:
        # Use the first result
        result = res['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
        df = df.append(geodata, ignore_index = True)
        # Wait for 5 seconds to avoid API issues
        time.sleep(5)
# Produce output file containing address, long and lat.
df.to_csv("places-locations.csv")

''' Original attempt to write csv output file; found df.to_csv as a better solution
        with open ('text.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Pronoun", "Address", "Longitude", "Latitude"])
            for item in propernouns:
                writer.writerow((item, ))

'''
