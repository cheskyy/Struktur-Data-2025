def infix_to_rpn(expression):
    tingkatoperator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  #tingkatan operator
    output_stack = []  
    operator_stack = []  

    for char in expression:
        if char.isalpha():  #operand (a-z)
            output_stack.append(char)  
        elif char == '(':  #fungsi jika bertemu ()
            operator_stack.append(char)  #masukkan '(' ke stack operator
        elif char == ')':  #jika bertemu ')', pop ke bawah
            while operator_stack and operator_stack[-1] != '(':
                output_stack.append(operator_stack.pop())  #jika bertemu operator, masukkan ke output
            operator_stack.pop()  #hapus '(' dari stack
        else:  #operator ditemukan
            while (operator_stack and operator_stack[-1] != '(' and 
                   tingkatoperator.get(operator_stack[-1], 0) >= tingkatoperator[char]):
                output_stack.append(operator_stack.pop())  #pindahkan operator ke output
            operator_stack.append(char) 

    while operator_stack:  #pop semua operator yang tersisa di stack
        output_stack.append(operator_stack.pop())

    return ''.join(output_stack)

t = int(input()) 
for _ in range(t):
    expression = input().strip()
    print(infix_to_rpn(expression))


"""    "(a+(b*c))",
    "((a+b)*(z+x))",
    "((a+t)*((b+(a+c))^(c+d)))"
    """



"""
deteksi input, jika operand masukkan ke stack output
jika bertemu ) pop kebawah, saat pop kebawah jika bertemu operator, masukkan ke stack output
declare tingkatan operator
declare fungsi jika bertemu ()"""
