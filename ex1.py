#a
list_95_105: list[int] = [i for i in range(95, 105 +1, +1)]
print(list_95_105)
#b
list_10_20: list[int] = [i for i in range(10, 20 +1, +2)]
print(list_10_20)
#c
import random
True_False_list_random:list[str]= [random.choice([True,False]) for _ in range(5)]
print('True_False_list_random',True_False_list_random)
#D
list_random_1_100: list[int] = [random.randint(1, 100) for _ in range(10)]
print('list_random_1_100', list_random_1_100)
#e
list_random_50: list[int] = [random.randint(50, 100) for _ in range(10)]
print('list_random_>50', list_random_50)
#f
combination: list[int]= [x for x in [random.randint(1,100) for x in range(10)] if x > 50]
print('combination',combination)
#g
sentence: str = input('give me a sentence?')
without_spaces_and_letter_t:list[str] = [ letter_t for letter_t in sentence if letter_t != 't' and letter_t != ' ']
print(without_spaces_and_letter_t)
#h
list_random_10_99: list[int] = [random.randint(10, 99) for _ in range(10)]
print('list_random_10_99', list_random_10_99)
only_unity=[x % 10 for x in list_random_10_99]
print('only_aha dot', only_unity)