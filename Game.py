import random
def begin():
    Begin = raw_input('Shall I deal you in? [Y/N]: ')

    if Begin == 'Y' or Begin == 'y' or Begin == 'yes' or Begin == 'Yes':
      print '\nExcelent, here is your hand sir.'
      return True

    elif Begin == 'N' or Begin == 'n' or Begin == 'no' or Begin == 'No':
      print '\nGood day sir.'
      return False

    elif len(Begin) == 0:
      print 'Input Empty.'
    else:
      print 'Invalid Input.'
def cardname(hand):
    deck = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    return deck[hand]
def Hit(handv):
    if handv > 21:
      print 'You have bust!\n'
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
    table = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return table[cardnum]
def dealerhit():
    newcard = random.randint(0,12)
    print 'The dealer flips over a/an %s.' % (cardname(newcard))
    return cardvalue(newcard)

while True:
    start = begin()
    if start == False:
      break
    elif start == True:
        hand1 = random.randint(0,12)
        hand2 = random.randint(0,12)
        dealerh1 = random.randint(0,12)
        dealerh2 = random.randint(0,12)
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
        print 'You hold a/an %s and a/an %s.\n' % (card1, card2)
        print 'The dealer shows a/an %s.\n' % (dealerc1)
        while True:
            hit = Hit(handv)
            if hit == False:
                break
            elif hit == True:
                newcard = random.randint(0,12)
                newcardv = cardvalue(newcard)
                newcardn = cardname(newcard)
                handv = handv + newcardv
                print 'You have been dealt a/an %s.' % (newcardn)
        print '\nThe dealer reveals a/an %s.' % (dealerc2)
        while dealerv < 18:
            dealerv = dealerv + dealerhit()
            if dealerv > 21:
                print 'The dealer has bust!'
        print '\nThe dealer holds a value of %s, while you hold a value of %s.' % (dealerv, handv)
        if (dealerv > handv or handv > 21) and dealerv <= 21:
            print 'The dealer has won the round.\n'
        elif dealerv == handv and handv <= 21:
            print 'It apears to be a tie.\n'
        elif (handv > dealerv or dealerv > 21) and handv <= 21:
            print 'You have won the round.\n'
        else:
            print 'It apears no one has won.\n'
