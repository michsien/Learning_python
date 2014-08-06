lexicon_of_words = [
	('direction', ['north' , 'south', 'east', 'west', 'down',
	 				'up', 'left', 'right', 'back']),
	('verb', ['go', 'stop', 'kill', 'eat']),
	('stop', ['the', 'in', 'of', 'from', 'at', 'it']),
	('noun', ['door', 'bear', 'princess', 'cabinet'])
]

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(str):
	tuples = []
	for w in str.split():
		type = None

		w_lower = w.lower()
		for (t, t_words) in lexicon_of_words:
			if w_lower in t_words:
				type = t
				break

		if type is None:
			number = convert_number(w)
			if number is None:
				type = 'error'
			else:
				type = 'number'
				w = number

		tuples.append((type, w))

	return tuples