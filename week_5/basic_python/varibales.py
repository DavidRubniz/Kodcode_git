num = input('enter number: ')
print(num=='7')

a =4
b =5
a+=b

age = int(input('enter your age: '))
if age < 0 or age > 120:
    print('Invalid')
elif age <= 12 and age > 0:
    print('Child')
elif age < 17 and age >= 12:
    print('Teen')
else:
    print('Adult')

char = input('enter a character: ')
if not char.isalpha():
    print('Invalid')
elif char in "aeiou":
    print('Vowel')
else:
    print('Consonant')

age2 = int(input('enter your age: '))
if age2 >= 16:
    vip = input('you have a vip card? (yes/no): ')
    if (vip == 'yes' and age2 >=18) or age2 in [19,20,21]:
        print('Wellcome')
    else:
        print('premission denied')

passwd = 'ygfdswer'
inp_passwd = input('enter a password')
if passwd == inp_passwd:
    print('Access Granted')
elif len(inp_passwd) < 8:
    print('too short')
else:
    print('Wrong password')

x = int(input('enter the x'))
y = int(input('enter the y'))
if 10 > x > 50 and 20< y < 80:
    print('inside the rectangle')
elif x in [10,50] and y in [20,80]:
    print('on the edge')
else:
    print('outside the rectangle')

name = input('enter your name: ')
print(f'wellcome {name or 'anonymous'}')

num_123 = input('enter three numbers: ').split(' ')
counter = 0
for i in num_123:
    counter =+ (int(i)>0)

score = int(input('enter a score: '))
print('a' if 90 <= score <= 101 else 'b' if score > 80 else 'c' if score > 70 else 'f')


