for i in range(1,151):
    print(i)


#Multiples of Five
for i in range(5,1000,5):
    print(i)


#Counting, the Dojo Way 
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)




#Whoa. That Sucker's Huge 
sum_of_odds = 0

for i in range(1, 500001, 2):
    sum_of_odds += i

print(sum_of_odds)


#Countdown by Fours 
for i in range(2018,0,-4):
    print(i)



#Flexible Counter
low_num=3
high_num=8
mult=2
for i in range(3,8+1):
    if i%2==0:
        print(i)
