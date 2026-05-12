# #1
# for i in range(1,10):
#     pass
# #2
# while True:
#     passwd = input('enter a password: ')
#     if passwd == '1234':
#         print('wellcome')
#         break
#     print('try again')
#
# #3
# products =[]
# while True:
#     name = input('enter a product name or done to finish: ')
#     if name == 'done':
#         break
#     products += name
# print(products)
#
# #4
# for r in [1,2,3]:
#     for c in [1,2,3]:
#         if c == 2:
#             break
#         print((r,c))
#
# #5
# string = input('enter a string: ').lower()
# counter = 0
# for i in string:
#     if i in 'aeiou':
#         counter += 1
# print(counter)
#
# #6
# for i in range(1,6):
#     for j in range(1,6):
#         print(f'{i} * {j} = {i*j}')
#
# #7
# string2 = input('enter a string')
# final_string = ''
# for i, _ in enumerate(string2):
#     final_string += string2[-i]
# print(final_string)
#
# #8
# num8 = input('enter a number: ')
# counter8 = 0
# index8 = 0
# while True:
#     if int(num8[index8]) % 2 == 0:
#         counter8 += 1
#     if index8 == len(num8) - 1:
#         break
#     index8 += 1
# print(counter8)
#
# #9
# string9 = input('enter a string: ')
# new_string9 = ''
# for i in string9:
#     new_string9 += i*2
# print(new_string9)
#
# #10
# highest10 = 0
# while True:
#     num10 = input('enter a positive number: ')
#     if num10 == 0:
#         break
#     highest10 = max(highest10, num10)
# print(highest10)
#
# #11
# string11 = input('enter a number or a string: ')
# bool11 = True
# for i in string11:
#     if not i.isalpha() and not i.isdigit():
#         bool11 == False
# print(bool11)

#12
num12 = int(input('enter a number: '))
new_num12 = 0
last_num12 = 0
while True:
    last_num12 = num12 % 10
    new_num12 = (new_num12 * 10) + last_num12
    num12 //= 10
    if num12 == 0:
        break
print(new_num12)


