def crearcliente():
    while True:
        item=int(input('Ingrese el tipo de prodcuto que desea comprar\n1. Quimico\2. Farmaceutico\n 3. Biologico\n>'))
        if item==1 or item==2 or item==3:
            break
    metododepago=''
    while True:
        metododepago=input('Por favor ingresa el metodo de pago\nC. Contado\nR.Credit\n>').upper()
        if metododepago=='C' or metododepago=='R':
            break
    return {
    'rif':input('Ingrese su rif: '), 
    'tipodecompra': item, 
    'metododepago': metododepago
    }


