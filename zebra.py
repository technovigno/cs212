import itertools


def imright(h1, h2):
    return h1 - h2 == 1

def nextto(h1, h2):
    return abs(h1 - h2) == 1

def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item

def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items'%(
        fn.__name__, result, c.starts, c.items))

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings=list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spinard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Kools is yellow
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spinard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )
def main():
    instrument_fn(zebra_puzzle)

if __name__ == "__main__":
    main()