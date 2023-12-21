# Scramble is a good exercise for practicing recursion

def scramble(r_letters, s_letters):
  if len(r_letters) == 0:
    # base case: all letters used
    print(s_letters)
  else:
    # recursive case: for each call to scramble()
    # move a letter from remaining to scrambled
    for i in range(len(r_letters)):
      # the letter at index i will be scrambled
      scramble_letter = r_letters[i]

      # remove letter to scramble from remaining letters list
      remaining_letters = r_letters[:i] + r_letters[i+1:]

      # scramble letter
      scramble(remaining_letters, s_letters + scramble_letter)

myInput = input('Enter a word you want scrambled for some reason: ')
scramble(myInput, '')