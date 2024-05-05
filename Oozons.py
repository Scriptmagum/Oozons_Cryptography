from random import randint,choice
import string
class caesar:
    def __init__(self):
        self.key=self.generer_cle()
        self.lettres=string.ascii_lowercase 

    def generer_cle(self):
        return randint(0,25)

    def chiffre(self,plaintext):
        plaintext=plaintext.lower()
        ciphertext=""
        for l in plaintext:
            if l in self.lettres:
                ciphertext+=self.lettres[(self.lettres.index(l)+self.key)%26]

            else:
                ciphertext+=l
        return ciphertext

    def dechiffre(self,ciphertext):
        #plaintext=plaintext.lower()
        plaintext=""
        for l in ciphertext:
            if l in self.lettres:
                plaintext+= self.lettres[(self.lettres.index(l)-self.key)%26]

            else:
                plaintext+=l
        return plaintext
    
class otp:

    def __init__(self):
        self.key=None
        self.lettres=string.printable

    def generer_cle(self,size):
        return "".join([choice(self.lettres) for i in range(size)])

    def chiffre(self,plaintext):
        self.key=self.generer_cle(len(plaintext))
        ciphertext=""
        for i in range(len(plaintext)):
           ciphertext+=chr(ord(plaintext[i])^ord(self.key[i]))

        return ciphertext

    def dechiffre(self,ciphertext):
        #self.key=self.generer_cle(len(plaintext))
        plaintext=""
        for i in range(len(ciphertext)):
           plaintext+=chr(ord(ciphertext[i])^ord(self.key[i]))

        return plaintext
