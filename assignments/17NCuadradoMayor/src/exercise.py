def main():
    #Escribe tu código debajo de esta línea
    Valor= int(input("Escribe un numero : "))
    Vi=1
    while Valor> Vi**2:
        Vi=Vi+1
        variable=Vi**2
        if variable>Valor:
            print(Vi)
            
if __name__=='__main__':
    main()
