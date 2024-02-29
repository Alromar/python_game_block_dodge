# tuts https://www.youtube.com/watch?v=Uo2p3znYhig
#1: for loop nuttig om
    # door lists te bladeren
    # even en oneven getallen te printen
    # om gemiddeld gewicht te bepalen
        # maak list met will getallen
        # maak var totaal en stel gelijk aan 0
        # maak een for loop
            # increment totaal met += iterator value 'weight'
        #maak een var met len() voor de gewichten
        # maak een var en deel het aantal spelers door de len-variabele
        # maak een lijst met gewicht en hun index
        # loop door een lijst met de enumerate keyword om index en iterator te krijgen

import random

grocery_list = ["milk", "toast","eggs", "avocados"]
for i in range(10):
    print('hello world')
    print(i)
    if i % 2 == 1:
        print(i)
    else:
        pass



for item in grocery_list:
   print(item)

weights = [171, 182, 190, 171, 182, 182, 191, 202, 187, 183, 179, 207, 209]
total_weight = 0
for weight in weights:
    print(weight, end=' ')
    total_weight += weight

print(total_weight)

number_of_players = len(weights)

print(number_of_players)

print(total_weight/number_of_players)

# 'index in'-method om uit meerdere sets, weight & weight2, indexes van data te halen
for index in range(len(weights)):
    # print(index)
    weight = weights[index]
    # weight2 = weights[index+1]
    total_weight += weight
print(total_weight)

number_of_players = len(weights)

print(number_of_players)

for index, weight in enumerate(weights):
    print(index, end=' ')
    print(weight)
print(total_weight)

number_of_players = len(weights)

# 2 while loops if statement dat zichezlef blijft controleren
    # voor Boolean conditionals bijv game over

i = 0
while i < 10:
    print('while-loop: ',i)
    print(i)
    i +=1

game_over = False
# doel van spel: 100 halen
    # 1: score var
score = 0



while not game_over:
    # print('playing game')
    #1
    score += random.randint(1,10)
    print('game-score:', score, end='\n')

    #3 als de score boven de 50 is exit de continue statement uit de inner-loop
    if score < 50:
        continue
    # 2 als de score boven de 100 komt, game-over
    if score > 100:
        game_over = True
        # statement om abrupt te eindigen
        break

    print('game is still on!!!')
    print('you are getting close to winning!!!')

# coding-bat exercise https://codingbat.com/prob/p193507

nums = [1, 1, 2, 1, 2, 3]


def array123(nums):
    # for num in nums:
    for i in range(len(nums)):
        firstValue = nums[i]
        secondValue = nums[i+1]
        thirdValue = nums[i+2]
        if firstValue == 1 and secondValue == 2 and thirdValue == 3:
            return True
    return False

    # return ""


print(array123(nums))
print('\n')









# tut: https://www.youtube.com/watch?v=Uo2p3znYhig
# willekeurige nummers genereren in range



# 3 importeer random lib


#2: list logic
    # input var als arg doorgeven
    # waarden input var in een result var weergeven

# 4: gebruik de randint method uit random lib en
# typ + 1 als value voor end
    # van het random.randint statement een variabele maken en toevoegen als temporary variable aan de result list
# return statment maken

def randomNumberList(numbers, startRange, endRange):
    result = []

    for i in range(numbers):
        temp = random.randint(startRange, endRange + 1)
        result.append(temp)
    return result



#1: input vars
numbers =int(input('How many numbers do you wish to generate in the list? '))
startRange =int(input('What is the starting range? '))
endRange =int(input('What is the ending range? '))

# 6: method callen function en printen
print('Generate number list:{0}'.format(randomNumberList(numbers, startRange, endRange)))


