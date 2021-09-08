def main():
    #escribe tu código abajo de esta línea
    Valor= int(input())
    i=0
    for numero in range (Valor):
        i=i+1
        if numero%2==0:
            print(str(i)+"-#")
        else:
            print(str(i)+"-%")
if __name__=='__main__':   
    main()
