numbers = [1, 2, 3, 4, 5]
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# map
raw_input = input() # 입력
num_list = map(int, raw_input.split()) # 여기서 int는 함수. 괄호 생략 가능
print(type(num_list)) # map은 매핑
print(sum(num_list))