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


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# line 21: '=' should be '=='
# line 23: colon missing from end of line 

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# line 28: 'dif' should read 'def'; comma should appear after 'card1'
# lines 29-32: should each be indented another measure
# line 30: 'card' should read 'card1'


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

# lines 38-42: should each be indented another measure
# line 38: should read 'total = 0'
# line 41: should use string interpolation i.e. should read: 'return(f"You have a total of {total}")'. Also should be less indented, so it's inline with line 39.
```
