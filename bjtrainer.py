#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random

# Initialize the deck of cards
def Deck():
	suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	return suit * 4

# Return the count status of the card passed through the method
def counter(card):
	c = -1
	try:
		thisCard = int(card)
		if thisCard <= 6:
			c = 1
		elif thisCard <= 9:
			c = 0
	except:
		if card in [10,'J','Q','K','A']:
			c = -1
	return c

# Tell the users what this is and how to use
def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)\n\n"

# Deck selection
def deckselect():
	dint = input("How Many decks will we use? (1,2, or 6)")
	d = int(dint)
	while d not in [1,2,6]:
		dint = input("How many decks will we use? (1, 2, or 6)")
		d = int(dint)
		if d == 1:
			print "Single Deck.\n"
			d = 1
			return d
		elif d == 2:
			d = 2
			print "Double Deck.\n"
			return d
		elif d == 6:
			print "6 Deck Shoe.\n"
			d = 6
			return d
		else:
			print "You didn't choose a proper deck size."
	return d

# More initialization
fulldeck = Deck() * deckselect()
print fulldeck

count = 0

while True:
	try:
		card1 = fulldeck[random.randint(0,len(fulldeck)-1)]
		fulldeck.remove(card1)
		card2 = fulldeck[random.randint(0,len(fulldeck)-1)]
		fulldeck.remove(card2)
	except ValueError:
		count = 0
		fulldeck = Deck() * deckselect()
		print fulldeck
		card1 = fulldeck[random.randint(0,len(fulldeck)-1)]
		fulldeck.remove(card1)
		card2 = fulldeck[random.randint(0,len(fulldeck)-1)]
		fulldeck.remove(card2)
	count = count + counter(card1)
	count = count + counter(card2)
	print "Your hand: {0},{1}".format(card1, card2)
	print "The coount is: {0}".format(count)
	print fulldeck
	response = raw_input("Deal?(y/n)")
	if response == "n":
		break

