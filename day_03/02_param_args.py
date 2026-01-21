def make_greeting(name, year):
    """
    사람에게 현재 연도를 바탕으로
    나이를 알려주는 문자열을 반환하는 함수
    
    :param name: 사람
    :param year: 출생 연도
    """

    return f'Hello, {name}. You are {2026 - year + 1} years old.'

# positional argument : 위치 인자
# 매개변수의 순서에 맞춰 인자를 전달하는 방법
print(make_greeting("Songhee", 1996))

# keyword argument : 키워드 인자
# 매개변수의 이름을 바탕으로 인자를 전달하는 방법
print(make_greeting(year=1996, name="Songhee"))

# default parameter : 기본 인자
def make_greeting(name="Songhee", year=1996):
    return f'Hello, {name}. You are {2026 - year + 1} years old.'

print(make_greeting())
print(make_greeting(name="Alex"))
print(make_greeting("Brad"))
print(make_greeting(year=2024))
# print(make_greeting(year=2024, "Alex")) # 오류남