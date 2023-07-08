import random

while True:
   random_number = random.randint(1, 100)
   user_choice = int(input("Hey! Please Enter Your Guessing Number : "))
   threshold_value = 5
   if random_number == user_choice:
       print("Brilliant!, You Guessed the Number Correctly")
   elif abs(user_choice - random_number) <= threshold_value:
       print(" Hey! , You got so close. One more time", random_number)
   elif user_choice == 0:
       print(" Thank you for playing. GoodBye!")
       break
   else:
       print(" Hey! , One More time ,  Its far ",random_number)