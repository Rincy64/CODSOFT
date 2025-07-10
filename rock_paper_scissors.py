import random
def get_computer_choice():
  return random.choice(['rock','paper','scissors'])
def determine_winner(user,computer):
  if user==computer:
    return "tie"
  elif(user=="rock"and computer=="scissors")or\
      (user=="paper"and computer=="rock")or\
      (user=="scissors"and computer=="paper"):
     return "win"
  else:
    return "lose"
def display_result(user,computer,result):
  print(f"\n You chose:{user}")
  print(f"Computer chose:{computer}")
  if result=='win':
    print("You win this round!")
  elif result=="lose":
    print("Computer wins this round!")
  else:
    print("It's a tie!")
          
 def play_game():
   user_score=0
   computer_score=0
   while True:
     user_choice=input("\n Choose Rock,Paper,or Scissors (or 'exit' to quit):").lower()
     if user_choice=='exit':
       print("Thanks for playing!")
       print(f"Final score-You:{user_score}|Computer:{computer_score}")
       break

     if user_choice not in ['rock','paper','scissors']:
       print("Invalid input.Please try again.")
       continue

     computer_choice=get_computer_choice()
     result= determine_winner(user_choice,computer_choice)
     display_result(user_choice,computer_choice,result)

     if result=="win":
       user_score+=1
     elif result=="lose"
       computer_score+=1
     
     print(f"Score-You:{user_score}|Computer:{computer_score}")

if __name__=="__main__":
  print("Welcome to Rock-Paper-Scissors Game!")
  play_game()
