#
#except-try? Provides protection to the code that the program will not crash and catches the reach so that the code continues even if it was supposed to crash
#b
#Effectively prevents the program from crashing and corrects it if it has errors and improves it, thus the program also flows more and cleaner when there are unexpected cases that may cause problems and crash
#c
x: int = 88

while True:
    try:
        number = int(input('enter number: '))
        x = 88 // 0
        print('good')
    except:
        print('wrong')

#d
    age: int = int(input('what is your age: '))
    if not 20 <= age <= 100:
        raise AttributeError(f"the age {age} is not good.")
    print(f"{age} is a beautiful age.")
    try:
         20 <= age <= 100
    except:
         print('the age was NOT good')
#e
    list_len_4: list[int]=[10, 14, 25, -80]
    print('list_len_4', list_len_4)

while True:
     number:int=int(input("num?"))
     if 0 <= number <= 1000 and number == -999:
             break
     print("number is good")
     try:
         index: int = int(input("what's your index?"))
         if not 0 <= index <= 1000 and index == -999:
             print(f"{index} not in range")
     except ValueError:
             print("the value was NOT a number")