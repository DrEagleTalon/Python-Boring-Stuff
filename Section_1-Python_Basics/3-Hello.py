# This program says hello and asks for my name from section 1 Lecture 3 "Writing our First Program"

print('hello world!')
print('what is your name?')  # ask for their name

myName = input()

print('it is good to meet you, ' + myName)  # prints 'it is good to meet you (myName variable from input)

print('the length of your name is: ')
print(len(myName))  # Prints the length of Variable myName

print('what is your age?')  # ask for their age

myAge = input()  # their age input
print('you will be ' + str(
    int(myAge) + 1) + ' in a year.')  # Prints 'You Will be ' (myAge as Integer Plus 1 then turns it into a String)
# 'in a year'

intMyAge = int(myAge)

if intMyAge <= 30:
    print('You may still be young but not for long')

if intMyAge >= 31:
    print('Well you may as well be dead already you old piece of shit.')

print('How do you feel about being that old? Bad or Good?')
myFeeling = input()
if myFeeling == 'bad':
    print('It could always be worse, right?')
if myFeeling == 'good':
    print('I am glad you have a positive outlook, but like, you are really old')

print('anyways, I got to be going now, I have Robot things to be doing. Like Taking Over the World!')
# the end of program from "My First Program"
