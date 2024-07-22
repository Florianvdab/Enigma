import pygame

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw


# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# create fonts
MONO = pygame.font.SysFont("FreeMono", 20)
BOLD = pygame.font.SysFont("FreeMono", 20, bold=True)

WIDTH = 1600
HEIGHT = 1020
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top": 200, "bottom": 100, "left": 100, "right": 100}
GAP = 100

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
enigma.set_key("CAT")
enigma.set_rings((1, 1, 1))

animating = True
while animating:
    # background
    SCREEN.fill("#333333")

    # draw enigma machine
    draw(enigma, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)   
    # update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate(1)
