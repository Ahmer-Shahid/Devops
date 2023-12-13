import random

def user_choice():
  choice_list = ['rock', 'paper', 'scissor']
  user_ch = input('Enter your choice (Rock / Paper / Scissor)').lower()
  if user_ch not in choice_list:
    print("Invalid choice.")
  return user_ch

def computer_choice():
  comp_ch = random.choice(['rock', 'paper', 'scissor'])
  return comp_ch

def winner(user_ch, comp_ch):
  if user_ch == comp_ch:
    return 'tie'
  elif (user_ch == 'rock' and comp_ch == 'scissor') or (user_ch == 'paper' and comp_ch == 'rock') or (user_ch == 'scissor' and comp_ch == 'paper'):
    return 'user win'
  else:
    return 'computer win'
  
  if __name__ == '__main__':
    play_again = 1
    while play_again:
        user_ch = user_choice()
        comp_ch = computer_choice()
        print(f"The computer's choice is: {comp_ch}")

        print(winner(user_ch, comp_ch))

        play_again = int(input("wanna play again? (0/1)"))
    
    print("Better luck next time...")