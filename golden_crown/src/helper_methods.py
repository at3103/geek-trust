from collections import defaultdict, Counter
import json
from src.exceptions import InvalidEncryption


def encrypt(char, ckey):
	"""
	Uses Seaser Cipher to encrypt the given character with 'ckey' Cipher Key.
	"""
	char = char.upper()

	if not char.isalpha():
		raise InvalidEncryption(char)

	new_char = ord(char) + ckey%26

	return chr(new_char) if new_char <=90 else chr(new_char-26)


def get_kingdom_emblems(json_file="config/kingdom_emblems.json"):
	"""
	Reads a json file to extract the kingdoms and it's respective emblems.

	This also extracts the candidate kingdom that sends the encrypted messages.
	"""

	with open(json_file) as f:
		full_json = json.load(f)

	kingdom_emblems = full_json["all_kingdoms"]
	candidate = full_json["candidate"]

	return candidate, kingdom_emblems


def get_encrypted_emblems():
	"""
	Obtains the kingdom-emblem map and encrypts the emblems using Seaser Cipher.
	"""

	candidate, kingdom_emblems = get_kingdom_emblems()

	encrypted_emblems = defaultdict()

	for kingdom, emblem in kingdom_emblems.items():

		# Cipher key is the number of characters in the emblem.
		ckey = len(emblem)
		encrypted_emblems[kingdom] = "".join([encrypt(x,ckey) for x in emblem])

	return candidate, encrypted_emblems


def is_ally(k_emblem, msg):
	"""
	Determines if a given kingdom is an ally based on it's emblem and message transmitted.
	"""
	msg_cnt = Counter(msg)
	emb_cnt = Counter(k_emblem)
	for ch, cnt in emb_cnt.items():
		if msg_cnt[ch] < cnt:
			return False

	return True