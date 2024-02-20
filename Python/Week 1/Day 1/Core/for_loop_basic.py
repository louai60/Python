def basic():
    for i in range(151):
        print(i)

def multiples_of_five():
    for i in range(5, 1001, 5):
        print(i)

def counting_the_dojo_way():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

def sum_of_odd_integers():
    sum_odd = 0
    for i in range(1, 500001, 2):
        sum_odd += i
    print(sum_odd)

def countdown_by_fours():
    for i in range(2018, 0, -4):
        print(i)

def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)


basic()
multiples_of_five()
counting_the_dojo_way()
sum_of_odd_integers()
countdown_by_fours()
flexible_counter(2, 9, 3)
