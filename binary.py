fh=open('output10.txt','w')
a=int(input('choose one 1.Binary 2.Decimal:'))
if a==1:
    binary_number=input('Enter :')
    n=int(binary_number,2)
    print(n)
    fh.write(f'{binary_number} in decimal is {str(n)} ')
if a==2:
    decimal_number=int(input('Enter: '))
    abc=bin(decimal_number)
    print(abc[2:])
    fh.write(f'{decimal_number} in binary is {str(abc)} ')
fh.close()