import pygame


def draw(enigma, screen, width, height, margins, gap, font):

    x = margins["left"]
    y = margins["top"]
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, 500, font)

        x += w + gap
