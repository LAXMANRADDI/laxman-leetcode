a = int ( input ( ' enter nuum 1 '))
b = int ( input ( ' enter nuum 2 '))
while a % b != 0:
        r = a % b
        a = b 
        b = r
print(f'{b} is greatest common divisor')
