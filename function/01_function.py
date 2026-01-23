def make_sum(x, y):
    return x + y

print(make_sum(1, 2))

# 이율 계산
def add_interest(money, rate): # 매개변수
    money += money * (rate / 100)
    return money

print(add_interest(100, 4.2)) # 인자


# 화면에 출력하는 함수
def print_greeting(name):
    print(f'Hello, {name}')

# 호출한 곳으로 값을 반환하는 함수
def make_greeting(name):
    return f'Hi, {name}'

print(print_greeting("Songhee"))
print(make_greeting("Songhee"))