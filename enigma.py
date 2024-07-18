class Enigma:

    def __init__(self, re, r1, r2, r3, pb, kb) -> None:
        self.reflector = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.plugboard = pb
        self.keyboard = kb

    def encipher(self, letter): 
        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)

        signal = self.reflector.reflect(signal)

        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.plugboard.backward(signal)
    
        letter = self.keyboard.backward(signal)
        print(letter)
