'''
Created on May 14, 2009

@author: darkxanthos
'''
import random

class MarkovBuilder:
    def __init__(self, value_list):
        self._values_added = 0
        self._reverse_value_lookup = value_list
        self._value_lookup = {}
        for i in range(0, len(value_list)):
            self._value_lookup[value_list[i]] = i
        #Initialize our adjacency matrix with the initial
        #probabilities for note transitions.
        self._matrix=[[0 for x in range(0,len(value_list))] for i in range(0,len(value_list))]

    def add(self, from_value, to_value):
        """Add a path from a note to another note. Re-adding a path between notes will increase the associated weight."""
        value = self._value_lookup
        self._matrix[value[from_value]][value[to_value]] += 1
        self._values_added = self._values_added + 1
        
    def next_value(self, from_value):
        value = self._value_lookup[from_value]
        value_counts = self._matrix[value]
        value_index = self.randomly_choose(value_counts)
        if(value_index < 0):
            raise RuntimeError, "Non-existent value selected."
        else:
            return self._reverse_value_lookup[value_index]
            
    def randomly_choose(self, choice_counts):
        """Given an array of counts, returns the index that was randomly chosen"""
        counted_sum = 0
        count_sum = sum(choice_counts)
        selected_count = random.randrange(1, count_sum + 1)
        for index in range(0, len(choice_counts)):
            counted_sum += choice_counts[index]
            if(counted_sum >= selected_count):
                return index
        raise RuntimeError, "Impossible value selection made. BAD!"