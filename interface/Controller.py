import random

from Ciphers.CrittersCipher import CrittersCipher


class Controller:
    def __init__(self):
        self.publicKey = None
        self.secretKey = None
        self.cipher = None

    def promptWhatToDo(self):
        print("What would you like to do: (1. Generate Key) (2. Encrypt) (3. Decrypt)")
        nextMove = input()
        if nextMove == "1" or nextMove == 1:
            self.generateKey()
        elif nextMove == "2" or nextMove == 2:
            self.promptEncryptionMethod()
        elif nextMove == "3" or nextMove == 3:
            self.promptDecryptionMethod()
        self.promptWhatToDo()


    def generateKey(self):
        print("Generate key for: (1: Critters)")
        option = input()
        if option == "1" or option == 1:
            self.publicKey = random.randint(1, 3)
            self.secretKey = 4 - self.publicKey
            self.cipher = CrittersCipher()
            print("Your Public Key is:", self.publicKey)
            print("Your Secret Key is:", self.secretKey)
        self.promptWhatToDo()

    def promptEncryptionMethod(self):
        print("Please enter encryption method (1: Critters)")
        choice = input()
        print("Enter your plaintext")
        plaintext = input()
        print("Now enter the public key:")
        pubKey = input()
        if choice == 1:
            self.cipher = CrittersCipher()
        else:
            self.cipher = CrittersCipher()
        ciphertext = self.cipher.encrypt(plaintext, int(pubKey))
        print(ciphertext)
        self.promptWhatToDo()

    def promptDecryptionMethod(self):
        print("Please enter decryption method (1: Critters)")
        choice = input()
        print("Enter your ciphertext")
        plaintext = input()
        print("Now enter the private key:")
        privKey = input()
        if choice == 1:
            self.cipher = CrittersCipher()
        else:
            self.cipher = CrittersCipher()
        plaintext = self.cipher.decrypt(plaintext, int(privKey))
        print(plaintext)
        self.promptWhatToDo()