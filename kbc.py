begin = "KBC :-"
question = [
"Q.1:- What is the capital of Maharashtra ?", 
"Q.2:- Who is the Prime Minister of India ?",
"Q.3:- Who discover the bulb ?",
"Q.4:- Who discover the Telephone ?",
"Q.5:- What is the capital of India ?"
]

options = [
"A=> Ranchi \nB=> Manipur \nC=> Mumbai \nD=> Lucknow",
"A=> Lalu Prasad Yadav \nB=> Rajiv Gandhi \nC=> Akhilesh Yadav \nD=> Narendra Damodardas Modi",
"A=> Elbert Einstien \nB=> Thomas Alva Edison \nC=> Issac Newton \nD=> Ramanujan",
"A=> Marie Curie  \nB=> Graham Bell \nC=> Einstien \nD=> Newton",
"A=> Gandhi Nagar \nB=> Chennai \nC=> Itanagar \nD=> New Delhi",
  ]
  
answers = [
"Answer => Mumbai",
"Answer => Narendra Damodardas modi",
"Answer => Thomas Alva Edision",
"Answer => Graham Bell",
"Answer => New Delhi",
  ]
  
print(begin,"\n") #Starting




# Question 1
print(question[0]) #Question no:- 1
print(options[0],"\n") #Giving Options
ans1 = input()
if (ans1 == "C" or ans1 == "c"):
  print("\n","You won 20.000 INR")
  print(answers[0],"\n")
  money1 = 20000
  print("Total Winning :-", money1,"\n""\n""\n")
else:
  print("Your answers is wrong","\n""\n""\n")
  money1 = 0
  print(answers[0],"\n")
# Question 1 ending
  



# Question 2
print(question[1]) #Question no:- 2
print(options[1],"\n") #Giving Options
ans2 = input()
if (ans2 == "D" or ans2 == "d"):
  print("\n","You won 20.000 INR")
  print(answers[1],"\n")
  money2 = 20000
  print("Total winning", money1 + money2,"\n""\n""\n")
else:
  print("Your answers is wrong","\n""\n""\n")
  money2 = 0
  print(answers[1],"\n")
# question 2 ending  
  



# Question 3
print(question[2]) #Question no:- 3
print(options[2],"\n") #Giving Options
ans3 = input()
if (ans3 == "B" or ans3 == "b"):
  print("\n","You won 20.000 INR")
  print(answers[2],"\n")
  money3 = 20000
  print("Total winning", money1 + money2 + money3,"\n""\n""\n")
else:
  print("Your answers is wrong","\n""\n""\n")
  money3 = 0
  print(answers[2],"\n")
# Question 3 ending  
  



# Question 4
print(question[3]) #Question no:- 4
print(options[3],"\n") #Giving Options
ans4 = input()
if (ans4 == "B" or ans4 == "b"):
  print("\n","You won 20.000 INR")
  print(answers[3],"\n")
  money4 = 20000
  print("Total winning", money1 + money2 + money3 + money4,"\n""\n""\n")
else:
  print("Your answers is wrong","\n""\n""\n")
  money4 = 0
  print(answers[3],"\n")
# question 4 ending




# Question 5 
print(question[4]) #Question no:- 5
print(options[4],"\n") #Giving Options
ans5 = input()
if (ans5 == "D" or ans5 == "d"):
  print("\n","You won 20.000 INR")
  print(answers[4],"\n")
  money5 = 20000
  print("Total winning", money1 + money2 + money3 + money4 + money5,"\n""\n""\n")
else:
  print("Your answers is wrong","\n""\n""\n")
  money5 = 0
  print(answers[4],"\n")
# question 5 ending



# Total money
total = money1 + money2 + money3 + money4 + money5



# Ends
print("Your game is finished","\n")
print("You won ==>", total)