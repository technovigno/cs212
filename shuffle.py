import random


def swap(p,i,j):
	p[i], p][j] = p[j], p[i]

def knuth_shuffle(p):
	"""Knuths shuffle algo which is gives every element an equally likely chance to be shuffled"""
	n = len(p)
	for i in range(n-1):
		swap(p, i, random.randrange(i,n))

def shuffle1(p):
    """Simple (wrong) shuffle which might not have a deterministic end"""
	n = len(p)
	swapped = [False] * n
	while not all(swapped):
		i,j = random.randrange(n), random.randrange(n)
		swap(p, i, j)
		swapped[i] = swapped[j] = True

def shuffle2(p):
	"""Variation of a simple (wrong) shuffle"""
	n = len(p)
	swapped= [False] * n
	while not all(swapped):
		i,j = random.randrange(n), random.randrange(n)
		swap(p, i, j)
		swapped[i] = True

def shuffle3(p):
	"""Shuffle Variation"""
	n = len(p)
	for i in range(n):
		swap(p, i, random.randrange(n))


def test_shuffle(shuffler, deck='abcd', n=10000):
	counts = defaultdict(int)
	for _ in range(n):
		input = list(deck)
		shuffler(input)
		counts[''.join(input)] += 1
	e = n * 1./factorial(len(deck))
	ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
	name = shuffler.__name__
	print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
	print '   ',
	for item, count in sorted(counts.items()):
		print "%s:%4.1f" % (item, count * 100./n),
	print 

def test_shufflers(shufflers = [knuth_shuffle, shuffle1, shuffle2, shuffle3], decks=['abc', 'ab']):
	for deck in decks:
		print
		for f in shufflers:
			test_shuffle(f, deck)

def factorial(n):
	return 1 if n <= 1 else n * factorial(n-1)



def main():
	test_shufflers()


if "__name__" == "__main__":
	main(argv[1:])