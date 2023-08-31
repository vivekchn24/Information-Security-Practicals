# -*- coding: utf-8 -*-
"""ceaser-cipher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18UYfcZWPLxlRG_dIwPQTrgVtGeyoJkTX
"""

text = input("enter the text here.")
key = int(input("enter the key here."))

#A python program to illustrate Caesar Cipher Technique
def encryption(ptext,key):
	result = ""

	# traverse text
	for i in range(len(ptext)):
		char = ptext[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + key))

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + key))

	return result

#A python program to illustrate Caesar Cipher Technique
def decryption(ctext,key):
		plaintext = ""
		for i in ctext:
				if i.isupper():
						plaintext += chr((ord(i) - key))
				else:
						plaintext += chr((ord(i) - key))

		return plaintext

def cryptanalysis(ttext):
	k=0
	for j in range (1,26):
			decrypt_key = ""
			for i in ttext:
					if i.isupper():
							decrypt_key += chr((ord(i) - j))
					else:
							decrypt_key += chr((ord(i) - j))
			if(decrypt_key==text):
					break
	return j

print ("Cipher Text: " + encryption(text,key))
cipher_Text = encryption(text,key)
print ("Plain text for the Cipher Text is: " + decryption(cipher_Text,key))
key_Text = cryptanalysis(cipher_Text)
print ("Cipher Text Key is: " , int(key_Text))