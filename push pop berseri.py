print('jumlah elemen: ')

stack2 = []
lstack = int(input())

for i in range (lstack):
    x = str(input())

    if x[0]=="+":
        stack2.append(x[1:])
        print(len(stack2))
    
    elif x[0]=="-":
        print(stack2[-1],end=';')
        stack2.pop()
        print(stack2)
