inputfile = open("p054_poker.txt", "r")
hands = inputfile.readlines()

def highestRankForHand(hand):
    if isRoyalFlush(hand):
        return 10
    if isStraightFlush(hand):
        return 9
    if isFourOfAKind(hand):
        return 8
    if isFullHouse(hand):
        return 7
    if isFlush(hand):
        return 6
    if isStraight(hand):
        return 5
    if isThreeOfAKind(hand):
        return 4
    if isTwoPairs(hand):
        return 3
    if isPair(hand):
        return 2
    return 0

def getPairValue(hand):
    hand = [x[:-1] for x in hand]
    pairs = [valueToInt(x) for x in hand if hand.count(x) == 2]

    single = [valueToInt(x) for x in hand if hand.count(x) == 1]
    single.sort()
    return pairs[0], single[2], single[1], single[0]


def getThreePairValues(hand):
    hand = [x[:-1] for x in hand]
    pairs = [valueToInt(x) for x in hand if hand.count(x) == 3]
    single = [valueToInt(x) for x in hand if hand.count(x) == 1]
    single.sort()
    return pairs[0], single[1], single[0]


def getTwoPairValues(hand):
    hand = [x[:-1] for x in hand]
    pairs = [valueToInt(x) for x in hand if hand.count(x) == 2]
    pairs.sort(reverse=True)
    single = [valueToInt(x) for x in hand if hand.count(x) == 1]
    return pairs[0], pairs[1], single[0]

def smartCompare(hand1, hand2):
    isPair = highestRankForHand(hand1) == 2
    isTwoPair= highestRankForHand(hand1) == 3
    isThree = highestRankForHand(hand1) == 4
    if isPair:
        h1v1, h1v2, h1v3, h1v4 = getPairValue(hand1)
        h2v1, h2v2, h2v3, h2v4 = getPairValue(hand2)
        if h1v1 != h2v1:
            return h1v1 > h2v1
        if h1v2 != h2v2:
            return h1v2 > h2v2
        if h1v3 != h2v3:
            return h1v3 > h2v3
        if h1v4 != h2v4:
            return h1v4 > h2v4
        print("wtf2")
    if isTwoPair:
        h1v1, h1v2, h1v3 = getTwoPairValues(hand1)
        h2v1, h2v2, h2v3 = getTwoPairValues(hand2)
        if h1v1 != h2v1:
            return h1v1 > h2v1
        if h1v2 != h2v2:
            return h1v2 > h2v2
        if h1v3 != h2v3:
            return h1v3 > h2v3
        print("wtf2")
    if isThree:
        h1v1, h1v2, h1v3 = getTwoPairValues(hand1)
        h2v1, h2v2, h2v3 = getTwoPairValues(hand2)
        if h1v1 != h2v1:
            return h1v1 > h2v1
        if h1v2 != h2v2:
            return h1v2 > h2v2
        if h1v3 != h2v3:
            return h1v3 > h2v3
        print("wtf3")

    hand1Values = [valueToInt(c[:-1]) for c in hand1]
    hand1Values.sort(reverse=True)
    hand2Values = [valueToInt(c[:-1]) for c in hand2]
    hand2Values.sort(reverse=True)
    for i in range(5):
        if hand1Values[i] == hand2Values[i]:
            continue
        return hand1Values[i] > hand2Values[i]
    print("wtffff")
    return False




def didPlayer1Win(hand1, hand2):
    if highestRankForHand(hand1) > highestRankForHand(hand2):
        return True
    if highestRankForHand(hand1) == highestRankForHand(hand2):
        return smartCompare(hand1, hand2)
    return False

def valueToInt(cardValue):
    if cardValue == "T":
        return 10
    if cardValue == "J":
        return 11
    if cardValue == "Q":
        return 12
    if cardValue == "K":
        return 13
    if cardValue == "A":
        return 14
    return int(cardValue)

def highestCard(hand):
    return max([valueToInt(card[:-1]) for card in hand])

def isPair(hand):
    distinctValues = dict()
    for card in hand:
        cardVal = card[:-1]
        if cardVal in distinctValues.keys():
            distinctValues[cardVal] += 1
        else:
            distinctValues[cardVal] = 1
    values = list(distinctValues.values())
    values.sort()
    return values == [1, 1, 1, 2]

def isTwoPairs(hand):
    distinctValues = dict()
    for card in hand:
        cardVal = card[:-1]
        if cardVal in distinctValues.keys():
            distinctValues[cardVal] += 1
        else:
            distinctValues[cardVal] = 1
    values = list(distinctValues.values())
    values.sort()
    return values == [1, 2, 2]


def isThreeOfAKind(hand):
    distinctValues = dict()
    for card in hand:
        cardVal = card[:-1]
        if cardVal in distinctValues.keys():
            distinctValues[cardVal] += 1
        else:
            distinctValues[cardVal] = 1
    return 3 in distinctValues.values()

def isStraight(hand):
    values = []
    for card in hand:
        value = card[:-1]
        values += [valueToInt(value)]
    if len(set(values)) != 5:
        return False
    values.sort()
    if values == [2, 3, 4, 5, 14]:
        return True
    for index in range(4):
        if values[index] != values[index + 1] - 1:
            return False
    return True

def isFlush(hand):
    suits = [x[-1] for x in hand]
    return len(set(suits)) == 1


def isFullHouse(hand):
    hand = [x[:-1] for x in hand]
    pairs = [valueToInt(x) for x in hand if hand.count(x) == 3]
    pairs.sort(reverse=True)
    single = [valueToInt(x) for x in hand if hand.count(x) == 2]
    return len(pairs) > 0 and len(single) > 0

def isFourOfAKind(hand):
    distinctValues = dict()
    for card in hand:
        cardVal = card[:-1]
        if cardVal in distinctValues.keys():
            distinctValues[cardVal] += 1
        else:
            distinctValues[cardVal] = 1
    return 4 in distinctValues.values()

def isStraightFlush(hand):
    firstCardSuit = hand[0][-1]
    values = []
    for card in hand:
        suit = card[-1]
        if suit != firstCardSuit:
            return False
        value = card[:-1]
        values += [valueToInt(value)]
    if len(set(values)) != 5:
        return False
    values.sort()
    if values == [2, 3, 4, 5, 14]:
        return True
    for index in range(4):
        if values[index] != values[index + 1] - 1:
            return False
    return True


def isRoyalFlush(hand):
    firstCardSuit = hand[0][-1]
    values = []
    for card in hand:
        suit = card[-1]
        if suit != firstCardSuit:
            return False
        values += card[:-1]
    return set(values) == {"T", "J", "Q", "K", "A"}

player1winsCount = 0
for hand in hands:
    cards = hand.split()
    p1hand = cards[:5]
    p2hand = cards[5:]
    if didPlayer1Win(p1hand, p2hand):
        player1winsCount += 1

print(player1winsCount)