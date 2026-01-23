hello_world = 'hello world'
hello_world = "hello world"

quotations = '따옴표 안에 "큰따옴표"'
quotations = "큰 따옴표 안에 '따옴표'"

escape = "Hello, my name \tis \nSonghee"
escape = "따옴표 내부의 따옴표는 \'탈출\'시켜라"
print(escape)

# String Interpolation : f-string
name = "Songhee"
greeting = f'hello, {name}'
print(greeting)

a = 2
b = 3
result = f'{a} + {b} = {a + b}'
print(result)

# indexing
print(name[3])

# slicing [start:end:step]
print(name[3:])
print(name[:3])
print(name[1:3])
print(name[::-1])
print(name[3:1:-1]) # 역순일땐 큰 수가 앞