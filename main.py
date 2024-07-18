"""
Reflector:  A
Rotors:     I-II-III
Plugboard:  A-R, G-K, O-X
Message:    A-X
"""

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector


I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

keyboard = Keyboard()
plugboard = Plugboard(["AR", "GK", "OX"])

letter = "A"

def enigma(letters): 
    for letter in letters: 
        signal = keyboard.forward(letter)
        signal = plugboard.forward(signal)
        signal = III.forward(signal)
        signal = II.forward(signal)
        signal = I.forward(signal)

        signal = A.reflect(signal)

        signal = I.backward(signal)
        signal = II.backward(signal)
        signal = III.backward(signal)
        signal = plugboard.backward(signal)
        letter = keyboard.backward(signal)
        print(letter)
    
enigma("ENIGMA")
