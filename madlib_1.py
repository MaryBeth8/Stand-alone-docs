"""
This program generates passages that are generated in mad-lib format
Author: Megabyte 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs has BEGUN!"

name = raw_input("Enter a name: ")
adj_1 = raw_input("Give me an adjective: ")
adj_2 = raw_input("Give me another adjective: ")
adj_3 = raw_input("Give me one more adjective: ")
verb_1 = raw_input("Give me a verb: ")
noun_1 = raw_input("Give me a noun: ")
noun_2 = raw_input("Give me another noun: ")
animal = raw_input("Give me an animal: ")
food = raw_input("Give me a food: ")
fruit = raw_input("Give me a fruit: ")
superhero = raw_input("Give me a superhero: ")
country = raw_input("Give me a country: ")
dessert = raw_input("Give me a dessert: ")
year = raw_input("Give me a year: ")

print STORY % (name, adj_1, adj_2, animal, food, verb_1, noun_1, fruit, adj_3, name, superhero, name, country, name, dessert, name, year, noun_2)
