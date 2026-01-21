# 함수
def add(x, y):
    return x + y

print(add(1, 2))


l_add = lambda x, y: x + y
print(l_add(2, 3))


print((lambda x, y: x + y)(3, 4))


# 함수도 변수로 할당 가능
assigned_add = add # 복사가 아니라 참조. 같은 메모리 주소
print(assigned_add(4, 5))


# sorted의 key는 각 아이템의 크기의 기준을 찾아주는 함수를 인자로 전달해야 한다
numbers = [3, 1, 2]
print(sorted(numbers))

students = [
    ("지민", 25),
    ("서준", 20),
    ("민우", 30)
]

def get_age(student):
    return -student[1] # 역순

print(sorted(students, key=get_age))
print(list(map(get_age, students))) # [25, 20, 30]