from typing import List


print('hello world')
a = 'char'
print(a)


def FunctiaAdaos(a, b):
    return a+b


print(FunctiaAdaos(1, 3))


def IsEven(a) -> bool:
    if a % 2 == 0:
        return True
    else:
        return False


print(IsEven(3.3))


def HowManyEvens(array:List[int]) ->int:
    counter=0
    for i in range(0, len(array)):
        if IsEven(array[i]):
            counter=counter+1
    return counter

print( HowManyEvens([1,2,3,4,5,6]))

