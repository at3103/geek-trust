import argparse
from src.helper_methods import encrypt, get_encrypted_emblems, is_ally
from collections import defaultdict, Counter


def find_ruler(fname):
	"""
		Reads the input file and determines the ruler.
	"""

#	kingdom_msgs = defaultdict()
	allies = list(["SPACE"])
	kingdom_emblem = get_encrypted_emblems()

	MAJORITY = -(len(kingdom_emblem)//-2)

	with open(fname, "r") as file:
		for lno, line in enumerate(file,1):
			tokens = line.strip().split(" ",1)

			if len(tokens) < 2:
				return "Incorrect input format on line number {lno}.\
 Please provide one kingdom and a non-blank message each line".format(lno=lno)

			kingdom, msg = tokens
			if kingdom in allies:
				continue
			elif is_ally(kingdom_emblem.get(kingdom), msg):
				allies.append(kingdom)


	if len(allies) >= MAJORITY + 1:
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
