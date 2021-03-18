import argparse
from collections import defaultdict, Counter


def is_ally(k_emblem, msg):

	msg_cnt = Counter(msg)
	emb_cnt = Counter(k_emblem)

	for ch, cnt in emb_cnt.items():
		if msg_cnt[ch] < cnt:
			return False

	return True



def get_kingdom_emblems():

	kingdom_emblems = {	"SPACE" : "GORILLA",
						"LAND"  : "PANDA",
						"WATER" : "OCTOPUS",
						"ICE"   : "MAMMOTH",
						"AIR"   : "OWL",
						"FIRE"  : "DRAGON" 
	}

	return kingdom_emblems

def encrypt(char, ckey):

	char = char.upper()

	new_char = ord(char) + ckey

	return chr(new_char) if new_char <=90 else chr(new_char-26)



def get_encrypted_emblems():

	kingdom_emblems = get_kingdom_emblems()

	encrypted_emblems = defaultdict()

	for kingdom, emblem in kingdom_emblems.items():

		# Cipher key is the number of characters in the emblem.
		ckey = len(emblem)

		#encrypted_emblems[kingdom] = "".join([chr(97 * (ord(x)+ckey)/122  + (ord(x)+ckey)%122) for x in emblem])
		# encrypted_emblems[kingdom] = "".join([chr((96 * ((ord(x)+ckey)//122))  + (ord(x)+ckey)%122) for x in emblem])
		encrypted_emblems[kingdom] = "".join([encrypt(x,ckey) for x in emblem])

	return encrypted_emblems


def find_ruler(fname):
	"""
		Reads the input file and determines the ruler.
	"""

	kingdom_msgs = defaultdict()
	allies = list(["SPACE"])
	kingdom_emblem = get_encrypted_emblems()

	with open(fname, "r") as file:
		for line in file:
			tokens = line.strip().split(" ",1)

			if len(tokens) < 2:
				print("Incorrect input format. Please provide one kingdom and a non-blank message each line")
				return 1

			kingdom_msgs[tokens[0]] = tokens[1]

	for kingdom, msg in kingdom_msgs.items():
		if is_ally(kingdom_emblem.get(kingdom), msg):
			allies.append(kingdom)


	if len(allies) >= 4:
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
