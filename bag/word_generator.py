import json
import random
import os
print(os.getcwd())
with open('bag/nouns.json', 'r') as f:
    nouns = json.load(f)
with open('bag/adjs.json', 'r') as f:
    adjs = json.load(f)

def get_words():
    return get_good_word(adjs) + "-" + get_good_word(nouns)

def get_good_word(wordlist):
    good_word = False

    while not good_word:
        word = random.choice(wordlist)

        good_word = True

        if len(word) > 10:
            good_word = False

        if '_' in word:
            good_word = False

    return word