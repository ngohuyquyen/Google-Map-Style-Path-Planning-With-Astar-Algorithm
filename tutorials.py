# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:23:14 2020

@author: ASUS
"""

ticket = {
    "date" : "2018-12-28",
    "priority" : "high",
    "description" : """Vehicle did not slow down despite
    SLOW    
    SCHOOL    
    ZONE    """
}

print(ticket.keys())
print(ticket['description'])

# Let's start with an empty dictionary. Eventually this will store 
# English to spanish translations...

eng_to_spa = {} # this creates an empty dictionary
print(eng_to_spa)

# 1. Adding elements to a dictionary.
#
#    Elements can be added to a dictionary as follows:

eng_to_spa['blue']  = 'Azul'
eng_to_spa['gren']  = 'verde'

print(eng_to_spa)

# 2. Removing elements from a dictionary
#    
#    Elements can be removed from a dictionary using the del keyword

del eng_to_spa['gren']

print(eng_to_spa)

# 3. Modifying elements in a dictionary.
#
#    Modifying the value associated with a key works just
#    like adding a new value...

eng_to_spa['blue'] = 'azul'

print(eng_to_spa)

eng_to_spa['blue'] = 'azul'
eng_to_spa['green'] = 'verde'
eng_to_spa['pink'] = 'rosa'
eng_to_spa['orange'] = 'naranja'
eng_to_spa['gray'] = 'gris'
eng_to_spa['brown'] = 'marron'

# YOUR CODE HERE - complete the eng_to_spa
#   dictionary so it contains all the information
#   shown in the table above.

# Testing code below
assert(eng_to_spa['blue'] == 'azul')
assert(eng_to_spa['gray'] == 'gris')
assert(eng_to_spa['orange'] == 'naranja')
assert(eng_to_spa['pink'] == 'rosa')
print("Your english to spanish dictionary is looking good!")



dictionary_ticket_1 = {
    "date"       : "2018-12-31",
    "priority"   : "high",
    "description": "Vehicle made unexpected stop."
}

dictionary_ticket_2 = {
    "priority"   : "high",
    "description": "Vehicle made unexpected stop.",
    "date"       : "2018-12-31"
}

# these dictionaries contain the same information, but the
# ordering looks different. Does Python consider them identical?

print("Does dictionary_ticket_1 == dictionary_ticket_2?")
print(dictionary_ticket_1 == dictionary_ticket_2)


# demonstration of dictionary looping 
# demo 1 - keys only

for key in dictionary_ticket_1:
    print(key)
    
    


# demonstration of dictionary looping 
# demo 2 - keys and values

for key in dictionary_ticket_1:
    value = dictionary_ticket_1[key]
    print(key, ':', value)

def reverse_dictionary(dictionary):
    new_d = {}
    # TODO - your code here
    for key in dictionary:
        #temp = dictionary[key]
        #key = temp
        #dictionary[temp] = key
        new_d[dictionary[key]] = key
    return new_d

eng_to_spa = {
    "red" :    "rojo",
    "blue"   : "azul",
    "green"  : "verde",
    "black"  : "negro",
    "white"  : "blanco",
    "yellow" : "amarillo",
    "orange" : "naranja",
    "pink"   : "rosa",
    "purple" : "morado",
    "gray"   : "gris"
}

# TESTING CODE

spa_to_eng = reverse_dictionary(eng_to_spa)

assert(len(spa_to_eng) == len(eng_to_spa))
assert(spa_to_eng['rojo'] == 'red')
assert(spa_to_eng['azul'] == 'blue')
assert(spa_to_eng['verde'] == 'green')

print("Nice work! Your reverse_dictionary function is correct.")

eng_to_spa = {
    "red" :    "rojo",
    "blue"   : "azul",
    "green"  : "verde",
    "black"  : "negro",
    "white"  : "blanco",
    "yellow" : "amarillo",
    "orange" : "naranja",
    "pink"   : "rosa",
    "purple" : "morado",
    "gray"   : "gris"
}

french_to_eng = {
    "bleu"  : "blue",
    "noir"  : "black", 
    "vert"  : "green",
    "violet": "purple",
    "gris"  : "gray",
    "rouge" : "red",
    "orange": "orange",
    "rose"  : "pink",
    "marron": "brown",
    "jaune" : "yellow",
    "blanc" : "white",
}

print("there are    ", len(eng_to_spa), "colors in eng_to_spa")
print("but there are", len(french_to_eng), "colors in french_to_eng")

# don't forget you have the "reverse_dictionary" function!

english_to_french = reverse_dictionary(french_to_eng)

for english_word in english_to_french:
    french_word = english_to_french[english_word]
    print("The french word for", english_word, "is", french_word)

def spanish_to_french(english_to_spanish, english_to_french):
    """
    Given an English to Spanish dictionary and an English
    to French dictionary, returns a Spanish to French dictionary.
    
    If any words appear in one dictionary but NOT the other, 
    they should not be included in the resulting dictionary.
    """
    s2f = {}
    #
    # TODO - your code here
    #
    spanish_to_english = reverse_dictionary(english_to_spanish)
    for spanish_word in spanish_to_english:
        english_word = spanish_to_english[spanish_word]
        french_word = english_to_french[english_word]
        s2f[spanish_word] = french_word
    return s2f


# TESTING CODE 
S2F = spanish_to_french(eng_to_spa, english_to_french)

assert(S2F["rojo"] == "rouge")
assert(S2F["morado"] == "violet")

print("Nice work! Your spanish to french function works correctly!")


# Note how the structure of a ticket is captured in the dictionary


ticket = {
    "type" : "bug",
    "status": "done",
    "priority": "medium",
    "resolution": "done",
    "description" : "testing 123",
    "attachments" : [],
    "people": {
        "assignee" : None,
        "reporter" : {
            "name" : "Andy Brown",
            "image": "www.example_image_url.com"
        },
        "votes" : 0,
        "watchers" : [
            {
                "name": "Andy Brown",
                "image": "www.example_image_url.com"  
            }
        ]
    },
    "dates" : {
        "created" : "6 days ago",
        "updated" : "6 days ago",
        "resolved": "6 days ago"
    }
}

# In this example, ticket is a dictionary with the following "keys":

print("The keys for this dictionary are...")
ticket.keys()

# notice how nicely the following code reads... 

ticket['people']['reporter']['name']

# let's pull in a bunch of "dummy" data

from sample_data import big_tickets
import random

print("there are", len(big_tickets), "big tickets")


# grab a random ticket and take a look at it

random_ticket = random.choice(big_tickets)
random_ticket

def get_popular_tickets(tickets):
    """
    From a list of tickets, fetch all the tickets with 8 or 
    more "watchers". 
    """
    popular_tickets = []
    #
    # TODO - your code here
    # 
    for ticket in tickets:
        if len(ticket['people']['watchers']) >= 8:
            popular_tickets.append(ticket)
    return popular_tickets

popular = get_popular_tickets(big_tickets)

# TESTING CODE 
assert( len(popular) > 0 ) # must be at least one popular ticket

for ticket in popular:
    assert( len(ticket['people']['watchers']) >= 8 )
    
print("Nice job! It looks like your function is working.")


















# start with an empty set

my_set = set()

print(my_set)


# add a few elements

my_set.add('a')
my_set.add('b')
my_set.add('c')
my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)

# like a dictionary, a set is UNORDERED. 
# We can still loop through a set though.

for element in my_set:
    print(element)

# let's see how many elements are in this set...

print("there are", len(my_set), "elements in my_set")


# and they haven't changed. What if we remove "a"
my_set.remove("a")
print("there are", len(my_set), "elements in my_set")
print(my_set)




# Initializing two sets

odds   = set([1,3,5,7,9])
primes = set([2,3,5,7])

# Demonstration of the "intersection" between two sets
# The intersection corresponds to the overlapping region
# in the Venn Diagram above.

odd_AND_prime = odds.intersection(primes)
print(odd_AND_prime)

# Demonstration of the "union" of two sets. The union
# of sets A and B includes ANY element that is in A OR B 
# or both.

odd_OR_prime = odds.union(primes)
print(odd_OR_prime)

# Demonstration of the "set difference" between two sets.
# What do you expect odds-primes to return?

odd_not_prime = odds - primes
print(odd_not_prime)

# Another demo of "set difference"

prime_not_odd = primes - odds
print(prime_not_odd)


























