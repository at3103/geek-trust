class InvalidEncryption(Exception):

	def __init__(self, char):
		self.message = "Seaser Cipher is valid only for characters in the English Alphabet.\
 {} is not part of the English Alphabet.".format(char)
		super().__init__(self.message)