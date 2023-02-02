num=int(input('Ingrese un numero: '))
print(num)
suma = 0
cont=1
while num>=cont:
    suma = suma + cont
    cont= cont + 3
    if suma==num:
        print('El numero es pentagonal')
        break
    elif suma>num:
        print('El numero no es pentagonal')
        break
    
    
