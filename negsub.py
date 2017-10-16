while True:

  pyg = 'ay'

  original = raw_input('Enter a word:')

  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
    if new_word == "topsay":
      break
  elif len(original) > 0 and not original.isalpha():
    print 'Invalid Input'
  else:
    print 'Input Empty'