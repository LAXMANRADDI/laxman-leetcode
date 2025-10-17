a = int ( input ( ' enter nuum 1 '))
b = int ( input ( ' enter nuum 2 '))
while a % b != 0:
        r = a % b
        a = b 
        b = r
print(f'{b} is greatest common divisor')
#####################################################################################
a = int(input('Enter num 1: '))
b = int(input('Enter num 2: '))
a = abs(a)
b = abs(b)
while b != 0:
    a, b = b, a % b
print('The greatest common divisor is:', a)
