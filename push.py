x=int(input())

stack_a=[]
stack_min=[]

for i in range(x):
    ang = input().split(" ")
    if ang[0]== "PUSH":
        bang = int(ang[1])
        stack_a.append(bang)
        if not stack_min:
            stack_min.append(bang)
        else:
            if bang <= stack_min[-1]:
                stack_min.append(bang)
           
    elif ang[0]=="POP":
        if stack_a: 
            if stack_a[-1] == stack_min[-1]:
                stack_min.pop()
            stack_a.pop()
            
    elif ang[0] == "MIN":
        if stack_min:
            print(stack_min[-1])  # Cetak elemen teratas stack_min
        else:
            print("Stack kosong")