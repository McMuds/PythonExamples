### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # no initiator
  # def __init__(self, value):
  #   self.value = value

  def check_for_ace(self, card):
    if card.value = 1:
    # if card.value == 1: - comparison, not assigment
      return True
    else
    # else: - no colon after the else
      return False
   

  dif highest_card(self, card1 card2):
  # dif highest_card(self, card1, card2): - needs a comma between parms
  # def highest_card(self, card1 card2): - spelled def wrong
  if card1.value > card2.value:
    return card
    # return card1 - card doesn't exist - only card1 and card2 exist
  else:
    return card2
  


def cards_total(self, cards):
  total
  # total = 0 - an uninitiated variable. Have to assign it to something
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # return "You have a total of" + str(total) - can't just concat two different types like this - must coerce the int
  
```
