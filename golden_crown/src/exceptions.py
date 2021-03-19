class InvalidEncryption(Exception):

	def __init__(self, char):
		self.message = "Seaser Cipher is valid only for characters in the English Alphabet.\
 {} is not part of the English Alphabet.".format(char)
		super().__init__(self.message)


class IncorrectInputFormat(Exception):

	def __init__(self, line_no):
		self.message = "Incorrect input format on line number {lno}.\
 Please provide one kingdom and a non-blank message each line".format(lno=line_no)
		super().__init__(self.message)


class InvalidKingdom(Exception):

	def __init__(self, kingdom, valid_kingdoms):
		self.message = "{kingdom} is not a valid kingdom.\
 Please enter one of the valid kindoms: {valid_kingdoms}".format(kingdom=kingdom, valid_kingdoms=", ".join(valid_kingdoms))
		super().__init__(self.message)