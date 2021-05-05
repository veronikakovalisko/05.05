"""
Task 1
A simple function.
Create a simple function called favorite_movie,
which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.
"""
def favorite_muvie(muv):
    print(f"My favorite movie is named{muv}")


if __name__ == '__main__':
    muv = input("enter name of muvie")
    favorite_muvie(muv)
"""
Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""
def make_country(name, capital):
    country = {name: capital}
    return country
if __name__ == '__main__':
    count_name = input("enter country`s name")
    count_capital = input("enter country`s capital")
    print(make_country(count_name, count_capital))
"""
Task 3
A simple calculator.
Create a function called make_operation, 
which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""
def make_operation(operation, elem):
    rez = 0
    x = 0
    for i in elem:
            if operation in ' + ':
                rez += i
            elif operation in ' - ':
                if x == 0:
                    rez = i
                    x += 1
                else:
                    rez -= i
            elif operation in ' * ':
                if x == 0:
                    rez = i
                    x += 1
                else:
                    rez *= i
            elif operation in ' / ':
                if x == 0:
                    rez = i
                    x += 1
                else:
                    rez = rez / i
            else:
                print(" Try enter another operation")
                break
    print(rez)

if __name__ == '__main__':
    operation = input("What should i do")
    elem = [i for i in input("enter elements")]
    for i in elem:
        if i in ' ':
           elem.remove(i)
    elem = [int(x) for x in elem]
    #print(elem)
    make_operation(operation, elem)
"""
Пишем игру виселица. Храним десяток слов и рандомно загадываем. Показываем звездочки вместо букв закрытых. 
Человек дает букву если не угадал "рисуем" ему элемент виселицы.  В виндовс можно 
"""

from random import randint
import shlex
def words(leng):
    x = randint(1, 11)
    if leng in 'uуУU':
        if x <= 5:
            word = 'привіт'
        else:
            word = 'орхідея'
    elif leng in 'eEіІ':
        if x <= 5:
            word = 'muvie'
        else:
            word = 'avangers'
    return word
def stars (word):
    for i in word:
        word = word.replace(i, '*')
    return word
def game(word, your_word):
    letter = input('letter:')
    word = chek(letter, word, your_word)
    return word
def change (n, i, word):
    print('-')
    letters = list(word)
    letters[n] = i
    return letters
def chek(letter, word, your_word):
    print('+')
    for i in your_word:
        if i in letter:
            n = your_word.find(i)
            print('++')
            word = change(n, i, word)
            return word
        else:
            continue


if __name__ == '__main__':
    your_word = words(input('which language you speek'))
    word = stars(your_word)
    print(word)
    your_word1 = list(your_word)
    num = 0
    while True:
        word = game(word, your_word)
        print(word)
        if word == your_word1:
            print("you winn")
            break
        if word == None:
            num += 1
            print(num)
        if num == 8:
            print("you lose")
            break

