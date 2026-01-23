# list : 0개 이상의 데이터를 저장
alex = ["Alex", "Rod", "NY"]
menus = ["Chicken", "Pizza", "Beer"]
print(menus)
print(menus[0])
print(menus[:2]) # Beer 빼고
print(menus[2:]) # Beer 만
print(menus[::-1])

# mutable : 변경 가능
menus[1] = "Pepperoni Pizza"
print(menus)

# 중첩 가능 : list 안에 list
beers = ["Stella", "Hoe", "Cass", "Terra"]
menus[2] = beers
print(menus)
print(menus[2][1])


# tuple : list랑 비슷, 소괄호 씀 (생략 가능)
songhee = ("Songhee", "Hong", 0)

# immutable
# songhee[0] = "SH" # error

# tuple unpacking
first_name, last_name, age = songhee

# swap
a = 2
b = 3
a, b = b, a
print(a, b)

result = 100, # 끝의 쉼표가 한개의 데이터를 가진 튜플을 만드는 행위
print(type(result)) # tuple


# range
print(range(10)) # 아직 값 X. 만들 준비. list 아님
print(range(5, 10))
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1]