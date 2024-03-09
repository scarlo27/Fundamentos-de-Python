import random

#definiendo la funcion que verificara los numeros que coinciden en dos listas dadas
def fn_comparar(lst1,lst2):
    aciertos=[]
    for i in lst1:
        for j in lst2:
            if i == j:
                x=lst2.count(i)    
                print("\nObtuviste "+str(x)+" acierto/s con el numero "+ str(i))
                aciertos.append(i)
                break
    if len(aciertos)<1:
        print("\n"+nombre +", no has logrado ningun acierto\n")

# mensaje de bienvenida
print ("Bienvenido a su loteria de la suerte!\n");

# captura del nombre del participante
nombre=input("Por favor ingrese su nombre: ");

print("\nPara mayor probabilidad de ganar, ingrese numeros del 1 al 10\n")

def fn_principal():
    
    # definicion de lista de numeros del participante
    lista=[]
    ganadores=[]
    

    # cargando la lista con los numeros del participante
    try:
        n1=int(input("Por favor ingrese su primer numero: "))
        
        while n1>10 or n1<1:            
            n1=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 

        lista.append(n1);
    except:
        n1=int(input("Ingrese un numero valido: "))
    
        while n1>10 or n1<1:            
            n1=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 

        lista.append(n1);

    try:
        n2=int(input("Por favor ingrese su segundo numero: "))
        
        while n2>10 or n2<1:            
            n2=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 

        lista.append(n2);
    except:
        n2=int(input("Ingrese un numero valido: "))
        
        while n2>10 or n2<1:            
            n2=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 
        
        lista.append(n2);

    try:
        n3=int(input("Por favor ingrese su tercer numero: "))
        
        while n3>10 or n3<1:            
            n3=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 
        
        lista.append(n3);
    except:
        n3=int(input("Ingrese un numero valido: "))
        
        while n3>10 or n3<1:            
            n3=int(input("Por favor ingrese un numero mayor que 0 y menor a 10: ")) 
        
        lista.append(n3);

    #bucle que agrega los 3 a la lista ganadores, desde el rango previamente declarado
    ln = 0
    while ln < 3:
        ganadores.append(random.randrange(1, 11))
        ln=len(ganadores)

    #imprimiendo listas
    print("\nEsta es su eleccion de numero: ");
    print(lista)
    print("\nEstos fueron los numeros ganadores: ");
    print(ganadores)

    #utilizando la funcion
    fn_comparar(lista,ganadores)

fn_principal()

resp = input("\nQuieres volver a jugar? s/n \n")
while  resp == 's':   #   Mientras no sea una opción válida repites
    
    fn_principal()
    resp = input("\nQuieres volver a jugar? s/n \n") 
   