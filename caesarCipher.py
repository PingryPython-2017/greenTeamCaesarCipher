# Define Functions:

def caesar_cipher(text, shift):
	"""
	Takes a message. Shifts it by a certain amount of characters. Returns the shifted message.
	"""
	if len(text) == 0:
		return ""
	
	char = text[0]
	char = ord(char)
	if char <= 126 - shift:
		char += shift
	elif char <= 126:
		char = char - 126 + 31 + shift
	char = chr(char)
	
	return char + caesar_cipher(text[1:], shift)