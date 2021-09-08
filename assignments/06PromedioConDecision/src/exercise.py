def main():
   a=float(input())
suma=a
i=0
while a>0:
    a=float(input())
    i=i+1
    if a>0:
     suma=suma+a
if a<=0:
    prom=suma/i
    print(prom)
    pass
if __name__=='__main__':
    main()
