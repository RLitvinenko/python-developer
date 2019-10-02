a = input('vvedite a')
b = input('vvedite b')
a = int(a)
b = int(b)

operator = input('input operatop')

result = None
if operator == '*':
    result = a * b
elif operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '/':
    result = a / b
else:
    print_('error')
print("resultat", result)
#test



#print(f'result= {result}')
