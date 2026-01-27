# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    return dictionary.keys()

# key_list = []
# def get_all_keys_from_dict(dictionary):
#     key_list.extend(dictionary.keys())

#     for value in dictionary.values():
#         if type(value) == dict:
#             get_all_keys_from_dict(value)

#     return key_list

def get_all_keys_from_dict(dictionary):
    # 1. 현재 딕셔너리의 키들을 리스트로 만듦
    keys = list(dictionary.keys())
    
    # 2. 값들을 순회하며 또 다른 딕셔너리가 있는지 확인
    for value in dictionary.values():
        if isinstance(value, dict): # type()보다 isinstance()가 더 안전함
            # 3. 재귀 호출로 가져온 키들을 리스트에 추가
            keys.extend(get_all_keys_from_dict(value))
            
    return keys

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
