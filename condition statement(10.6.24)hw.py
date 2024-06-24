
#condition statement

x=int(input('enter number'))
if x==0:
    print('number is zero')
elif x>0:
    print('no is greater than 0')
else:
    print('no is negative')

x=input('Enter a character')
print(x)
y=["a","e","i","o","u","A","E","I","O","U"]
if x in y:
    print('value is a vowel')
else:
    print('value is not a vowel')

#palidrome
x='level'
y='level'
if x==y:
    print('it is palindrome')
else:
    print('it is not palindrome')

x=input('Enter a character')
if (x==x[::-1]):
    print('it is palindrome')
else:
    print('it is not palindrome')

#NESTED IF

x=int(input('enter the first number'))
y=int(input('enter the second number'))
z=int(input('enter the third number'))

if (x>y):
     
        if (x>z):
                print('x is greater than z')
        else:
            print('z is greater than x')
else:
    print('y is greater than x')


