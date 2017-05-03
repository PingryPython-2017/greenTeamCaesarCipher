# Define Functions:

def caesar_cipher(text, shift):
	"""
	Takes a message. Shifts it by a certain amount of characters. Returns the shifted message.
	"""
	if len(text) == 0:
		return ""
	
	char = text[0]
	char = ord(char)
	char += shift
	while char > 126:
		char -= 95
	char = chr(char)
	
	return char + caesar_cipher(text[1:], shift)