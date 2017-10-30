import random
def begin():
    Begin = raw_input('Shall I deal you in? [Y/N]: ')

    if Begin == 'Y' or Begin == 'y' or Begin == 'yes' or Begin == 'Yes':
      print 'Excelent, here is your hand sir.'
      return True

    elif Begin == 'N' or Begin == 'n' or Begin == 'no' or Begin == 'No':
      print 'Good day sir.'
      return False

    elif len(Begin) == 0:
      print 'Input Empty'
    else:
      print 'Invalid Input'
def cardname(hand):
    deck = [2,3,4,5,6,7,8,9,'Jack','Queen','King','Ace']
    return deck[hand]
def Hit(handv):
    if handv > 21:
      print 'You have bust!'
      return False
    else:
      hit = raw_input('Would you like to "Hit"? [Y/N]: ')
      if hit == 'Y' or hit == 'y' or hit == 'yes' or hit == 'Yes':
        return True

      elif hit == 'N' or hit == 'n' or hit == 'no' or hit == 'No':
        return False

      elif len(Begin) == 0:
        print 'Input Empty.'
      else:
        print 'Invalid Input.'
def cardvalue(cardnum):
    table = [2,3,4,5,6,7,8,9,10,10,10,11]
    return table[cardnum]
while True:
    start = begin()
    if start == False:
      break
    elif start == True:
        print 'test'
        hand1 = random.randint(0,11)
        hand2 = random.randint(0,11)
        dealerh1 = random.randint(0,11)
        dealerh2 = random.randint(0,11)
        card1 = cardname(hand1)
        card2 = cardname(hand2)
        dealerc1 = cardname(dealerh1)
        dealerc2 = cardname(dealerh2)
        hand1cv = cardvalue(hand1)
        hand2cv = cardvalue(hand2)
        dealer1cv = cardvalue(dealerh1)
        dealer2cv = cardvalue(dealerh2)
        handv = hand1cv + hand2cv
        dealerv = dealer1cv + dealer2cv
        print 'You hold a %s and a %s.' % (card1, card2)
        print 'The dealer reveals a %s.' % (dealerc1)
        while True:
            hit = Hit(handv)
            if hit == False:
                break
            elif hit == True:
                newcard = random.randint(0,11)
                newcardv = cardvalue(newcard)
                newcardn = cardname(newcard)
                handv = handv + newcardv
                print 'You have been dealt a %s.' % (newcardn)
        print 'The dealer flips over a %s.' % (dealerc2)
        if dealerv < 18
