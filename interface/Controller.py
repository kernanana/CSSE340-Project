import random

from Ciphers.CrittersCipher import CrittersCipher


class Controller:
    def __init__(self):
        self.publicKey = None
        self.secretKey = None
        self.plaintext = None
        self.ciphertext = None
        self.cipher = None

    def promptInput(self):
        print("Please enter a message to encrypt")
        self.plaintext = input()

    def promptEncryptionMethod(self):
        print("Please enter encryption method (1: Critters)")
        choice = input()
        self.publicKey = random.randint(1,3)
        self.secretKey = 4 - self.publicKey
        if choice == 1:
            self.cipher = CrittersCipher()
        else:
            self.cipher = CrittersCipher()

    def runEncryption(self):
        print("encrypting", self.plaintext)
        self.ciphertext = self.cipher.encrypt(self.plaintext, self.publicKey)
        print("result", self.ciphertext)

    def runDecryption(self):
        print("decrypting")
