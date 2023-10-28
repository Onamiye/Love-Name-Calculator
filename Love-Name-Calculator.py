print("Welcome to the Love Name Calculator")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = (name1+name2).lower()
check1 = "true"
check2 = "love"
counter_1 = 0
counter_2 = 0
for name in names:
  if name in check1:
    counter_1+=1
  if name in check2:
    counter_2 += 1

Love_score = int(str(counter_1)+str(counter_2))


if  Love_score <=30: 
  print(f"Your score is {Love_score}, you should break up.")
elif Love_score >90:
  print(f"Your score is {Love_score}, you are soulmates.")
elif Love_score >40 and Love_score<50:
  print(f"Your score is {Love_score}, maybe not soulmates but you'll be alright.")
else:
  print(f"Your score is {Love_score}, take your chances, it could be an hit or a miss")
  
