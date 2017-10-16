while True:
  import random
  Begin = raw_input('Shall I deal you in? [Y/N]: ')

  if Begin == 'Y' or Begin == 'y' or Begin == 'yes' or Begin == 'Yes':
    print 'Excelent, here is your hand sir.'
    hand1 = random.randint (1,11)
    hand2 = random.randint (1,11)
    hvalue = hand2 + hand1
    print 'Your hand value is: ', hvalue
    
    if hand1 == 11:
      acevalue = hvalue - 10
      hand1 = 'Ace'
      print 'Your hand value could also be: ', acevalue
    if hand2 == 11:
      hand2 = 'Ace'
      acevalue = hvalue - 10
      print 'Your hand value could also be: ', acevalue
    if hand1 == 10:
       crown = random.randint (1,3)
       if crown == 1:
         hand1 = 'Jack'
       elif crown == 2:
	 hand1 = 'Queen'
       elif crown == 3:
	 hand1 = 'King'
    if hand2 == 10:
       crown2 = random.randint (1,3)
       if crown2 == 1:
         hand2 = 'Jack'
       elif crown2 == 2:
	 hand2 = 'Queen'
       elif crown2 == 3:
	 hand2 = 'King'
    print 'Your hand consist of a %s and a %s.' % (hand1, hand2)



  elif Begin == 'N' or Begin == 'n' or Begin == 'no' or Begin == 'No':
    break

  elif len(Begin) == 0:
    print 'Input Empty'

  else:
    print 'Invalid Input'