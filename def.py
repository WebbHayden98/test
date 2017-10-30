def cardname(hand1,hand2):
    if hand1 == 11:
      acevalue = hvalue - 10
      hand1 = 'Ace'
      print 'Your hand value could also be: ', acevalue

    if hand1 == 10:
      crown = random.randint (1,3)
       if crown == 1:
         hand1 = 'Jack'
       elif crown == 2:
	     hand1 = 'Queen'
       elif crown == 3:
	     hand1 = 'King'
