# Author: HackerRank
# Author: Ian Bejarano (Player() class)
# Date: 4/13/2023

# Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. 
# If  or more players have the same score, sort those players alphabetically ascending by name.
# Implement the comparator interface. 

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name + ", " + self.score
        
    def comparator(a, b):
        # flip the normal return values of a comparator class to ensure descending sort 
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.score == b.score:
            # use normal return values for string comparison since name compariosn in in Ascending order 
            if a.name < b.name: return -1 
            else: return 1 
        
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)