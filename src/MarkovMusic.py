'''
Created on May 12, 2009

@author: Justin Bozonier
'''
import pysynth
from MarkovBuilder import MarkovBuilder

class MusicMatrix:
    def __init__(self):
        self._markov = MarkovBuilder(["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"])

    def add(self, from_note, to_note):
        """Add a path from a note to another note. Re-adding a path between notes will increase the associated weight."""
        self._markov.add(from_note, to_note)
        
    def next_note(self, from_note):
        return self._markov.next_value(from_note)

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