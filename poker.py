import random

def poker(hands):
	"""returns the best hand: poker([hand,...]) => hand"""
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	"""Returns a list of items equal to the max (incase of ties)"""
	iterable.sort(key=key, reverse=True)
	result = [iterable[0]]
	maxValue = key(iterable[0]) if key else iterable[0]
	for value in iterable[1:]:
		v = key(value) if key else value
		if v == maxValue: 
			result.append(value)
		else:
			break
	return result

def hand_rank(hand):
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif two_pair(ranks):
		return (2, two_pair(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)

def card_ranks(hand):
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
	ranks.sort(reverse=True)
	return straight_specialcase(ranks)

def straight_specialcase(ranks):
	return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

'''
Modules with lower abstraction on hand types
'''

def straight(ranks):
	"""Returns true if the ranks of the card are ordered continuously with no breaks """
	return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
	""" Returns true if all cards are from the same suit"""
	suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the value which occurs exactly n times in the ranks"""
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None

def two_pairs(ranks):
	"""Returns two pairs  of ranks if there exists two pairs"""
	pair = kind(2, pair)
	lowerpair = kind(2, list(reversed(ranks)))
	if pair and lowerpair != pair:
		return (pair, lowerpair)
	else:
		return None

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
	random.shuffle(mydeck)
	return [mydeck[n*i:n*(i+1)] for i in range(numhands)]

hand_names = ["Straight flush", "Four of a kind", "Full house", "Flush", "Straight",
              "Three of a kind", "Two pair", "One pair", "High card"]

def hand_percentages(n=700*1000):
	count = [0]*9
	for i in range(n/10):
		for hand in deal(10):
			ranking = hand_rank(hand)[0]
			counts[ranking] += 1
	for i in reversed(range(9)):
		print "%15s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)

def main():
	poker(hands)


if __name__ == "__main__":
	main(argv[1:])