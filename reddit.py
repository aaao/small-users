from itertools import product
import requests
import re
chars = 'abcdefghijkmnopqrstuvwxyz0123456789' # chars to look for
def main():
	for length in range(4, 30): # only do lengths of 1 + 2
		to_attempt = product(chars, repeat=length)
		for attempt in to_attempt:
			print("trying:" + re.sub('[^abcdefghijkmnopqrstuvwxyz0123456789]', '', str(attempt)))
			r = requests.get('https://reddit.com/u/' + re.sub('[^abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ0123456789]', '', str(attempt)))
			if r.status_code == 404:
				if re.sub('[^abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ0123456789]', '', str(attempt)) != "acw":
					if re.sub('[^abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ0123456789]', '', str(attempt)) != "abc":
						if re.sub('[^abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ0123456789]', '', str(attempt)) != "ab9":
							print(re.sub('[^abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ0123456789]', '', str(attempt)))
							print("Reddit success")
							return
main()