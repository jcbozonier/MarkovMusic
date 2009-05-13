'''
Created on May 12, 2009

@author: Justin Bozonier
'''
import pysynth
import random

class MusicMatrix:
    def __init__(self):
        self._notes_added = 0
        self._reverse_note_lookup = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
        self._note_lookup = {
              "a":0,
              "a#":1,
              "b":2,
              "c":3,
              "c#":4,
              "d":5,
              "d#":6,
              "e":7,
              "f":8,
              "f#":9,
              "g":10,
              "g#":11
              }
        #Initialize our adjacency matrix with the initial
        #probabilities for note transitions.
        self._matrix=[[0 for x in range(0,12)] for i in range(0,12)]

    def add(self, from_note, to_note):
        """Add a path from a note to another note. Re-adding a path between notes will increase the associated weight."""
        note = self._note_lookup
        self._matrix[note[from_note]][note[to_note]] += 1
        self._notes_added = self._notes_added + 1
        
    def next_note(self, from_note):
        note_value = self._note_lookup[from_note]
        note_counts = self._matrix[note_value]
        note_index = self.randomly_choose(note_counts)
        if(note_index < 0):
            raise RuntimeError, "Non-existent note selected."
        else:
            return self._reverse_note_lookup[note_index]
            
    def randomly_choose(self, choice_counts):
        """Given an array of counts, returns the index that was randomly chosen"""
        counted_sum = 0
        count_sum = sum(choice_counts)
        selected_count = random.randrange(1, count_sum + 1)
        for index in range(0, len(choice_counts)):
            counted_sum += choice_counts[index]
            if(counted_sum >= selected_count):
                return index
        raise RuntimeError, "Impossible note selection made. BAD!"

# Playing it comes next :)
#test = [['c',4], ['e',4], ['g',4], ['c5',1]]
#pysynth.make_wav(test, fn = "test.wav")

musicLearner = MusicMatrix()

# Input the melody of Row, Row, Row Your Boat
# The MusicMatrix will automatically use this to 
# model our own song after it.
musicLearner.add("c", "c")
musicLearner.add("c", "c")
musicLearner.add("c", "d")
musicLearner.add("d", "e")
musicLearner.add("e", "f")
musicLearner.add("e", "f")
musicLearner.add("d", "e")
musicLearner.add("e", "f")
musicLearner.add("f", "g")
musicLearner.add("g", "c")

musicLearner.add("c", "c")
musicLearner.add("c", "c")
musicLearner.add("c", "g")

musicLearner.add("g", "g")
musicLearner.add("g", "g")
musicLearner.add("g", "e")

musicLearner.add("e", "g")
musicLearner.add("e", "g")
musicLearner.add("e", "c")

musicLearner.add("c", "c")
musicLearner.add("c", "c")
musicLearner.add("c", "g")

musicLearner.add("g", "f")
musicLearner.add("f", "e")
musicLearner.add("e", "d")
musicLearner.add("d", "c")

random_score = []
current_note = "c"
for i in range(0,20):
    print current_note
    current_note = musicLearner.next_note(current_note)
    random_score.append([current_note, 4])

pysynth.make_wav(random_score, fn = "first_score.wav")