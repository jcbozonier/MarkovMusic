'''
Created on May 12, 2009

@author: Justin Bozonier
'''
import pysynth
from MarkovBuilder import MarkovBuilder

class MusicMatrix:
    def __init__(self):
        self._previous_note = None
        self._markov = MarkovBuilder(["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"])
        self._timings = MarkovBuilder([1, 2, 4, 8, 16])

    def add(self, to_note):
        """Add a path from a note to another note. Re-adding a path between notes will increase the associated weight."""
        if(self._previous_note is None):
            self._previous_note = to_note
            return
        from_note = self._previous_note
        self._markov.add(from_note[0], to_note[0])
        self._timings.add(from_note[1], to_note[1])
        self._previous_note = to_note
        
    def next_note(self, from_note):
        return [self._markov.next_value(from_note[0]), self._timings.next_value(from_note[1])]

# Playing it comes next :)
#test = [['c',4], ['e',4], ['g',4], ['c5',1]]
#pysynth.make_wav(test, fn = "test.wav")

musicLearner = MusicMatrix()

# Input the melody of Row, Row, Row Your Boat
# The MusicMatrix will automatically use this to 
# model our own song after it.
musicLearner.add(["c", 4])
musicLearner.add(["c", 4])
musicLearner.add(["c", 4])
musicLearner.add(["d", 8])
musicLearner.add(["e", 4])
musicLearner.add(["e", 4])
musicLearner.add(["d", 8])
musicLearner.add(["e", 4])
musicLearner.add(["f", 8])
musicLearner.add(["g", 2])

musicLearner.add(["c", 8])
musicLearner.add(["c", 8])
musicLearner.add(["c", 8])

musicLearner.add(["g", 8])
musicLearner.add(["g", 8])
musicLearner.add(["g", 8])

musicLearner.add(["e", 8])
musicLearner.add(["e", 8])
musicLearner.add(["e", 8])

musicLearner.add(["c", 8])
musicLearner.add(["c", 8])
musicLearner.add(["c", 8])

musicLearner.add(["g", 4])
musicLearner.add(["f", 8])
musicLearner.add(["e", 4])
musicLearner.add(["d", 8])
musicLearner.add(["c", 2])

random_score = []
current_note = ["c", 4]
for i in range(0,100):
    print current_note[0] + ", " + str(current_note[1])
    current_note = musicLearner.next_note(current_note)
    random_score.append(current_note)

pysynth.make_wav(random_score, fn = "first_score.wav")