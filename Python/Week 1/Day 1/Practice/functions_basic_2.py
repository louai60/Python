def  print_and_return(arr) :
    print(arr[0])
    return arr[1]


print(print_and_return([4,9]))






def countdown(num):
    lst=[]
    for num in range(num,-1,-1):
        lst.append(num)
    return lst
print (countdown(10))

def first_plus_length(list):
    sum=list[0]+len(list)
    return sum

print(first_plus_length([4,5,8,7]))


def Values_Greater_than_Second(lst):
    int=[]
    sum=0
    for i in range(0,len(lst)):
        if (lst[i]>lst[1]):
            int.append(lst[i])
            sum+=1
    print(f"the sum is {sum} and the new list is {int}")

print(Values_Greater_than_Second([5,2,3,2,1,4]))




def create_list(size, value):
    return [value] * size

size = 5
value = 3
result = create_list(size, value)
print(result)
