import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
user_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 2)  
sum_user = sum(user_cards)
sum_computer = sum(computer_cards)

def add_score(user_cards, computer_cards, sum_user, sum_computer):
  print(user_cards)
  print(computer_cards)
  if (user_cards[0] == 10 and user_cards[1] == 11) or (user_cards[0] == 11 and user_cards[1] == 10):
    print("User has BlackJack, User Wins!")
    return sum_user
  elif (computer_cards[0] == 10 and computer_cards[1] == 11) or (computer_cards[0] == 11 and computer_cards[1] == 10):
    print("Computer has BlackJack, Computer Wins!")
    return sum_computer
  if sum_user > 21:
    if user_cards[0] or user_cards[1] == 11:
      if user_cards[0] == 11:
        user_cards[0] = 1
      elif user_cards[1] == 11:
        user_cards[1] = 1
  
  sum_user = sum(user_cards)
  print(sum_user)
  print(sum_computer)
  
  if sum_user > 21:
    print("User lose.")
    return sum_user, sum_computer
    
  user_input = input("Does the user want to draw another card? (Yes/No): ")
  
  if user_input == 'Yes':
    user_cards.append(random.choice(cards))
    add_score(user_cards, computer_cards, sum_user, sum_computer)
    
  elif user_input == 'No':
    if sum_computer < 17:
      computer_cards.append(random.choice(cards))
    sum_computer = sum(computer_cards)
    if sum_computer > 21:
      print("User Won!")
    elif sum_user > sum_computer and sum_user <= 21:
      print("User Won!")
    elif sum_computer > sum_user and sum_computer <= 21:
      print("Computer Won")
    elif sum_computer == sum_user:
      print("Draw")

  return sum_user, sum_computer, sum_user, sum_computer
  
add_score(user_cards, computer_cards, sum_user, sum_computer)