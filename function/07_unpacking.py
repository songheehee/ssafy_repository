number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = {
        "name": name,
        "age": age,
        "address": address
    }

    print(f'{name}님 환영합니다!')

    return user_info

many_user = list(map(create_user, name, age, address)) # 인자 값만큼

def rental_book(info):
    name, age = info.popitem()
    number = age // 10
    decrease_book(number)
    print(f'{name}님의 {number}권의 책을 대여하였습니다.')

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')


user_info = list(map(lambda user: {user["name"] : user["age"]}, many_user))

# for user in many_user:
#     user_info.append({
#         user["name"] : user["age"]
#     })

list(map(rental_book, user_info)) # map은 지연 평가 특성으로 즉시 실행되지 않으므로, list()로 감쌈

# for user in user_info:
#     rental_book(user)