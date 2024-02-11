import sys
x = str(input("Napis w piramidzie: "))
dl = len(x);
top = int(dl/2)+3
for i in range(0,top+1):
    for j in range(0,top-i):
        sys.stdout.write(" ")
    for k in range(0,i*2+1):
        if(k==0 or k==i*2 or i==top):
            sys.stdout.write("*")
        elif(i==top-1):
            sys.stdout.write(" "+x+" *")
            break
        else:
            sys.stdout.write(" ")
    print("")