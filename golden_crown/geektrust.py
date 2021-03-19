import argparse
from src.helper_methods import encrypt, get_encrypted_emblems, is_ally
from src.exceptions import InvalidKingdom, IncorrectInputFormat
from collections import defaultdict, Counter



def find_ruler(fname):
	"""
		Reads the input file and determines the ruler.
	"""

	candidate, kingdom_emblem = get_encrypted_emblems()
	allies = list([candidate])

	MAJORITY = -(len(kingdom_emblem)//-2) + 1

	with open(fname, "r") as file:
		for lno, line in enumerate(file,1):
			tokens = line.strip().split(" ",1)

			if len(tokens) < 2:
				raise IncorrectInputFormat(line_no=lno)

			kingdom, msg = tokens

			if kingdom not in kingdom_emblem:
				raise InvalidKingdom(kingdom, kingdom_emblem.keys())

			if kingdom in allies:
				continue 
			elif is_ally(kingdom_emblem.get(kingdom), msg):
				allies.append(kingdom)


	if len(allies) >= MAJORITY:
		return " ".join(allies)

	return "NONE"



def main():

	parser = argparse.ArgumentParser(description='Analyze the secret messages to determine if King Shan gets the Golden Crown!')

	parser.add_argument("input_fname", type=str, help="Absolute path of the input text file")

	args = parser.parse_args()

	ruler = find_ruler(fname=args.input_fname)

	print(ruler)


if __name__ == "__main__":
	main()
