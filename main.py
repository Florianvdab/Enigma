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
from enigma import Enigma


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

enigma = Enigma(B, I, II, III, plugboard, keyboard)
enigma.set_key("DOG")
enigma.set_rings((1, 2, 3))

message = (
    "TESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTING"
)
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + enigma.encipher(letter)

print(cipher_text)
