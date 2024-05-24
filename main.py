#Asking questions to figure out if they are a golden retriever or black cat 
test_counter = 0 

test_1 = input("do you like to go the beach or the mountains? (say 1 or 2)")
test_2 = input("do you like to go the park or library? (say 1 or 2)")
test_3 = input("do you like to play sports or read? (say 1 or 2)")
test_4 = input("do you want  the superpower to fly or to be invisible? (say 1 or 2)")
test_5 = input("do you like summer or winter? (say 1 or 2)")
test_6 = input("do you like salty or sweet food? (say 1 or 2)")
test_7 = input("do you like sporty or elegant style (say 1 or 2)")

if test_1 == "1":
  test_counter += 1
if test_2 == "1":
  test_counter += 1
if test_3 == "1": 
  test_counter += 1 
if test_4 == "1": 
  test_counter += 1 
if test_5 == "1": 
  test_counter =+ 1 
if test_6 == "1":
  test_counter =+ 1 
if test_7 == "1": 
  test_counter =+ 1
#RESULTS 
if test_counter >= 4:
  print("you are a golden retrievver")
else:
  print("you are a black cat")