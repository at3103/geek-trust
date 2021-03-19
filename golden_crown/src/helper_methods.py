from collections import defaultdict, Counter
import json
from src.exceptions import InvalidEncryption


def encrypt(char, ckey):

	char = char.upper()

	if not char.isalpha():
		raise InvalidEncryption(char)

	# if not ckey.isnumeric() and ckey:
	# 	raise InvalidEncryption(char)

	new_char = ord(char) + ckey

	return chr(new_char) if new_char <=90 else chr(new_char-26)


def get_kingdom_emblems(json_file="config/kingdom_emblems.json"):

	with open(json_file) as f:
		kingdom_emblems = json.load(f)

	return kingdom_emblems


def get_encrypted_emblems():

	kingdom_emblems = get_kingdom_emblems()

	encrypted_emblems = defaultdict()

	for kingdom, emblem in kingdom_emblems.items():

		# Cipher key is the number of characters in the emblem.
		ckey = len(emblem)
		encrypted_emblems[kingdom] = "".join([encrypt(x,ckey) for x in emblem])

	return encrypted_emblems


def is_ally(k_emblem, msg):

	msg_cnt = Counter(msg)
	emb_cnt = Counter(k_emblem)
	for ch, cnt in emb_cnt.items():
		if msg_cnt[ch] < cnt:
			return False

	return True