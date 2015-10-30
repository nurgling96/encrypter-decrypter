#!/usr/bin/python
# -*- coding: utf-8 -*-


class Caesar:
    global alphabet
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def encryption(self, word, key):
        result = ""
        for i in word:
            if i in alphabet:
                x = (alphabet.index(i) + key) % len(alphabet)
                new_symbol = alphabet[x]
                result += new_symbol
            if i not in alphabet:
                result += i
        print("Ciphertext: {}".format(result))
        return result

    def decryption(self, cipher, key):
        result = ""
        for i in cipher:
            if i in alphabet:
                x = (alphabet.index(i) - key) % len(alphabet)
                new_symbol = alphabet[x]
                result += new_symbol
            if i not in alphabet:
                result += i
        print("Plaintext message is: {}".format(result))
        return result               

class Vigenere:
    global prepval
    global dec
    global enc
    global dic_len
    global dic

    dic = [chr(i) for i in range(127)]
    dic_len = len(dic)
    prepval = lambda val: zip( range(0,len(val)), val )

    enc = lambda ch,key: (ch + key) % dic_len
    dec = lambda ch,key: (ch - key + dic_len) % dic_len


    def encryption(self, value, key):

        key_len = len(key)
        value = prepval(value)
        e = [enc(ord(c), ord(key[i % key_len])) for (i,c) in value]
        return ''.join([dic[c] for c in e])

    def decryption(self, value, key):
        key_len = len(key)
        value = prepval(value)
        e = [dec(ord(c), ord(key[i % key_len])) for (i,c) in value]
        return ''.join([dic[c] for c in e])
        
loop = True
while loop == True:
    print('')

    way_of_crypt = raw_input('What method do you want to use? \n\
You can choose between Caesar and Vigenere ciphers. \n\
For Caesar print "c" or "v" for Vigenere: ')

    print('')


    if way_of_crypt == "c":
        print("Caesar cipher")
        choice= raw_input('Type "e" for encrypt or "d" for decrypt: ')
        print("")

        if choice == "e":
            word = raw_input("Enter a message: ")
            key = int(input("Enter a key (any number): "))
            c = Caesar()
            c.encryption(word, key)
            

        if choice == "d":
            cipher = raw_input("Enter a cipher: ")
            key = int(input("Enter a key: "))
            c = Caesar()
            c.decryption(cipher, key)


    if way_of_crypt == "v":
        print("Vigenere cipher")
        choice= raw_input('Type "e" for encrypt or "d" for decrypt: ')
        print("")

        if choice == "e":
            word = raw_input("Enter a message: ")
            key = raw_input("Enter a key (any word): ")
            v = Vigenere()
            ciphertext = v.encryption(word, key)
            print("Ciphertext is: {}".format(ciphertext))

        if choice== "d":
            cipher = raw_input("Enter a cipher: ")
            key = raw_input("Enter a key: ")
            v = Vigenere()
            plaintext = v.decryption(cipher, key)
            print("Plaintext message is: {}".format(plaintext))

    print ('')
    response = raw_input("Do you want to continue? (y/n): ")
    if response == "y" or response == "Y":
        pass
    else: # Exit the program
        print ('')
        print('Goodbye')
        loop = False
