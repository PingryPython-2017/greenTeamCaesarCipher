# Imports:

import caesarCipher

# Main Program:

message = input("Give me a message: ")

shift = input("Give me a shift: ")
integer = False

while integer == False:
	try:
		shift = int(shift)
		integer = True
	except:
		shift = input("That wasn't a valid shift! Try again: ")

print('Your message shifted by {} is "{}"'.format(shift, caesarCipher.caesar_cipher(message, shift)))