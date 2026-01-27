def ordered_difference_sets(set1, set2):
    result1 = set1 - set2
    result2 = set2 - set1

    # 1.
    # if len(result1) <= len(result2):
    #     return result1, result2
    # else:
    #     return result2, result1

    # 2.
    # return (result1, result2) if len(result1) <= len(result2) else (result2, result1)

    # 3.
    # 1) 두 차집합을 먼저 구합니다.
    diffs = (set1 - set2, set2 - set1)
    
    # 2) 길이(len)를 기준으로 정렬해서 반환합니다. (자동으로 짧은 게 앞, 긴 게 뒤)
    return tuple(sorted(diffs, key=len))