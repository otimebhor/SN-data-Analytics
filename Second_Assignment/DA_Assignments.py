#Question 1
print(int('1000'))
#Question 2
print(int(3.764))
#Question 3
num = 99.45
print('$' + str(num) +" dollars")
'''
Question 4
The type function returns the type of the specified object.
Question 5
A Boolean is a data type with two possible values.The two possible values are True and False
Question 6
The technical name for the % operator is Modulus. It gives the remainder of the division of left operand by the right
'''
#Question 7
fancy_name = 'Success'
print(fancy_name)
#Question 8
hours = int(input('Time in hours: '))
seconds = hours * 3600
print(f'The time in seconds is {seconds}')
#Question 9
'''
An easy_money function that accepts no parameters but always returns the value 100
'''
def easy_money():
     return 100
print(easy_money())
'''
A best_food_ever function that accepts no parameters but always returns the string 'Sushi'
'''
def best_food_ever():
    return 'Sushi'
print(best_food_ever())
'''
A convert_to_currency function that accepts a single parameter.
'''
def convert_to_currency(num):
    result = '$' + str(num) + ' dollars'
    return result
num = int(input('Type a number: '))
print(convert_to_currency(num))
#Question 10
def string_adder(x,y):
    if y == "":
        print(x)
    elif x == "" and y == "":
        print("")
    else:
        print(x + " " + y)

string1 = input('first_word: ')
string2 = input('second_word: ')
print(string_adder(string1, string2))

#Question 11
def long_word(word):
    if len(word) > 7 :
        return True
    else:
        return False

word = input('Enter a word: ')
print(long_word(word))


#Question 12
def same_first_and_last_letter(letter):
    if letter[0] == letter[-1]:
        return True
    else:
        return False
    
word = input('Enter a word: ')
print(same_first_and_last_letter(word))

#Question 13
def first_three_characters(word):
    return word[0:3]

word = input('Type a word: ')
print(first_three_characters(word))