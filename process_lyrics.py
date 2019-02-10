#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process_lyrics.py
Created on Sat Feb  9 14:02:34 2019
Description: Process lyrics using the musixmatch.api
@author: johnkim
"""
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import re 
import requests 
import time
import json
from google_sentiment_analysis import get_sentiment

def get_urb_dic_defn(word:str) -> list: 
    '''
    Gets the definition as a list of words appended as a bracket
    The words will be those that are highlighted in blue or surrounded as 
    square brackets
    '''
    
    get_definition = json.loads(requests.get("http://api.urbandictionary.com/v0/define?term=%s"%(word)).text)["list"]
    length_get_definition = len(get_definition)
    key_words = []
    
    for i in range(length_get_definition):
        indiv_defn = get_definition[i]["definition"]
        indiv_defn = re.findall(r"\[\w*\s*\w*\]",indiv_defn)

        
        for term in indiv_defn: 
            term = re.sub(r"[\[\]]","",term.lower())
            key_words.append(term)
    
    return(key_words[0])


# An example of an input
lyrics = """Astro, yeah
Sun is down, freezin' cold
That's how we already know winter's here
My dawg would prolly do it for a Louis belt
That's just all he know, he don't know nothin' else
I tried to show 'em, yeah
I tried to show 'em, yeah, yeah
Yeah, yeah, yeah
Gone on you with the pick and roll
Young LaFlame, he in sicko mode
Woo, made this here with all the ice on in the booth
At the gate outside, when they pull up, they get me loose
Yeah, Jump Out boys, that's Nike boys, hoppin' out coupes
This shit way too big, when we pull up give me the loot
(Gimme the loot!)
Was off the Remy, had a Papoose
Had to hit my old town to duck the news
Two-four hour lockdown, we made no moves
Now it's 4AM and I'm back up poppin' with the crew
I just landed in, Chase B mixes pop like Jamba Juice
Different colored chains, think my jeweler really sellin' fruits
And they chokin', man, know the crackers wish it was a noose
Some-some-some, someone said
To win the retreat, we all in too deep
P-p-playin' for keeps, don't play us for weak (someone said)
To win the retreat, we all in too deep
P-p-playin' for keeps, don't play us for weak (yeah)
This shit way too formal, y'all know I don't follow suit
Stacey Dash, most of these girls ain't got a clue
All of these hoes I made off records I produced
I might take all my exes and put 'em all in a group
Hit my esés, I need the bootch
'Bout to turn this function to Bonnaroo
Told her, "Hop in, you comin' too"
In the 305, bitches treat me like I'm Uncle Luke
(Don't stop, pop that pussy!)
Had to slop the top off, it's just a roof (uh)
She said, "Where we goin'?" I said, "The moon"
We ain't even make it to the room
She thought it was the ocean, it's just the pool
Now I got her open, it's just the Goose
Who put this shit together? I'm the glue (someone said)
Shorty FaceTimed me out the blue
Someone said (Playin' for keeps)
Someone said, motherfuck what someone said
(Don't play us for weak)
Yeah
Astro
Yeah, yeah
Tay Keith, fuck these niggas up (Ay, ay)
She's in love with who I am
Back in high school, I used to bus it to the dance (yeah)
Now I hit the FBO with duffles in my hands
I did half a Xan, thirteen hours 'til I land
Had me out like a light, ayy, yeah
Like a light, ayy, yeah
Like a light, ayy
Slept through the flight, ayy
Knocked for the night, ayy, 767, man
This shit got double bedroom, man
I still got scores to settle, man
I crept down the block (down the block), made a right (yeah, right)
Cut the lights (yeah, what?), paid the price (yeah)
Niggas think it's sweet (nah, nah), it's on sight (yeah, what?)
Nothin' nice (yeah), baguettes in my ice (aww, man)
Jesus Christ (yeah), checks over stripes (yeah)
That's what I like (yeah), that's what we like (yeah)
Lost my respect, you not a threat
When I shoot my shot, that shit wetty like I'm Sheck (bitch!)
See the shots that I took (ayy), wet like I'm Book (ayy)
Wet like I'm Lizzie, I be spinnin' Valley
Circle blocks 'til I'm dizzy (yeah, what?)
Like where is he? (Yeah, what?)
No one seen him (yeah, yeah)
I'm tryna clean 'em (yeah)
She's in love with who I am
Back in high school, I used to bus it to the dance
Now I hit the FBO with duffles in my hand (woo!)
I did half a Xan, thirteen hours 'til I land
Had me out like a light, like a light
Like a light, like a light
Like a light (yeah), like a light
Like a light
Yeah, passed the dawgs a celly
Sendin' texts, ain't sendin' kites, yeah
He said, "Keep that on lock"
I said, "You know this shit, it’s life", yeah
It's absolute (yeah), I'm back reboot (it's lit!)
LaFerrari to Jamba Juice, yeah (skrrt, skrrt)
We back on the road, they jumpin' off, no parachute, yeah
Shawty in the back
She said she workin' on her glutes, yeah (oh my God)
Ain't by the book, yeah
This how it look, yeah
'Bout a check, yeah
Just check the foots, yeah
Pass this to my daughter, I'ma show her what it took (yeah)
Baby mama cover Forbes, got these other bitches shook, yeah
Ye-ah
"""
 
def preprocess_lyrics(lyrics:list) -> list:
    eng_stopwords = set(stopwords.words("english"))
    lyrics = lyrics.lower()
    lyrics = re.sub(r"[\(\),.?!]","",lyrics)
    lyrics = word_tokenize(lyrics)
    # Convert all the n't to not 
    word_replace_dict = {"n't":"not","'m":"am,","til":"until","'":"","'em":"them",'"':"",'``':"",'""':"","''":"","’":""}
    lyrics = list(map(lambda word: word_replace_dict[word] if word in word_replace_dict.keys() else word,lyrics))
    lyrics = [word for word in lyrics if word not in eng_stopwords]
    # remove empty elements
    lyrics = [word for word in lyrics if word != ""]
    return(lyrics)


def n_grams(lyrics_list:list,n:int) -> list: 
    # n denotes the n in n-grams 
    # e.g. n=2 -> bigrams; n=3 -> trigrams
    lst_ngrams = [] 
    length_list = len(lyrics_list)
    
    for i in range(length_list - n): 
        lst_ngrams.append(lyrics_list[i:i+n])
    
    return(lst_ngrams)

#lyric = preprocess_lyrics(lyrics=lyrics)
#trigram = n_grams(lyric,3)

'''
Too many api calls
def word_converter(word:str) -> str: 
    # Here we don't consider any synsets and just consider the overall polarity
    word_sentiment_score = get_sentiment(word)
    # Get our "synsets"
    word_list = get_urb_dic_defn(word)
    # get the sentiment scores (polarity) of each word
    #word_sentiment_list = list(map(lambda word_2_sentiment: get_sentiment(word_2_sentiment),word_list))
    #word_sentiment_list = [get_sentiment(word_2_sentiment) for word_2_sentiment in word_list]
    #word_sentiment_list = list(map(lambda word_score: abs(word_score - word_sentiment_score),word_sentiment_list))
    #word_sentiment_list = [abs(word_score - word_sentiment_score) for word_score in word_sentiment_list]
    word_sentiment_list = [abs(get_sentiment(word_2_sentiment)-word_sentiment_score) for word_2_sentiment in word_list]
    print(word_sentiment_list)
    #word_min_sent = min(list(map(lambda word_score: abs(word_score - word_sentiment_score),word_sentiment_list)))
    word_min_sent  = min(word_sentiment_list)
    word_sentiment_list_index = word_sentiment_list.index(word_min_sent)
    word_list = word_list[word_sentiment_list_index]

    # Returns the first occurrence of the min difference between the "synset" and the inputted word
    return(word_list)
'''

# make a dictionary of word to slang (assume slang are any definitions of urban dictionary)
# We'll take the first definition
def word_to_dict(lyrics:str) -> dict: 

    preprocessed_lyrics_set = set(preprocess_lyrics(lyrics))  

    # Build a dictionary from the set 

    translation_dict = {} 

    for word in preprocessed_lyrics_set: 
        translation_dict[word] = get_urb_dic_defn(word)
        time.sleep(1)
    
    #print(translation_dict)
    return(translation_dict) 

'''
s = set(preprocess_lyrics(lyrics))  
print(s)
f = word_converter('fuck')
print(f) 
'''
d = word_to_dict(lyrics)


def substitute_words(lyrics:str,word_dict:dict) -> str:
    dict_substitution = word_to_dict(lyrics)

    lyrics = word_tokenize(lyrics) 
    lyrics = [dict_substitution[word] for word in lyrics if word in dict_substitution.keys()] 

    return(" ".join(lyrics))

print(substitute_words(lyrics,d))

