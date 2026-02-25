#1.Create a program capable of dispalying questions to the user like KBC! 
#2.Use the list data types to store the questions and their correct answers.
#3.Display the final amount the peron is taking home after playing the game.

print("WELCOME TO KBC!")
print("Rules:Give the answer number in the answer. No cheating!!")
lst=["1.Which is the national game of Bharat?",'2.Who is the president of Russia' ,'3.What is the formula of comman salt?' ,'4.Who is the CEO of Google?', '5.What is the square of 45?']
ans=["a.Hockey b.Cricket c.Golf d.No national game", 'a.N.Modi b.D.Trump c.V.Putin d.K.J.Un', 'a.NaCl b.H2o c.HCl d.H2So4', 'a.Elon Musk b.Sundar Pichai c.Srijan Mishra d.N.Modi','a.2345 b.2025 c.346 d.1234']
print(lst[0])
print(ans[0])
get=str(input("Enter the answer:"))
if get=='d':
    print("Correct answer! You won Rs.10,000")
else :
    print("Sorry!Incorrect answer")

print(lst[1])
print(ans[1])
get=str(input("Enter the answer:"))
if get=='c':
    print("Correct answer! You won Rs.10,000")
else :
    print("Sorry!Incorrect answer")

print(lst[2])
print(ans[2])
get=str(input("Enter the answer:"))
if get=='a':
    print("Correct answer! You won Rs.10,000")
else :
    print("Sorry!Incorrect answer")

print(lst[3])
print(ans[3])
get=str(input("Enter the answer:"))
if get=='b':
    print("Correct answer! You won Rs.10,000")
else :
    print("Sorry!Incorrect answer")

print(lst[4])
print(ans[4])
get=str(input("Enter the answer:"))
if get=='b':
    print("Correct answer!You won Rs.10,000")
else :
    print("Sorry!Incorrect answer.Better luck next time!")

c=int(input("How many do you have corrected?"))
if c==1:
    print("You won Rs.10,000!!")
elif c==2:
    print("You have won Rs.20,000!!")
elif c==3:
    print("You have won Rs.30,000!!")
elif c==4:
    print("You have won Rs.40,000!!")
elif c==5:
    print("You have won the highest amount Rs.50,000!!")



